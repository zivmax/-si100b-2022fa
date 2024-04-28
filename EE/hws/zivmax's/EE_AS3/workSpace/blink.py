from machine import Pin

import time

p2 = Pin(2, Pin.OUT)

for i in range(100):
  
  for j in range(25):
    p2.value(1)
    time.sleep(0.02)
    
    p2.value(0)
    time.sleep(0.02)
    
    j += 1

  for k in range(5):
    p2.value(1)
    time.sleep(0.1)
    
    p2.value(0)
    time.sleep(0.1)
    
    k += 1
 
p2.value(0) 
 
  
  

