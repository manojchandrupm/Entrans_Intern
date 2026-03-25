import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SimpleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Echo the received message back to the client
        await self.send(text_data)