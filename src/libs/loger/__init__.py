import inspect
import datetime

import libs.config

import enum
class Level(enum.Enum):
    NONE=0
    INFO=1
    WARN=2
    ERROR=3

class Loger:
    def __init__(self,level):
        self.level=level

    def info(self,content:str):
        if self.level>=Level.INFO.value:
            filename,line,time=self._get_call_stack()
            print(f"{time}[{Level.INFO.name}] - {content} | {filename} line:{line} ")

    def warn(self,content:str):
        if self.level>=Level.WARN.value:
            filename,line,time=self._get_call_stack()
            print(f"{time}[{Level.WARN.name}] - {content} | {filename} line:{line} ")

    def error(self,content:str):
        if self.level>=Level.ERROR.value:
            filename,line,time=self._get_call_stack()
            print(f"{time}[{Level.ERROR.name}] - {content} | {filename} line:{line} ")

    def _get_call_stack(self):
        caller_frame = inspect.stack()[2]
        # 获取上一级调用者的帧
        filename = caller_frame.filename
        lineno = caller_frame.lineno
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return filename,lineno,current_time

aloger = Loger(libs.config.LOG_LEVEL)
