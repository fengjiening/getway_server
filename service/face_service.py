#!/usr/bin/python
# author  fengjiening
# -*- coding: UTF-8 -*-
from ctypes import *
class FaceService:

    def __init__(self,logger):
        self.logger=logger
        self.flag = False
        #self.path = "lib"
        self.path = "../lib"
        logger.info("sdk加载路径：%s" % self.path)
        try:
            self.face = CDLL(self.path + "\FaceCompare.dll")
            logger.info("加载人脸识别需要的DLL成功，开始初始化人脸识别。。。。")
            ret = self.Init()
            if ret == 1:
                self.flag = True
                logger.info("初始化人脸识别成功")
            else:
                self.flag = False
                logger.error("初始化人脸识别失败,原因【%s】"%ret)
        except Exception as e:
            logger.error("加载人脸识别所需要的DLL失败,原因【%s】"%e)



    def Init(self):
        self.logger.debug("HKFace_Init ...")
        a=c_char_p()
        ret = self.face.Init()
        return ret

    def Get1stCameraID(self):
        self.logger.debug("Get1stCameraID ...")
        ret = self.face.Get1stCameraID()
        print(ret)

    def Get2ndCameraID(self,st2):
        self.logger.debug("Get2ndCameraID ...")
        ret = self.face.Get2ndCameraID(st2)
        print(ret)

    def FaceCompare(self,imgFileName,nVISCameraID,nNIRCameraID):
        self.logger.debug("FaceCompare ...")
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

a = FaceService(logger)
a.UnInit()

#a.HKFace_UnInit()
# EndTime = c_short * 5
# EndTime1 = EndTime(2003, 8, 8, 19, 11)
#
# print(dir(EndTime1))
# c=pointer(EndTime1)
# print(c)