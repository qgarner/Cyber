#Quin Garenr
#6-19-2023
#Using Python with Bash

import os


x = os.popen('whoami').read() 
y = os.popen('ip a').read()
z = os.popen('lshw -short').read()
print(x)
print(y)
print(z)