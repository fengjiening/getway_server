#!/usr/bin/python
# author  fengjiening
# -*- coding: UTF-8 -*-
# from fastapi import FastAPI


from flask import Flask,jsonify,request
from flask_cors import CORS

from util.jt_logging import JtLogging

from flask_socketio import SocketIO
from threading import Lock


app = Flask(__name__)
CORS(app, resources=r'/*')
logger = JtLogging.getLogger("socket")
async_mode = None

# socketio = SocketIO(app, async_mode=async_mode,cors_allowed_origins = "*")
socketio = SocketIO(app, cors_allowed_origins="*")

asrRecorder = None
thread_lock = Lock()

@socketio.on('startRecog')
def startASR(message):
    datas = {"code": "", "message": "success"}
    logger.info("开启语音识别 Recog")
    asrRecorder.asr_wakeup(False)
    datas['code'] = 0
    socketio.emit(data=datas, event="onRecogMessage")


@socketio.on('closeASR')
def closeASR(message):
    datas = {"code": "", "message": "success"}
    logger.info("关闭语音识别 closeASR")
    asrRecorder.asr_sleep()
    datas['code'] = 2
    datas['message'] = "关闭语音识别 closeASR"
    socketio.emit(data=datas, event="onAsrMessage")
    return "success"


if __name__ == '__main__':
    import _thread
    socketio.run(app, host="0.0.0.0", port=5222, debug=False)




