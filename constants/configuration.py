#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author  fengjiening
import  configparser
import codecs

class Configuration(object):
    CONFIG_FLAG=False
    USE_TIME=10
    BASE_PATH = "d:/"
    CWD=BASE_PATH+"card_server"
    AUTH_PATH = "%s/" % CWD
    LOG_PATH  = "%s/log/" % CWD
    CONFIG_FILE = "%s/config.ini"  % CWD
    CONFIG_FILE1 = "config.ini"
    CARD_COM=1
    CARD_KEY=2
    CARD_KEY1=3
    TIME=-1
    SERVER_PORT=8888
    INIPATH=""
    config = configparser.ConfigParser()
    try:
        config.readfp(codecs.open(CONFIG_FILE1, "r", "utf-8-sig"))
        CONFIG_FLAG=True
        CARD_COM = config.get('card', 'card_com')
        CARD_KEY = config.get('card', 'appkey')
        CARD_KEY1 = config.get('card', 'devkey')
        TIME= config.get('card', 'count')
        SERVER_PORT= config.get('card', 'server_port')
        INIPATH = config.get('card', 'inipath')
    except Exception as e:
        CONFIG_FLAG=False



