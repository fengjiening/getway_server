from util.subprocess import register

appkey="40:EC:99:48:33:9DBFEBFBFF000906EA0025_38A1_01B6_6020."
devkey="2020-11-29 00:00:00"
reg = register()
print("加密")
print("[appkey :%s]"%reg.Encrypted(appkey))
print("[devkey :%s]"%reg.Encrypted(devkey))
print("解密")
print("[appkey :%s]"%reg.DesDecrypt(reg.Encrypted(appkey)))
print("[devkey :%s]"%reg.DesDecrypt(reg.Encrypted(devkey)))