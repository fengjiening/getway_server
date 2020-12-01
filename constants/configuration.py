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
    CONFIG_FILE1 = "config.ini"
    #CONFIG_FILE1 = "E:\project\getway_server\config.ini"

    CARD_COM=1
    TIME=-1
    SERVER_PORT=8888
    config = configparser.ConfigParser()
    try:
        config.readfp(codecs.open(CONFIG_FILE1, "r", "utf-8-sig"))
        CARD_COM = config.get('card', 'card_com')
        APPKEY = config.get('card', 'appkey')
        DEVKEY = config.get('card', 'devkey')
        TIME= config.get('card', 'count')
        SERVER_PORT= config.get('card', 'server_port')
        CONFIG_FLAG=True
    except Exception as e:
        print(e)
        CONFIG_FLAG=False



