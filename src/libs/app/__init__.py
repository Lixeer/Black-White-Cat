import json
import asyncio

import libs.config as config

import websockets

class App:
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

    def __init__(self,address :str,port :int):
        self.address = address
        self.port = port
        self.connected_users = set()


    async def _auth_bridge(self,websocket,path)->bool:
        """

        :param websocket:
        :param path:
        :return: 验证通过与否
        """
        headers = websocket.request_headers

        key = headers.get("X-Auth-Key")

        # 检查密钥是否有效
        if key != config.VALID_KEY:
            await websocket.send(json.dumps(self.WK))

            return False
        # 如果密钥有效，则处理连接
        await websocket.send(json.dumps(self.RK))
        return True

    async def _middleware(self,websocket,path):
        return True,websocket,path


    async def _handler(self,websocket,path):

        result = await self._auth_bridge(websocket,path)
        if result == False:
            return


        result,websocket,path = await self._middleware(websocket,path)
        if result == False:
            return

        self.connected_users.add(websocket)
        try:
            async for message in websocket:
                data = json.loads(message)

                if data["type"] == "message":
                    await self._broadcast(message, websocket)
        except websockets.ConnectionClosed:
            pass

        finally:
            # 连接关闭时，从集合中移除用户
            self.connected_users.remove(websocket)

    async def _broadcast(self,message, sender):
        # 向所有其他连接的用户发送消息
        for user in self.connected_users:
            if user != sender:
                print(message)
                await user.send(message)

    async def run(self):
        print(f"websockets server is running ws://{self.address}:{self.port}")
        async with websockets.serve(self._handler, self.address, self.port):
            await asyncio.Future()
