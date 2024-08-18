import asyncio

from libs.app import App
from libs.app import config


# 启动异步事件循环


b="""
              ______     __     __     ______    
 /\_/\       /\  == \   /\ \  _ \ \   /\  ___\   
( o.o )      \ \  __<   \ \ \/ ".\ \  \ \ \____  
 > ^ <        \ \_____\  \ \__/".~\_\  \ \_____\ 
/     \        \/_____/   \/_/   \/_/   \/_____/ 
                                    
"""






app = App(address=config.ADDRESS, port=config.PORT)
if __name__ == "__main__":

    print(b)
    asyncio.run(app.run())