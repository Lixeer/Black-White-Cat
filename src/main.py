import asyncio
import websockets
import json

# 保存所有连接的WebSocket
connected_users = set()
VALID_KEY = "caixukun66"


from libs.app import App
from libs.app import config

async def broadcast(message, sender):
    # 向所有其他连接的用户发送消息
    for user in connected_users:
        if user != sender:
            print(message)
            await user.send(message)


async def handler(websocket, path):
    # 将新连接的用户添加到集合中
    connected_users.add(websocket)
    try:
        async for message in websocket:
            data = json.loads(message)

            if data["type"] == "message":
                await broadcast(message, websocket)
    except websockets.ConnectionClosed:
        pass

    finally:
        # 连接关闭时，从集合中移除用户
        connected_users.remove(websocket)


WK = {
    "sender": "server",
    "type": "notice",
    "content": "wrong-key",
    "time": "2024-8-5-17-17",
}
RK = {
    "sender": "server",
    "type": "notice",
    "content": "right-key",
    "time": "2024-8-5-17-17",
}


async def auth_handler(websocket, path):
    # 从请求头中获取密钥
    headers = websocket.request_headers

    key = headers.get("X-Auth-Key")

    # 检查密钥是否有效
    if key != VALID_KEY:
        await websocket.send(json.dumps(WK))

        return
    # 如果密钥有效，则处理连接
    await websocket.send(json.dumps(RK))
    await handler(websocket, path)


async def main():
    print("websockets server is running ws://127.0.0.1:2048")
    async with websockets.serve(auth_handler, "0.0.0.0", 2048):
        await asyncio.Future()  # run forever


# 启动异步事件循环

app=App(address=config.ADDRESS, port=config.PORT)
if __name__=="__main__":
    asyncio.run(app.run())