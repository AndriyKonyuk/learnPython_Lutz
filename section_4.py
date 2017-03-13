import time
import mytimer
import math
l = [2, 4, 9, 16, 25]

# def timeSetFun(sp,fun):
#     start = time.clock()
#     fun(sp)
#     end = time.clock() - start
#     return print(fun.__name__,'==>', end)


def f(l):
    res = []
    for i in l:
        res.append(math.sqrt(i))
    return res

def f2(l):
    res = list(((map(math.sqrt, l))))
    return res

def f3(l):
    res = [math.sqrt(i) for i in l]
    return res

mytimer.timer(f,l)
mytimer.timer(f2,l)
mytimer.timer(f3,l)
import random
print(random.randrange(10))