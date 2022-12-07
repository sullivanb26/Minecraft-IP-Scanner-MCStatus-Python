#!/bin/python3
import requests
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
    output.writelines(str(x.content))
    count -= 1
    print(count)
    sleep(.01)
  