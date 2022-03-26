import datetime
from ntpath import join
import random
import os

def get_payment_id():

    ctime = datetime.datetime.now()
    mtime = str(ctime.time())
    newtime = ''.join(ch for ch in mtime if ch.isalnum())
    digits = [x for x in range(0,10)]
    randNumber =str(random.choices(digits,k=3))
    randNumber = ''.join(x for x in randNumber if x.isalnum())
    my_id = f'{randNumber}-{str(newtime)}'
    return my_id
