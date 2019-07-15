# -*- encoding:utf-8 -*-

import random

shenyang_randInt = random.randint(0, 100)
wangyunfei_randInt = random.randint(0, 100)

if shenyang_randInt > wangyunfei_randInt:
    print("沈洋不变，汪云飞写用户")
else:
    print("汪云不变，沈洋写用户")