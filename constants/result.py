class R :

    @classmethod
    def init(cls):
        cls.result = {}
        return cls
    @classmethod
    def success(cls,message=None):
        if not message:
            cls.result["message"] = "success"
        else :
            cls.result["message"]=message
        cls.result["code"] =0
        return  cls.result

    @classmethod
    def dSuccess(cls, data,message=None):
        if not message:
            cls.result["message"] = "success"
        else :
            cls.result["message"]=message
        cls.result["code"] =0
        cls.result["data"]=data

        return  cls.result

    @classmethod
    def error(cls,  data,message=None):
        if not message:
            cls.result["message"] = "error"
        else:
            cls.result["message"] = message
        cls.result["code"] =1
        cls.result["data"] = data
        return cls.result

    @classmethod
    def auth(cls):
        cls.result["code"] = -999
        cls.result["message"] = "授权到期"
        return cls.result