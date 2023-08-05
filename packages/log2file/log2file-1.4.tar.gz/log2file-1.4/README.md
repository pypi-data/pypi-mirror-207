# log2file

python 自带 logging 模块的一个封装
自己的项目经常用，每次都配置一堆很麻烦，就自己封装了一个。

# 安装

```
pip install log2file
```

# 使用

```py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import log2file
import logging

# from multiprocessing import Pool
from multiprocessing.dummy import Pool
import time
import random

log2file.init(console=True, name="test")

# for root logger, don't use this or you will get many many logs,and all other loggers will be shadowed by root logger
# log2file.init(console=True)

trace_test = log2file.trace(name="test")
# this is the trace for root logger, don't use this if you have not init root logger
trace_root = log2file.trace()


for i in range(20):
    log2file.init(console=True, name=str(i))

for i in range(20):
    log2file.init(console=True, name=str(i))


@trace_test("test_test111")
def s():
    time.sleep(0.1 + random.randint(0, 100) / 1000)


@trace_root("root_debug")
def s2():
    time.sleep(0.1 + random.randint(0, 100) / 1000)


def fun(t):
    log = logging.getLogger(name=str(t))
    for i in range(100):
        s()
        log.debug("this is a test [{0}]-[{1}]".format(t, i))
        s2()


p = Pool(10)
p.map(fun, range(20))
p.close()
p.join()
```

# License

[MIT](https://github.com/pythonml/douyin_image/blob/master/LICENSE)


[version-badge]:   https://img.shields.io/badge/version-0.1-brightgreen.svg
[version-link]:    https://pypi.python.org/pypi/douyin_image/
[license-badge]:   https://img.shields.io/github/license/pythonml/douyin_image.sv
