#dice roll
#hi.
import random
import time
clerk = input("set count")
def roll(count):
    a = 0
    while a != count:
        b = random.randrange(1,6)
        print(str(a+1)+"번:"+str(b))
        a = a+1
        time.sleep(0.7)
roll(int(clerk))