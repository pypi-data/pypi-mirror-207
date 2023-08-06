
import logging
import time

logger_name = "sdk"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.INFO)

fmt = "%(asctime)-15s %(levelname)s %(filename)s:%(lineno)d %(message)s"
formatter = logging.Formatter(fmt)
sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)


def enable_logging_to_file():
    logger.setLevel(logging.INFO)
    filename = "UGOT_SDK_{0}_log.txt".format(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    fh = logging.FileHandler(filename)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

# SDK_VERSION_MAJOR = 0
# SDK_VERSION_MINOR = 0
# SDK_VERSION_REVISION = 3
#
# __version__ = "{0:d}.{1:d}.{2:d}".format(SDK_VERSION_MAJOR, SDK_VERSION_MINOR, SDK_VERSION_REVISION)
#
# def get_version():
#     return __version__
