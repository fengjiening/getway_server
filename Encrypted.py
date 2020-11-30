from util.subprocess import register

appkey="72:04:20:52:41:53BFEBFBFF000906E9W9A6GR7A170396718404664"
devkey="2020-12-29 00:00:00"
reg = register()
print("加密")
print("[appkey :%s]"%reg.Encrypted(appkey))
print("[devkey :%s]"%reg.Encrypted(devkey))
print("解密")
print("[appkey :%s]"%reg.DesDecrypt(reg.Encrypted(appkey)))
print("[devkey :%s]"%reg.DesDecrypt(reg.Encrypted(devkey)))