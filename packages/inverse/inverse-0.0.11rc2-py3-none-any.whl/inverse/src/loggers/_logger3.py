import datetime
import functools
import logging
import os
from typing import Any, Callable


class spLogger:
    _logger = None

    def __init__(cls, name, *args, **kwargs):
        if cls._logger is None:
            cls._logger = logging.getLogger("x1")
            cls._logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                '%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')
            now = datetime.datetime.now()
            dirname = "./logs"
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            fileHandler = logging.FileHandler(
                dirname + "/log_" + name + '_' + now.strftime("%Y-%m-%d") + ".log")
            streamHandler = logging.StreamHandler()
            fileHandler.setFormatter(formatter)
            streamHandler.setFormatter(formatter)
            cls._logger.addHandler(fileHandler)

LOGGING_ON = False

def with_logging(
        func: Callable[..., Any],
        logger: logging.Logger
) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if LOGGING_ON:
            logger.info(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        value = func(*args, **kwargs)
        # logger.info(f"Finished {func.__name__}")
        return value

    return wrapper


def get_my_logger(name):
    logger = spLogger(name)._logger
    return functools.partial(with_logging, logger=logger)


def free_logger(*args) -> Callable[..., Any]:
    logger = spLogger('free')
    return logger._logger.info(*args)

    # return functools.partial(with_logging, logger=logger)


'''
with_default_logging1 = get_my_logger('ops2')  # functools.partial(with_logging, logger=logger)
with_default_logging2 = get_my_logger('buffer3')  # functools.partial(with_logging, logger=logger2)

'''
# usage :

#
# # a simple usecase
# if __name__ == "__main__":
#     logger = spLogger('Buffer')
#     logger._logger.info("Hello, Logger")
#     logger = spLogger('DbOps')
#     logger._logger.info("Hello, Logger")
