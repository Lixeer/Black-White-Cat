import asyncio
import websockets
import json



from libs.app import App
from libs.app import config


# 启动异步事件循环

app=App(address=config.ADDRESS, port=config.PORT)
if __name__=="__main__":
    asyncio.run(app.run())