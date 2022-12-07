#!/bin/python3
import requests
from rpo import *
from time import sleep
list = open("ips.txt", "r")

#count lines
with open(r"ips.txt", "r") as fp:
    x = len(fp.readlines())
    print('Total lines:', x) # 8;
count = x
content = list.readlines()
output = open("output.json", "w")

while True:
  for i in range(1, count+1):
    x = requests.get('https://api.mcstatus.io/v2/status/java/' + content[i])
    output.writelines(str(x.content) + '\n')
    print(count)
    count -= 1
    sleep(.01)
    if count == 158982:
      break
  break
DelOff("b'{\"online\":false")
print('done deloff')
#f1 = open('output2.json', 'r')
#print(f1.readlines())
DelMax('"max":50', '"online":0')
print('done delmax')
#f2 = open('output.json', 'r')
#print(f2.readlines())