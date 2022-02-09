import opc
from time import sleep
import colorsys

client = opc.Client('localhost:7890')
leds = [(0,0,0)]*360

s = 1.0 #max colour saturation
v = 1.0 # max bright value

for hue in range(360):
    rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v)
    r_float = rgb_fractional[0]
    g_float = rgb_fractional[1]
    b_float = rgb_fractional[2]

    rgb = (r_float*255, g_float*255, b_float*255)
    print(rgb)
    client.put_pixels([rgb]*360)

    sleep(0.03)
    
