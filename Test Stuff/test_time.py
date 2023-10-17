from time import time
import math
import random

r = 10000000
def floorTimeFunction():
    for i in range(r):
        string = f'{random.randint(-100,100):.0f}'

def intTimeFunction():
    for i in range(r):
        int(random.randint(-100,100))

t0 = time()
floorTimeFunction()
t1 = time()
intTimeFunction()
t2 = time()

print('function format takes %f sec' %(t1-t0))
print('function int takes %f sec' %(t2-t1))