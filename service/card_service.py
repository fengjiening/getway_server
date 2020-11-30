#!/usr/bin/python
# author  fengjiening
# -*- coding: UTF-8 -*-
from ctypes import *
from constants.configuration import Configuration
from util.jt_logging import JtLogging
from constants.result import R
class Service:

    def __init__(self,logger,re):
        self.logger=logger
        self.flag = False
        self.R=re
        self.path ="lib"
        logger.info("sdk加载路径：%s"% self.path)
        try:
            self.card = CDLL(self.path+"\Sdtapi.dll")
            CDLL(self.path+"\dewlt.dll")
            CDLL(self.path+"\JpgDll.dll")
            CDLL(self.path+"\SavePhoto.dll")
            CDLL(self.path+"\Sdtapi.dll")
            CDLL(self.path+"\WltRS.dll")
            self.flag = True
            logger.info("加载所需要的DLL成功")
        except Exception as e:
            logger.info("加载所需要的DLL失败")

    def InitComm(self,com):
        re = self.card.InitComm(c_int(com))
        print(re)

    def CloseComm(self):
        if self.card :
            re = self.card.CloseComm()
            print(re)
        else:
            print("err")

    def CardOn (self):
        re = self.card.CardOn()
        print("sfz")
        print(re)

    def Routon_DecideIDCardType(self):
        ret= self.card.Routon_DecideIDCardType()
        return ret

    def ReadBaseMsgWPhoto(self):
        ExpireEnd = c_char_p("k".encode("gbk"))
        s="E://project".encode("gbk")
        path = c_char_p(s)

        ret= self.card.ReadBaseMsgWPhoto(ExpireEnd,path)
        print(str(ExpireEnd.value, "gbk"))
        return ret


    def Authenticate(self):
        ret = self.card.Authenticate()
        return ret


    def read(self,type):
        #读取身份证信息
        Name = c_char_p("a".encode("utf-8"))
        Gender = c_char_p("b".encode("utf-8"))
        Folk = c_char_p("c".encode("utf-8"))
        BirthDay = c_char_p("d".encode("utf-8"))
        Code = c_char_p("e".encode("utf-8"))
        Address = c_char_p("f".encode("utf-8"))
        Agency = c_char_p("g".encode("utf-8"))
        ExpireStart = c_char_p("h".encode("utf-8"))
        ExpireEnd = c_char_p("k".encode("utf-8"))
        ret = None
        if type == 100:
            #身份证卡
            ret = self.card.ReadBaseInfos(Name, Gender, Folk, BirthDay, Code, Address,  Agency,  ExpireStart,  ExpireEnd);
        # elif type == 101:
        #     #读取外国居留证
        #     ret = Routon_ReadAllForeignBaseInfos(enName, Gender, Code,Nation, cnName, BirthDay, ExpireStart, ExpireEnd,CardVertion,Agency,CardType,FutureItem);
        # elif type == 102:
        #     #读港澳台居住证
        #     ret=Routon_ReadAllGATBaseInfos(Name, Gender, FutureItem1, BirthDay, Address, Code, Agency, ExpireStart, ExpireEnd，PassID, SignCnt, FutureItem2, CardType, FutureItem3)
        print(ret,type)
        print(str(Name.value, "gbk"))
        print(str(Gender.value, "gbk"))
        print(str(Folk.value, "gbk"))
        #print(str(BirthDay.value, "gbk"))
        print(str(Code.value, "gbk"))
        print(str(Address.value, "gbk"))
        print(str(Agency.value, "gbk"))
        print(str(ExpireStart.value, "gbk"))
        print(str(ExpireEnd.value, "gbk"))
        self.CloseComm();
        return str(Name.value, "gbk"),str(Gender.value, "gbk"),str(Folk.value, "gbk"),str(BirthDay.value, "gbk"),str(Code.value, "gbk"),str(Address.value, "gbk"),str(Agency.value, "gbk"),str(ExpireStart.value, "gbk"),str(ExpireEnd.value, "gbk")

    def getHeadImg(self):
        # 读取图片
        import base64,os
        image_base64 = None
        #img_save_path = os.path.join(os.environ['BASE_PATH'], 'frontend', 'static', 'media', 'work_ticket', 'Photo.jpg')
        img_save_path =self.path+"/photo.jpg"
        if os.path.exists(img_save_path):
            with open(img_save_path, 'rb') as f:
                ls_f = base64.b64encode(f.read())
                image_base64 = str(base64.b64encode(ls_f), encoding='utf-8')
                f.close()
            os.remove(img_save_path)
        return image_base64
