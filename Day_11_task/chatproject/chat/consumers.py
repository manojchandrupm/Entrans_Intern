import json
from channels.generic.websocket import AsyncWebsocketConsumer
import ollama
import asyncio

MAX_HISTORY = 10 

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected!")
        self.chat_history = []
        await self.accept()

    async def disconnect(self, close_code):
        print("WebSocket disconnected")

    async def receive(self, text_data):
        print("Message received:", text_data)
        data = json.loads(text_data)
        message = data['message']
        
        self.chat_history.append({"role": "user", "content": message})
        self.chat_history = self.chat_history[-MAX_HISTORY:]
        
        context = ""
        for msg in self.chat_history:
            role = "User" if msg["role"] == "user" else "AI"
            context += f"{role}: {msg['content']}\n"

        prompt = f"""
        You are a friendly, human-like AI chatbot.
        Respond naturally and warmly.
        Use the chat history to maintain context.

        Chat History:
        {context}

        User Message:
        {message}

        Reply naturally:
        """

        try:
            answer = await asyncio.to_thread(
                lambda: ollama.chat(
                    model="llama3:8b",
                    messages=[{"role": "user", "content": prompt}]
                )['message']['content']
            )
        except Exception as e:
            answer = "Error generating answer: " + str(e)
            
        self.chat_history.append({"role": "ai", "content": answer})
            
        await self.send(text_data=json.dumps({
            "message": answer
        }))