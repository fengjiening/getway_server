
from flask_cors import CORS
from flask import Flask,redirect
from util.subprocess import register
from flask import request,jsonify
from util.jt_logging import JtLogging
from service.card_service import Service
from constants.configuration import Configuration
from constants.result import R
logger =JtLogging.getLogger("card_service")

Re = R.init()
reg = register()
card= Service(logger,Re)
key_data =reg.Encrypted(reg.getCombinNumber())
app = Flask(__name__)
# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求
CORS(app, resources=r'/*')

@app.before_request
def before_request():
    print(request.args)
    flag = True
    if flag:
       if compare_time():
           logger.error("调用次数限制，【service】")
           return jsonify(R.auth())
       else:
           result = []
           if request.path.find("EncodeInit") > 0:
               # (读门锁参数设置，打开端口)
               result = EncodeInit()
           elif request.path.find("MakeGuestCard") > 0:
               # 制客人卡
               result = MakeGuestCard(request.args)
           elif request.path.find("ReadCard") > 0:
               # 读卡
               result = ReadCard(request.args)
           elif request.path.find("ClearCardData") > 0:
               # 清空卡片
               result = ClearCardData(request.args)
           elif request.path.find("EncodeExit") > 0:
               # 关闭发卡机端口
               result = EncodeExit()
           else:
               result = undfind()

           logger.debug("同一返回结果，【%s】"%result)
           return jsonify(result)
    else:
        logger.error("机器码不一致，【service】")
        return jsonify(R.auth())


def undfind():
    return R.error({},"接口未找到")

def EncodeInit():
    logger.info("接口 EncodeInit【调试】")
    return card.EncodeInit()

def MakeGuestCard(a):
    logger.info("接口 MakeGuestCard【调试】")
    rom = a.get("rom")
    room = a.get("room")
    starttime=a.get("starttime")
    endtime=a.get("endtime")
    enOverride = a.get("enOverride")
    try:
        rom = int(rom)
        enOverride = int(enOverride)
        room=int(room)
        starttime=starttime.split(",")
        endtime=endtime.split(",")
    except Exception as e:
        print(e)
        return R.error([],"检查参数")
    if len(starttime) == 5 and len(endtime) == 5 and enOverride and rom and room:
         return card.MakeGuestCard(rom,room,starttime,endtime,enOverride )
    else:
        return R.error([], "检查参数.")

def ReadCard(a):
    logger.info("接口 ReadCard【调试】")
    rom=a.get("rom")
    room = a.get("room")
    starttime=a.get("starttime")
    endtime=a.get("endtime")
    enOverride = a.get("enOverride")

    try:
        rom = int(rom)
        enOverride = int(enOverride)
        room=int(room)
        starttime=starttime.split(",")
        endtime=endtime.split(",")
    except Exception as e:
        print(e)
        return R.error([],"检查参数")
    if (enOverride):
        print(enOverride)
    if len(starttime)==5 and len(endtime)==5 and enOverride and rom and room:
         return card.ReadCard(rom,room,starttime,endtime,enOverride )
    else:
        return R.error([], "检查参数.")

def ClearCardData(a):
    logger.info("接口 ClearCardData【调试】")
    rom = a.get("rom")
    try:
        rom = int(rom)
    except Exception as e:
        print(e)
        return R.error([], "检查参数")

    if rom:
        return card.ClearCardData(rom)
    else:
        return R.error([], "检查参数.")

def EncodeExit():
    logger.info("接口 EncodeExit【调试】")
    return card.EncodeExit()

def checkAuth():
    return key_data==Configuration.CARD_KEY

def set():
    import os
    path ="C:/ProgramData/jy_sCount_data.dat"
    if os.path.exists(path):
        f1=True
        i=0
        with open(path, "r+") as f:
            count = f.read()
            i = int(count) + 1
        f = open(path, mode="w", encoding="utf-8")
        print("接口调用次数【%s】" % count)
        if i==1:
            f1= False
            f.write("0")
        else:
            if Configuration.TIME == str(reg.Encrypted(str(i)),"utf-8"):
                f.write("0")
                f1 = False
            else:
                f.write(str(i))
                f1 = True
        f.close()
    else:
        f = open(path, mode="w", encoding="utf-8")
        f.write("1")
        f.close()
        f1=True

    return f1


def compare_time():
    import datetime
    time1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time2=reg.DesDecrypt(Configuration.CARD_KEY1)
    d1 = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
    delta = d1 - d2
    print("days is %s"%delta.days)
    if delta.days > 0 :
        return True
    else:
        return False

if __name__ == '__main__':
    logger.info("开始启动【接口服务】" )
    message = "config.ini 未找到"
    key = Configuration.CONFIG_FLAG
    if key:
        message = "授权失败，"
        key =checkAuth()

    if key:
         port=int(Configuration.SERVER_PORT)
         app.run(host="0.0.0.0",port=port, debug=False)
    else:
        logger.info("授权失败，")
        import time
        for i in range(10):
            print("%s 服务停止!【%s秒后退出】"%(message,10-i))
            time.sleep(1)



