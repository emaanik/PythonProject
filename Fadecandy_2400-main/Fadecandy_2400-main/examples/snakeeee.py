import opc
from time import sleep
import random
import colorsys

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

while True:
    for led in range(170):
        leds= [(255,255,255)]*360
        leds[led] = (0,0,255)
        leds[led+1] = (0,0,255)
        leds[led+2] = (0,0,255)
        leds[led+3]= (0,0,255)
        leds[led+4]= (0,0,255)   #if you want to go backwarrds do leds[355- led+4]
        if led== 359:
            led=0
        client. put_pixels(leds)       
        sleep(.1)

while True:           
    for led1 in range (355) :
        leds1= [(255,0,0)]*360
        leds1[355-led1] = (0,0,255)
        leds1[355-led1+1] = (0,0,255)
        leds1[355-led1+2] = (0,0,255)
        leds1[355-led1+3]= (0,0,255)
        leds1[355-led1+4]= (0,0,255)
        if led == 170:
            led = 359
        client. put_pixels(leds1)       
        sleep(.1)
   


    



