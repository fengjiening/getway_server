from util.subprocess import register

appkey="B8:E1:20:52:41:53BFEBFBFF000906E9170396718404664"
devkey="2020-11-29 00:00:00"
reg = register()
print("加密")
print("[appkey :%s]"%reg.Encrypted(appkey))
print("[devkey :%s]"%reg.Encrypted(devkey))
print("解密")
print("[appkey :%s]"%reg.DesDecrypt(reg.Encrypted(appkey)))
print("[devkey :%s]"%reg.DesDecrypt(reg.Encrypted(devkey)))