import logging

logger_path = "/var/log/pixel.log"

format = "{pixel} " \
         "time=%(asctime)s " \
         "level=%(levelname)-8s " \
         "log=%(name)-12s " \
         "process=%(process)d " \
         "thread=%(thread)d " \
         "msg=%(message)s"

formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S")
fh = logging.FileHandler(logger_path)
fh.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
