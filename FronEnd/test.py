
import random
from math import *
from time import sleep

A = 2; f=3; t=0

with open("example.txt", "w") as fo1:
    pass

while 1:
    x = t
    y = A * sin(2 * pi * f * t)
    # print(y, x)
    data = "{},{}".format(x, y) 

    with open("example.txt", "a") as fo:

        # for xs in range(1000):
        #     data = "{},{}".format(xs+1, random.randint(3, 12)) 
        #     # print(data)
        #     fo.write(data)
        #     fo.write("\n")

        fo.write(data)
        fo.write("\n")
    
    if t >= 10:
        with open("example.txt", "w") as fo1:
            pass    
        t = 0
    
    print(data)
    t+=0.01
    sleep(0.01)




    


