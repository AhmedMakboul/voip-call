# from fastapi import FastAPI, WebSocket
# from fastapi.responses import HTMLResponse
#
# app = FastAPI()
# connections = set()
#
# @app.websocket("/ws")
# async def websocket_endpoint(ws: WebSocket):
#     await ws.accept()
#     connections.add(ws)
#     try:
#         while True:
#             data = await ws.receive_text()
#             # relay offer/answer/ICE to all others
#             for conn in list(connections):
#                 if conn != ws:
#                     await conn.send_text(data)
#     except:
#         connections.remove(ws)
#
# @app.get("/")
# async def get():
#     return HTMLResponse(open("index.html").read())
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()
connections = {}  # {client_id: WebSocket}


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(ws: WebSocket, client_id: str):
    await ws.accept()
    connections[client_id] = ws
    print(f"✅ {client_id} connected. {len(connections)} clients online.")

    try:
        while True:
            data = await ws.receive_text()
            # Expect messages like {"to": "user2", "offer": {...}}
            # Here we just relay to everyone else
            for target_id, target_ws in connections.items():
                if target_id != client_id:
                    await target_ws.send_text(data)
    except WebSocketDisconnect:
        # Handle disconnect cleanly
        connections.pop(client_id, None)
        print(f"❌ {client_id} disconnected.")
    except Exception as e:
        print(f"⚠️ Error with {client_id}: {e}")
        connections.pop(client_id, None)


@app.get("/")
async def get():
    # ✅ Fix UnicodeDecodeError by forcing UTF-8 encoding
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(content=html)

