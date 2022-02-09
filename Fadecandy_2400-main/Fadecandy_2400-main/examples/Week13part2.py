import opc
from time import sleep
import colorsys

client = opc.Client('localhost:7890')
leds = [(0,0,0)]*360

s = 1.0 #max colour saturation
v = 1.0 # max bright value
start_hue = 50

for i in range(60):
    rgb_fractional = colorsys.hsv_to_rgb(((srart_hue+i)*2)/360,i/60,v)
    r,g,b = rgb_fractional
    leds[i] =(r*255, g*255, b*255)
    client.put_pixels(leds)
    sleep(0.2)
    
