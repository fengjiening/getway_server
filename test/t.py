import datetime
def compare_time(time1, time2):

    d1 = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')
    delta = d1 - d2
    print("days is %s"%delta.days)
    if delta.days >= 30:
        return True
    else:
        return False

time1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
time2 = '2020-04-26 00:00:00'
compare_time(time1,time2)