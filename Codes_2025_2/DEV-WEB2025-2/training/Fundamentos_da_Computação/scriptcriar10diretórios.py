import os
import time
a = -1
b = -1
for i in range (101):
    a += 1
    at = str(a)
    os.mkdir("pão" + (at))
    
    
time.sleep(5)

for i in range (101):
    b += 1 
    bt = str(b)
    os.rmdir("pão" + (bt))