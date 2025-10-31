# from fastapi import FastAPI, WebSocket
# from fastapi.responses import HTMLResponse
# import uvicorn
#
# app = FastAPI()
# connections = set()
#
# @app.websocket("/ws")
# async def websocket_endpoint(ws: WebSocket):
#     await ws.accept()
#     connections.add(ws)
#     print(f"🔗 Client connected ({len(connections)} total)")
#     try:
#         while True:
#             data = await ws.receive_text()
#             for conn in list(connections):
#                 if conn != ws:
#                     await conn.send_text(data)
#     except Exception as e:
#         print("❌ Disconnected:", e)
#     finally:
#         connections.remove(ws)
#         print(f"🧹 Client removed ({len(connections)} left)")
#
# @app.get("/")
# async def get():
#     with open("index.html", "r", encoding="utf-8") as f:
#         return HTMLResponse(f.read())
#
# if __name__ == "__main__":
#     uvicorn.run("server:app", host="0.0.0.0", port=8000)



# from fastapi import FastAPI, WebSocket
# from fastapi.responses import HTMLResponse
# import uvicorn
#
# app = FastAPI()
# connections = set()
#
# @app.websocket("/ws")
# async def websocket_endpoint(ws: WebSocket):
#     await ws.accept()
#     connections.add(ws)
#     print(f"🔗 Client connected. Total: {len(connections)}")
#
#     try:
#         while True:
#             data = await ws.receive_text()
#             # relay offer/answer/ICE to all others
#             for conn in list(connections):
#                 if conn != ws:
#                     await conn.send_text(data)
#     except:
#         print("❌ Client disconnected")
#         connections.remove(ws)
#
# @app.get("/")
# async def get():
#     return HTMLResponse(open("index.html").read())
#
# if __name__ == "__main__":
#     print("🚀 Signaling Server Running on http://0.0.0.0:8000")
#     uvicorn.run(app, host="0.0.0.0", port=8000)


