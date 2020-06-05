import base64
from pyDes import *  #pip install pyDes
class DEncry:
    def __init__(self):
        self.Des_Key = "DESCRYPT"  # Key
        self.Des_IV = "jiayfjn8"  # 自定IV向量
    # 使用DES加base64的形式加密
    def encrypt(self, s):
        k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
        EncryptStr = k.encrypt(s)
        # EncryptStr = binascii.unhexlify(k.encrypt(str))
        return base64.b64encode(EncryptStr).decode()  # 转base64编码返回
    # des解码
    def decrypt(self, s):
        s = base64.b64decode(s)
        k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
        DecryptStr = k.decrypt(s,padmode=PAD_PKCS5)
        return DecryptStr.decode()