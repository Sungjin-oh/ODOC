#my daily diary
import time

lst = []

def wrote(inc):
    tm = time.localtime(1575142526.500323)
    send = str(tm.tm_mon)+"월"+str(tm.tm_mday)+"일"+str(tm.tm_hour)+"시<>:"+inc
    lst.append(send)
    print(lst)


txt = input("How did you feel today?")
wrote(txt)

