from collections import namedtuple
from email.utils import localtime
import random
import math
import time
from turtle import title

def timeR():
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    print(time_string)

def clock():
    while True:
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(result)
        time.sleep(1)

clock()



