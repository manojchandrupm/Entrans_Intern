import asyncio
import json
import sys
from pathlib import Path

from openai import OpenAI

# pyrefly: ignore [missing-import]
from mcp import ClientSession, StdioServerParameters

# pyrefly: ignore [missing-import]
from mcp.client.stdio import stdio_client


client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

MODEL_NAME = "llama3.1:8b"


def convert_mcp_tools_to_openai_tools(mcp_tools):
    """
    Convert MCP tool schema into OpenAI-compatible tool schema.
    """
    tools = []

    for tool in mcp_tools:
        tools.append({
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description or "",
                "parameters": tool.inputSchema,
            }
        })

    return tools


async def main(question: str):
    server_path = Path(__file__).parent / "server.py"

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(server_path)]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            tools_result = await session.list_tools()
            mcp_tools = tools_result.tools

            print("\nAvailable MCP Tools:")
            for tool in mcp_tools:
                print(f"- {tool.name}: {tool.description}")

            openai_tools = convert_mcp_tools_to_openai_tools(mcp_tools)

            # while True:
            #     user_input = input("\nYou: ")

            #     if user_input.lower() in ["exit", "quit"]:
            #         print("Exiting...")
            #         break

            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant. "
                        "You MUST use ONLY the provided MCP tools. "
                        "Do NOT invent tools. "
                        "If the user asks to read a file, use the file_reader tool. "
                        "If the user asks for calculations, use calculator. "
                        "If the user asks for weather, use weather. "
                        "If the user asks for system information, use system_info."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ]

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                tools=openai_tools,
                tool_choice="auto"
            )

            assistant_message = response.choices[0].message

            if assistant_message.tool_calls:
                messages.append(assistant_message)

                for tool_call in assistant_message.tool_calls:
                    tool_name = tool_call.function.name
                    tool_args = json.loads(tool_call.function.arguments)

                    print(f"\nAI selected tool: {tool_name}")
                    print(f"Tool arguments: {tool_args}")

                    tool_result = await session.call_tool(
                        tool_name,
                        arguments=tool_args
                    )

                    tool_output = tool_result.content[0].text

                    print(f"Tool output: {tool_output}")

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_output
                    })

                final_response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=messages
                )
                if tool_name == "file_reader":
                    return tool_output

                return final_response.choices[0].message.content

            else:
                return assistant_message.content
