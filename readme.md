1��˫�� ��genCode.exe�� ���� ��code.txt�� ������
2���޸�config.ini �ļ�
    a�����ݵõ�����Կ �硰8GbmCnAaRgLqeDtR17kkKZYlRhipC+fzGDMe/KnBpr2lkLHbii+lUWjAMc55mIRXDuHtURvO0GTujDtEmKTaGu15aeOpGTRpEvTkN+3xKP8=�����޸� appkey
    b���޸ķ���˿� server_port
    c���޸�Ӳ������
    d���޸�iniPath ע;ilocksoft.ini���ڵ�λ�ã�ilocksoft.ini������ϵͳ��װ·���һ��Ϊ�� C:\Program Files\Smart card lock system\ilocksoft.ini
    f��ֻ���޸����ϲ���
3���޸ĺò�����˫����server.exe������Ӧ��
�����⣬�ȿ�ͬĿ¼�µġ�server.log����־�ļ�

4�����ýӿ�
#����ʵ�����������Ϳ�sdk ���Ľӿ��ĵ�

http://localhost:8881/EncodeInit
http://localhost:8881/MakeGuestCard?room=102&starttime=2020,4,28,12,0&endtime=2020,4,29,12,0&rom=112233&enOverride=1
http://localhost:8881/ReadCard?room=102&starttime=2020,4,28,12,0&endtime=2020,4,29,12,0&rom=112233&enOverride=1
http://localhost:8881/ClearCardData?room=1&starttime=1,2,3,4,5&endtime=1,2,3,4,5&rom=112233&enOverride=2
http://localhost:8881/ReadCard?rom=112233
http://localhost:8881/EncodeExit