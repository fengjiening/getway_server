# 功能说明： 用户运行程序后自动检测认证状态：
#  1. 检测到有注册文件时，注册文件中的注册码和DES+base64加密的注册码比较，若一致，则通过认证，进入主程序。
#  2. 未检测到注册文件或者注册文件中的注册码与DES+base64加密的注册码不一致,则提醒用户输入注册码或重新获取注册码。
#     重新获取注册码会将程序运行后显示的机器码 161k8Z  发送给指定管理员，管理员经过编码生成注册码给回用户，同时生成注册文件。
import wmi
import json
# import win32com

import base64
from util.DEncry_base import DEncry
from pyDes import *


class register:
    def __init__(self):
        self.Des_Key = "DESCRYPT"  # Key
        self.Des_IV = "\x15\1\x2a\3\1\x23\2\0"  # 自定IV向量
        self.DEncry=DEncry()
    ############ 1. 获取硬件信息,输出 macode
    #   1.CPU序列号（ID） 2.本地连接 无线局域网 以太网的MAC 3.硬盘序列号（唯一） 4.主板序列号（唯一）

    global s
    s = wmi.WMI()

    # cpu 序列号
    def get_CPU_info(self):
        cpu = []
        cp = s.Win32_Processor()
        for u in cp:
            cpu.append(
                {
                    "Name": u.Name,
                    "Serial Number": u.ProcessorId,
                    "CoreNum": u.NumberOfCores
                }
            )
        #   print(":::CPU info:", json.dumps(cpu))
        return cpu

    # 硬盘序列号
    def get_disk_info(self):
        disk = []
        for pd in s.Win32_DiskDrive():
            disk.append(
                {
                    "Serial": s.Win32_PhysicalMedia()[0].SerialNumber.lstrip().rstrip(),  # 获取硬盘序列号，调用另外一个win32 API
                    "ID": pd.deviceid,
                    "Caption": pd.Caption,
                    "size": str(int(float(pd.Size) / 1024 / 1024 / 1024)) + "G"
                }
            )
        #   print(":::Disk info:", json.dumps(disk))
        return disk

    # mac 地址（包括虚拟机的）
    def get_network_info(self):
        network = []
        for nw in s.Win32_NetworkAdapterConfiguration():  # IPEnabled=0
            if nw.MACAddress != None:
                network.append(
                    {
                        "MAC": nw.MACAddress,  # 无线局域网适配器 WLAN 物理地址
                        "ip": nw.IPAddress
                    }
                )
        #    print(":::Network info:", json.dumps(network))
        return network

    # 主板序列号
    def get_mainboard_info(self):
        mainboard = []
        for board_id in s.Win32_BaseBoard():
            mainboard.append(board_id.SerialNumber.strip().strip('.'))
        return mainboard

        #  由于机器码太长，故选取机器码字符串部分字符

    #  E0:DB:55:B5:9C:16BFEBFBFF00040651W3P0VKEL6W8T1Z1.CN762063BN00A8
    #  1 61 k 8Z
    #     machinecode_str = ""
    #     machinecode_str = machinecode_str+a[0]['MAC']+b[0]['Serial Number']+c[0]['Serial']+d[0]
    def getCombinNumber(self):
        a = self.get_network_info()
        b = self.get_CPU_info()
        c = self.get_disk_info()
        d = self.get_mainboard_info()
        return a[0]['MAC'] + b[0]['Serial Number'] + c[0]['Serial'] + d[0]



    ############ 2. 注册登录

    # DES+base64加密
    def Encrypted(self, tr):
        return self.DEncry.encrypt(tr)

    # #des+base64解码
    def DesDecrypt(self,tr):
        return self.DEncry.decrypt(tr)

    # 获取注册码，验证成功后生成注册文件
    def regist(self):
        key = input('please input your register code: ')
        # 由于输入类似“12”这种不符合base64规则的字符串会引起异常，所以需要增加输入判断
        if key:
            ontent = self.getCombinNumber()
            tent = bytes(ontent, encoding='utf-8')
            content = self.Encrypted(tent)
            ###            print('content :',content)
            ###            print(type(content))
            key_decrypted = bytes(key, encoding='utf-8')
            if content != 0 and key_decrypted != 0:
                if content != key_decrypted:
                    print("wrong register code, please check and input your register code again:")
                    self.regist()
                elif content == key_decrypted:
                    print("register succeed.")
                    # 读写文件要加判断
                    with open('register.txt', 'w') as f:
                        f.write(key)
                        f.close()
                    return True
                else:
                    return False
            else:
                return False
        else:
            self.regist()
            return False

    # 打开程序先调用注册文件，比较注册文件中注册码与此时获取的硬件信息编码后是否一致
    def checkAuthored(self):
        ontent = self.getCombinNumber()
        print()
        tent = bytes(ontent, encoding='utf-8')
        content = self.Encrypted(tent)
        # 读写文件要加判断
        try:
            f = open('register.txt', 'r')
            if f:
                key = f.read()
                if key:
                    key_decrypted = bytes(key, encoding='utf-8')  # 注册文件中注册码
                    ###              print('key_decrypted:',key_decrypted)
                    ###              print('content:',content)
                    if key_decrypted:
                        if key_decrypted == content:
                            print("register succeed.")
                            ##      checkAuthoredResult = 1  # 注册文件与机器码一致
                        else:
                            ##        checkAuthoredResult = -1 # 注册文件与机器码不一致
                            print('未找到注册文件，', '请重新输入注册码，', '或发送', ontent, '至17695797270', '重新获取注册码')
                            self.regist()
                    else:
                        ##       checkAuthoredResult = -2     # 注册文件的注册码不能被解析
                        self.regist()
                        print('未找到注册文件，', '请重新输入注册码，', '或发送', ontent, '至17695797270', '重新获取注册码')
                else:
                    ##         checkAuthoredResult = -3         # 注册文件中不能被读取
                    self.regist()
                    print('未找到注册文件，', '请重新输入注册码，', '或发送', ontent, '至17695797270', '重新获取注册码')
            else:
                self.regist()
        except:
            print('请发送', ontent, '至17695797270', '获取注册码')
            ##  checkAuthoredResult = 0                      # 未找到注册文件，请重新输入注册码登录
            self.regist()
    ##    print(checkAuthoredResult) 
    ##   return checkAuthoredResult


#reg = register()
#    reg.regist()
#reg.checkAuthored()
#print(str(reg.Encrypted(reg.getCombinNumber()),"utf-8"))