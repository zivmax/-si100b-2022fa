from machine  import Pin,PWM
from time import sleep

fq = 5000
LED = PWM(Pin(2), fq)


for i in range(512):
  LED.duty(2*i)
  sleep(0.01)
  
  
for i in range(512):
  LED.duty(1023 - 2*i)
  sleep(0.01)
