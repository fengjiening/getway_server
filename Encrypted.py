from util.subprocess import register
appkey="94:C6:91:35:2F:26BFEBFBFF0003067818180144018700000000"
devkey="2020-05-10 00:00:00"
reg = register()
print("加密")
print("[appkey :%s]"%reg.Encrypted(appkey))
print("[devkey :%s]"%reg.Encrypted(devkey))
print("解密")
print("[appkey :%s]"%reg.DesDecrypt(reg.Encrypted(appkey)))
print("[devkey :%s]"%reg.DesDecrypt(reg.Encrypted(devkey)))