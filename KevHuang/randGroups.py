#!/bin/python
import random

a = []
myFile = open("ml7-student-names")
for i in myFile.readlines():
    
    i= i.strip()
    a.append(i.split(",")[1] +" "+ i.split(",")[0])
myFile.close()

def randomGroup(x):
    for i in range(1000):
        b = random.randrange(len(a)-1)
        c = random.randrange(len(a)-1)
        a[b],a[c] = a[c],a[b]
    tmp=0
    for i in range(len(a)):
        print a[i]
        if tmp % x == 3 :
            print ""
        tmp=tmp+1
randomGroup(4)
