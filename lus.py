from machine import Pin
import utime


luz_led = Pin(15,Pin.OUT)
luz_led1 = Pin(2,Pin.OUT)
luz_led2 = Pin(4,Pin.OUT)
luz_led3 = Pin(16,Pin.OUT)
luz_led4 = Pin(17,Pin.OUT)
luz_led5 = Pin(5,Pin.OUT)
luz_led6 = Pin(18,Pin.OUT)
luz_led7 = Pin(19,Pin.OUT)

def Leds (a,b,c,d,e,f,g,h):
    luz_led.value(a)
    luz_led1.value(b)
    luz_led2.value(c)
    luz_led3.value(d)
    luz_led4.value(e)
    luz_led5.value(f)
    luz_led6.value(g)
    luz_led7.value(h)


while True:
    
    
    Leds(0,0,0,0,0,0,0,0)
    utime.sleep(0.1)
    Leds(1,1,0,0,0,0,0,0)
    utime.sleep(0.1)
    Leds(1,1,1,0,0,0,0,0)
    utime.sleep(0.1)
    Leds(0,1,1,1,0,0,0,0)
    utime.sleep(0.1)
    Leds(0,0,1,1,1,0,0,0)
    utime.sleep(0.1)
    Leds(0,0,0,1,1,1,0,0)
    utime.sleep(0.1)
    Leds(0,0,0,0,1,1,1,0)
    utime.sleep(0.1)
    Leds(0,0,0,0,0,1,1,1)
    utime.sleep(0.1)
    Leds(0,0,0,0,0,0,1,1)
    utime.sleep(0.1)
    Leds(0,0,0,0,0,0,0,1)
    utime.sleep(0.1)
    Leds(0,0,0,0,0,0,0,0)
    
    utime.sleep(0.1)
    Leds(0,0,0,0,0,0,0,0)
    utime.sleep(0.1)
    Leds(0,0,0,0,0,0,0,1)
    utime.sleep(0.1)
    Leds(0,0,0,0,0,0,1,1)
    utime.sleep(0.1)
    Leds(0,0,0,0,0,1,1,1)
    utime.sleep(0.1)
    Leds(0,0,0,0,1,1,1,0)
    utime.sleep(0.1)
    Leds(0,0,0,1,1,1,0,0)
    utime.sleep(0.1)
    Leds(0,0,1,1,1,0,0,0)
    utime.sleep(0.1)
    Leds(0,1,1,1,0,0,0,0)
    utime.sleep(0.1)
    Leds(1,1,1,0,0,0,0,0)
    utime.sleep(0.1)
    Leds(1,1,0,0,0,0,0,0)
    utime.sleep(0.1)
    Leds(1,0,0,0,0,0,0,0)
    utime.sleep(0.1)
    Leds(0,0,0,0,0,0,0,0)
    utime.sleep(0.1)