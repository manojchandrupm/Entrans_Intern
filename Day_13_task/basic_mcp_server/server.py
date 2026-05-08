# pyrefly: ignore [missing-import]
from mcp.server.fastmcp import FastMCP

import os
import platform
import psutil
import requests
import ast
import operator


mcp = FastMCP("Basic MCP Server")


# Safe calculator operations
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub, 
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def safe_eval(node):
    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.BinOp):
        left = safe_eval(node.left)
        right = safe_eval(node.right)
        op = operators[type(node.op)]
        return op(left, right)

    if isinstance(node, ast.UnaryOp):
        operand = safe_eval(node.operand)
        op = operators[type(node.op)]
        return op(operand)

    raise ValueError("Invalid expression")


@mcp.tool()
def calculator(expression: str) -> str:
    """
    Calculate a mathematical expression. 
    Example: 10 + 20 * 3
    """
    try:
        tree = ast.parse(expression, mode="eval")
        result = safe_eval(tree.body)
        return str(result)
    except Exception as e:
        return f"Calculation error: {str(e)}"


@mcp.tool()
def weather(city: str) -> str:
    """
    Get current weather for a city.
    Example: Chennai
    """
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=10)
        return response.text
    except Exception as e:
        return f"Weather error: {str(e)}"


@mcp.tool()
def file_reader(filename: str) -> str:
    """
    Read and return the content of a local .txt file.

    Use this tool whenever the user asks:
    - read a file
    - open a file
    - show file content

    Example:
    sample.txt
    """
    try:
        if not filename.endswith(".txt"):
            return "Only .txt files are allowed."

        base_dir = os.getcwd()
        file_path = os.path.join(base_dir, filename)

        if not os.path.exists(file_path):
            return "File not found."

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:
        return f"File reading error: {str(e)}"


@mcp.tool()
def system_info() -> str:
    """
    Get basic system information.
    """
    info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "processor": platform.processor(),
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
    }

    return str(info)


if __name__ == "__main__":
    mcp.run()