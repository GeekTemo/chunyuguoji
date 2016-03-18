#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gongxingfa on 16/3/18

import requests
import time
from splinter import Browser

b = Browser('chrome')
proxies = {'http': '111.56.13.174:80'}
headers = {
    'User-Agent': 'AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 MicroMessenger/6.3.13 NetType/WIFI Language/zh_CN'}
url = 'http://mp.weixin.qq.com/s?__biz=MzI5NTAyNzkzOQ==&mid=406457899&idx=2&sn=6b41c39ebcbaf58ac47028619b072e0a&scene=4#wechat_redirect'
for i in range(6000):
    requests.get(url, headers=headers, proxies=proxies)
    time.sleep(1)
