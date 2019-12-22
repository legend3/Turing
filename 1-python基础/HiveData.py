#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @date:2018/11/15 16:50
# @name:write
# @author:jint
import random
import csv


i=1
sno=1



sdept="BigData"
for i in range(100000000):
  if i%2==0:
    sex="女"
    sname = "marry"
  else:
    sex="男"
    sname = "Jack"
  sage = random.randint(20, 40)
  f=open("data.txt",'a')
  f.write("\n")
  f.write(str(sno)+","+sname+str(i)+","+sex+","+str(sage)+","+sdept)
  sno=sno+1
  print(i)

# if  __name__== '__main__':
#