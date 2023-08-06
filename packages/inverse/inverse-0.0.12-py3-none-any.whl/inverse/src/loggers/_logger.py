import logging
import os
import sys
from pathlib import Path

from inverse.src.utils.sp_general_utils import create_dirs


def set_logger(name, file_name='logs.log') -> logging.Logger:
    path_log = Path(os.getcwd()) / 'logs'
    create_dirs(path_log)
    log_file = path_log / file_name

    logformat = f"%(name)s %(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s"
    datefmt = "%m-%d %H:%M"

    logging.basicConfig(filename=log_file, level=logging.DEBUG, filemode="a",
                        format=logformat, datefmt=datefmt)

    # stream_handler = logging.StreamHandler(sys.stderr)
    # stream_handler.setFormatter(logging.Formatter(fmt=logformat, datefmt=datefmt))

    logger = logging.getLogger(name)
    # logger.addHandler(stream_handler)

    return logger

