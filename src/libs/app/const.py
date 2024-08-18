import enum
from libs.config import lang



#en
class EN_Out(enum.Enum):
    SERVER_RUNNING = "websocket server is running"
    ILLEGAL_DATA_PACK = "wrong data pack"
    CONNECT_CLOSE = "connection closed"
    BUILDING_CONNECT = "is building connect"
    FAILURE_FOR_WRONG_KEY = "connect failure because of wrong auth-key"
    SUCCESS = "success"

#cn
class CN_Out(enum.Enum):
    SERVER_RUNNING = "websocket服务器正在运行"
    ILLEGAL_DATA_PACK = "非法的报文数据,缺少必要字段"
    CONNECT_CLOSE = "连接已断开"
    BUILDING_CONNECT = "正在建立连接"
    FAILURE_FOR_WRONG_KEY = "由于错误的请求头验证密钥,连接失败"
    SUCCESS = "连接成功"


Out=None
if lang == "en":
    Out=EN_Out
if lang == "cn":
    Out=CN_Out


