#!/usr/bin/python
# author  fengjiening
# -*- coding: UTF-8 -*-
from ctypes import *
from constants.configuration import Configuration
class FaceService:

    def __init__(self,logger,re):
        self.path = "../lib/"
        self.face = CDLL(self.path+"FaceCompare.dll")

        self.logger=logger
        self.flag = False
        self.R=re

    def Init(self):
        self.logger.info(" HKFace_Init ...")
        a=c_char_p()
        ret = self.face.Init()
        print(ret)

    def Get1stCameraID(self):
        ret = self.face.Get1stCameraID()
        print(ret)

    def Get2ndCameraID(self,st2):
        ret = self.face.Get2ndCameraID(st2)
        print(ret)

    def FaceCompare(self,imgFileName,nVISCameraID,nNIRCameraID):
        img=c_char_p(imgFileName)
        ret = self.face.FaceCompare(byref(img),nVISCameraID,nNIRCameraID)
        print(ret)

    def UnInit(self):
        self.logger.info(" HKFace_UnInit ...")
        ret = self.face.UnInit()
        print(ret)



from constants.configuration import Configuration
from constants.result import R
from util.jt_logging import JtLogging
logger =JtLogging.getLogger("card_service")
Re = R.init()
a = FaceService(logger,Re)

#a.Init()
# a.Get1stCameraID()
# a.Get2ndCameraID(1)
a.UnInit()

#a.HKFace_UnInit()
# EndTime = c_short * 5
# EndTime1 = EndTime(2003, 8, 8, 19, 11)
#
# print(dir(EndTime1))
# c=pointer(EndTime1)
# print(c)