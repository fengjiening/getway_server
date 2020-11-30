
from flask_cors import CORS
from flask import Flask,redirect,session
from util.subprocess import register
from flask import request,jsonify
from util.jt_logging import JtLogging
from service.card_service import Service
from constants.configuration import Configuration
from constants.result import R
from service.card_service import  Service

logger =JtLogging.getLogger("card_service")

Re = R.init()
reg = register()
#card= Service(logger,Re)
key_data =reg.Encrypted(reg.getCombinNumber())
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fjn'
# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求
CORS(app, resources=r'/*')
a=Service(logger,Re)

@app.before_request
def before_request():
    print(request.args)
    key  = session.get("keyName")
    if key:
        return None
    else:
        logger.error("【 检验过期时间 】")
        if compare_time():
            logger.error("【 检验时间失败 】")
            return jsonify(R.auth())
        else:
           logger.info("【 检验时间成功 】")
           session["keyName"] =True


@app.route('/index')
def index():
    data={}
    rets =None
    import time
    print("开始")
    while 1:
        r = a.Authenticate()
        print(r)
        if r == 1:
            rets = a.Routon_DecideIDCardType()
            Name,Gender ,Folk,BirthDay,Code ,Address ,Agency ,ExpireStart ,ExpireEnd=a.read(rets)
            data["Name"]=Name
            data["Gender"]=Folk
            data["BirthDay"]=BirthDay
            data["Code"]=Code
            data["Address"]=Address
            data["Agency"]=Agency
            data["ExpireStart"]=ExpireStart
            data["ExpireEnd"]=ExpireEnd
            data["headImg"]=a.getHeadImg()
            break
        time.sleep(2)
    return jsonify(R.dSuccess(data,"success"))

@app.route('/face')
def face():
    return jsonify(R.success("success"))

def undfind():
    return R.error({},"接口未找到")


def checkAuth():
    return key_data==Configuration.APPKEY

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
    time2=reg.DesDecrypt(Configuration.DEVKEY)
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
    message = "授权失败"
    flag=True
    if Configuration.CONFIG_FLAG:
        key = checkAuth()
        if key:
             flag=False
             logger.info("【接口服务】 启动成功" )
             port=int(Configuration.SERVER_PORT)
             app.run(host="0.0.0.0",port=port, debug=False)
        else:
            logger.info("授权失败")
            message = "授权失败"
    else:
        message = "config.ini未找到"
    logger.info("%s 服务停止!"%(message))
    if flag:
        import time
        for i in range(10):

            print("%s 服务停止!【%s秒后退出】"%(message,10-i))
            time.sleep(1)





