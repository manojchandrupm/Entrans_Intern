import websockets
import asyncio

async def echo(websocket):
    async for message in websocket:
        print("Received:", message)
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())