#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import logging.handlers
import time


def init(
    logpath="log.log",
    name=None,
    console=False,
    maxBytes=20 * 1024 * 1024,
    backupCount=10,
):
    """
    指定保存日志的文件路径，日志级别，以及调用文件
    将日志存入到指定的文件中
    """

    if name is None:
        # 给logger添加handler
        logger = logging.root
    else:
        logger = logging.getLogger(name)

    if logger.hasHandlers():
        logger.info("already initialized...")
        return

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s"
    )

    # 创建一个handler，用于写入日志文件
    fh = logging.handlers.RotatingFileHandler(
        logpath,
        maxBytes=maxBytes,
        backupCount=backupCount,
    )
    # fh.setLevel(logging.INFO)
    fh.setLevel(logging.DEBUG)

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    if console:
        ch.setLevel(logging.DEBUG)
    else:
        ch.setLevel(logging.ERROR)

    # 定义handler的输出格式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)

    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)


def trace(name=None):
    def trace(label=""):
        def handle_func(func):
            def handle_args(*args, **kwargs):
                logging.getLogger(name).debug(
                    "{1} {0} start...".format(func.__name__, label)
                )
                st = time.time()

                res = func(*args, **kwargs)

                du = time.time() - st
                logging.getLogger(name).debug(
                    "{1} {0} end cost [{2:.2f}]ms...".format(
                        func.__name__, label, du * 1000
                    )
                )
                return res

            return handle_args

        return handle_func

    return trace


if __name__ == "__main__":
    init()

    log = logging.getLogger()
    log.error("cc")
