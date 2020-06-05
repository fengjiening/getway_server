
#flask & socket-io
#解决问题&方案

1、快速开发HTTP API接口开发

2、增加本地机器唯一码、时间授权，实现接口授权调用

3、提供 python run 运行（不推荐，源码泄露、不安全）

4、提供本地生成exe应用程序、服务启动（推荐）

5、提供websocket 接口实例





#启动步骤、及配置修改

1、双击 “genCode.exe” 生成 “code.txt” 发回来


2、修改config.ini 文件

    a、根据得到的秘钥 如“8GbmCnAaRgLqeDtR17kkKZYlRhipC+fzGDMe/KnBpr2lkLHbii+lUWjAMc55mIRXDuHtURvO0GTujDtEmKTaGu15aeOpGTRpEvTkN+3xKP8=”，修改 appkey 
    b、修改服务端口 server_port
    c、修改硬件串口
    d、修改iniPath 注;ilocksoft.ini所在的位置，ilocksoft.ini在门锁系统安装路径里，一般为” C:\Program Files\Smart card lock system\ilocksoft.ini
    f、只用修改以上参数
    
3、修改好参数，双击“server.exe”启动应用
有问题，先看同目录下的“server.log”日志文件



4、调用接口
#请求实例，参数解释看sdk 给的接口文档

http://localhost:8881/EncodeInit
http://localhost:8881/MakeGuestCard?room=102&starttime=2020,4,28,12,0&endtime=2020,4,29,12,0&rom=112233&enOverride=1
http://localhost:8881/ReadCard?room=102&starttime=2020,4,28,12,0&endtime=2020,4,29,12,0&rom=112233&enOverride=1
http://localhost:8881/ClearCardData?room=1&starttime=1,2,3,4,5&endtime=1,2,3,4,5&rom=112233&enOverride=2
http://localhost:8881/ReadCard?rom=112233
http://localhost:8881/EncodeExit