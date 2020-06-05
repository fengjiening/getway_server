from util.subprocess import register
reg = register()
f = open('code.txt', 'w') #清空文件内容再写
f.write(reg.getCombinNumber()) #只能写字符串
f.close()