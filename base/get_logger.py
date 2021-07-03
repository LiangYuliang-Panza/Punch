import logging.handlers

log_format = "%(asctime)s   %(levelname)s   [%(name)s]   " \
             "[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"


class GetLogger(object):
    """获取日志器类——实现同时输出日志到控制台和日志文件"""
    logger = None

    @classmethod
    def get_logger(cls):
        """获取日志器"""
        if cls.logger is None:
            # 实例化日志器对象，并且设置日志器日志等级
            cls.logger = logging.getLogger(name="punch_logger")
            cls.logger.setLevel(logging.INFO)
            # 实例化 控制台处理器对象 以及 按时间切割日志的处理器对象
            console_handle = logging.StreamHandler()
            time_split_handler = logging.handlers. \
                TimedRotatingFileHandler(filename="../log/punch.log",
                                         when="midnight",
                                         interval=1,
                                         backupCount=3,
                                         encoding="utf-8")
            # 实例化格式器
            formatter = logging.Formatter(fmt=log_format)

            # 为处理器设置格式器
            console_handle.setFormatter(formatter)
            time_split_handler.setFormatter(formatter)
            # 为日志器添加处理器
            cls.logger.addHandler(console_handle)
            cls.logger.addHandler(time_split_handler)
        return cls.logger
