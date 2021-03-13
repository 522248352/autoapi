import logging.handlers
import os

from config import BASE_PATH


class GetLog(object):
    # 新建一个日至期变量
    __logger = None
    # 新建获取日志器方法
    @classmethod
    def get_logger(cls):
        # 判断日志器为空
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 修改日志器默认级别
            cls.__logger.setLevel(logging.INFO)
            # 获取处理器
            log_path = os.path.join(BASE_PATH, "log", "api_log.log")
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            th.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__logger.addHandler(th)

        return cls.__logger

if __name__ == '__main__':
    a = GetLog.get_logger()
    a.info("aa")
    a.error("bb")
        