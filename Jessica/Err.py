from functools import wraps
import logging
from logging.handlers import RotatingFileHandler


def logger(**kwargs):
    def decorate(func):
        log_level = logging.DEBUG
        level = kwargs['log_level']
        name = None
        message = None
        log_path = kwargs['log_path']
        log_format = kwargs['log_format']
        log_revision = kwargs["log_revision"]
        log_size = kwargs["log_size"]
        log_level_dict = {
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        if level in log_level_dict:
            log_level = log_level_dict[level]
        log_name = name if name else func.__module__
        log_msg = message if message else func.__name__
        log_file = "{}{}".format(log_path, '.log')
        handler = RotatingFileHandler(log_file, mode='a', maxBytes=int(log_size) * 1024 * 1024,
                                         backupCount=int(log_revision), encoding=None, delay=0)

        log = logging.getLogger(log_name)
        if len(log.handlers) == 0:
            log_formatter = logging.Formatter(log_format)
            handler.setFormatter(log_formatter)
            handler.setLevel(log_level)
            log.addHandler(handler)
        logging.basicConfig(filename=log_file, format=log_format, level=log_level)
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if level == logging.DEBUG:
                    log.log(log_level, log_msg)
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                log_msg = log_msg + e
                log.log(log_level, log_msg)
        return wrapper

    return decorate