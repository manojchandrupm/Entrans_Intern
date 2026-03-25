###### below client is for python websocket

# from websockets.sync.client import connect
#
# with connect("ws://localhost:8765") as websocket:
#     websocket.send("hi frd")


###### below client is for fastapi websocket
import asyncio
import websockets

# async def client():
#     uri = "ws://127.0.0.1:8000/ws/"
#     async with websockets.connect(uri) as websocket:
#         while True:
#             message = input("Enter message to send: ")
#             await websocket.send(message)
#             response = await websocket.recv()
#             print(f"Server replied: {response}")
#
# asyncio.run(client())

import asyncio
import websockets

async def client():
    uri = "ws://127.0.0.1:8000/ws/"  # must match ASGI URL exactly
    async with websockets.connect(uri) as websocket:
        while True:
            msg = input("Enter message: ")
            await websocket.send(msg)
            response = await websocket.recv()
            print("Server replied:", response)

asyncio.run(client())