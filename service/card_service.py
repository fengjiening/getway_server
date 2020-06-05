#!/usr/bin/python
# author  fengjiening
# -*- coding: UTF-8 -*-
from ctypes import *
from constants.configuration import Configuration
class Service:

    def __init__(self,logger,re):
        #self.path = "lib/"
        self.path = ""
        self.lock = CDLL(self.path+"Hotellock.dll")
        # CDLL(self.path + "CP2101.dll")
        # CDLL(self.path + "CLSIC32.dll")
        # CDLL(self.path + "EasyD12.dll")
        # CDLL(self.path + "EasyD12_500.dll")
        # CDLL(self.path + "CLSIC32.dll")
        # CDLL(self.path + "Ib97e32.dll")
        # CDLL(self.path + "Ibfs32.dll")
        # CDLL(self.path + "Ib97u32.dll")
        # CDLL(self.path + "Mwic_32.dll")
        # CDLL(self.path + "RC500_232.dll")
        # CDLL(self.path + "RC500USB.dll")
        # CDLL(self.path + "TUTIL32.dll")

        self.logger=logger
        self.flag = False
        self.R=re

    def EncodeInit(self):
        self.logger.info(" 读取门锁Ini文件 EncodeInit")
        ret = self.lock.EncodeInit(bytes(Configuration.INIPATH,"utf-8"))
        if ret == 1:
            return self.R.success()
        else:
            return self.R.error([],"操作失败:::ERROR_CODE【%s】"%ret)

    def MakeGuestCard(self,c,r,s,e,enOverride ):
        self.logger.info(" 制宾客卡 MakeGuestCard")
        room = c_short(r)
        nu = c_short(c)
        enOverride=c_short(enOverride )
        p=pointer(c_short())

        StartTime = c_short * 5
        StartTime1 = StartTime(int(s[0]),int(s[1]), int(s[2]),int( s[3]),int( s[4]))
        EndTime=c_short * 5
        EndTime1=EndTime(int(e[0]),int(e[1]),int( e[2]),int( e[3]),int( e[4]))
        ret = self.lock.MakeGuestCard(pointer(nu),p,c_short(0),p,p,pointer(room),enOverride,p,p,pointer(StartTime1),pointer(EndTime1))
        if ret == 1:
            return self.R.success()
        else:
            return self.R.error([], "操作失败:::ERROR_CODE【%s】" % ret)

    def ReadCard(self,c,r,s,e,enOverride ):
        self.logger.info(" 读卡内容")
        room = c_short(r)
        nu = c_short(c)
        enOverride = c_short(enOverride)
        p = pointer(c_short())

        StartTime = c_short * 5
        StartTime1 = StartTime(int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]))
        EndTime = c_short * 5
        EndTime1 = EndTime(int(e[0]), int(e[1]), int(e[2]), int(e[3]), int(e[4]))
        ret = self.lock.MakeGuestCard(pointer(nu), p, c_short(0), p, p, pointer(room), enOverride, p, p, pointer(StartTime1),
                                      pointer(EndTime1))
        data={}
        if ret == 1:
            data["Rom"]=nu.value
            data["Room"] = room.value
            data["enOverride "] = enOverride.value
            data["StartTime  "] =  StartTime1[0]+","+StartTime1[1]+","+StartTime1[2]+","+StartTime1[3]+","+StartTime1[4]
            data["StartTime  "] =  EndTime1[0]+","+EndTime1[1]+","+EndTime1[2]+","+EndTime1[3]+","+EndTime1[4]
            return self.R.dSuccess(data)
        else:
            return self.R.error([], "操作失败:::ERROR_CODE【%s】" % ret)

    def ClearCardData(self,c):
        self.logger.info(" 清空卡片内容 ClearCardData")
        nu = c_short(c)
        ret = self.lock.ClearCardData(pointer(nu))
        if ret == 1:
            return self.R.success()
        else:
            return self.R.error([], "操作失败:::ERROR_CODE【%s】" % ret)

    def EncodeExit(self):
        self.logger.info(" 退出发卡系统，关闭端口 EncodeExit")
        ret = self.lock.EncodeExit()
        if ret == 1:
            return self.R.success()
        else:
            return self.R.error([], "操作失败:::ERROR_CODE【%s】" % ret)


# EndTime = c_short * 5
# EndTime1 = EndTime(2003, 8, 8, 19, 11)
#
# print(dir(EndTime1))
# c=pointer(EndTime1)
# print(c)