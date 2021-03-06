import os, random, time
import opc
import random
import colorsys
import tkinter as tk
import numpy

window = tk.Tk()

def happy():
    led= 0
    while led< 50:
        for led in range (40):
            led_colour = [(0,0,0)]*360
            led_colour[43-led]=(235, 210, 52); #3rd Smile CIRCLE
            led_colour[44-led]=(235, 210, 52);
            led_colour[45-led]=(235, 210, 52);
            led_colour[46-led]=(235, 210, 52);
            led_colour[47-led]=(235, 210, 52);
            led_colour[101-led]=(235, 210, 52);
            led_colour[108-led]=(235, 210, 52);
            led_colour[160-led]=(235, 210, 52);
            led_colour[169-led]=(235, 210, 52);
            led_colour[220-led]=(235, 210, 52);
            led_colour[229-led]=(235, 210, 52);
            led_colour[281-led]=(235, 210, 52);
            led_colour[288-led]=(235, 210, 52);
            led_colour[343-led]=(235, 210, 52);
            led_colour[344-led]=(235, 210, 52);
            led_colour[345-led]=(235, 210, 52);
            led_colour[346-led]=(235, 210, 52);
            led_colour[347-led]=(235, 210, 52);
            led_colour[102-led]=(235, 210, 52); #3rd Smile Shading
            led_colour[104-led]=(235, 210, 52);
            led_colour[105-led]=(235, 210, 52);
            led_colour[107-led]=(235, 210, 52);
            led_colour[161-led]=(235, 210, 52);
            led_colour[162-led]=(235, 210, 52);
            led_colour[163-led]=(235, 210, 52);
            led_colour[164-led]=(235, 210, 52);
            led_colour[165-led]=(235, 210, 52);
            led_colour[166-led]=(235, 210, 52);
            led_colour[167-led]=(235, 210, 52);
            led_colour[168-led]=(235, 210, 52);
            led_colour[221-led]=(235, 210, 52);
            led_colour[223-led]=(235, 210, 52);
            led_colour[224-led]=(235, 210, 52);
            led_colour[225-led]=(235, 210, 52);
            led_colour[226-led]=(235, 210, 52);
            led_colour[228-led]=(235, 210, 52);
            led_colour[282-led]=(235, 210, 52);
            led_colour[287-led]=(235, 210, 52);
            led_colour[222-led]=(232, 37, 37); #3rd Smile MOUTH
            led_colour[227-led]=(232, 37, 37);
            led_colour[283-led]=(232, 37, 37);
            led_colour[284-led]=(232, 37, 37);
            led_colour[285-led]=(232, 37, 37);
            led_colour[286-led]=(232, 37, 37);
            led_colour[103-led]=(52, 217, 235); #3rd Smile EYES
            led_colour[106-led]=(52, 217, 235);
            client.put_pixels(led_colour)
            time.sleep(.1)
        break
client = opc.Client('localhost:7890')

led_colour = [(0,0,0)]*360

def pattern () :
    leds= [(0,0,0)] *360
    led = 0
    
    while True:
        for led in range (0,360,2):
            leds[led]= (random.randint(150, 255), random.randint(0,0), random.randint(150, 255))
            client.put_pixels(leds)
            time.sleep(.1)
            leds[led+1]=(255,0,255)
            time.sleep(.1)
        break
        
def blinking () :
    leds= [(0,0,0)] *360
    
    
    while True:
       for led in range (0,360):
            leds= [(255,0,0)]*360
            client.put_pixels(leds)
            time.sleep(.1)
            leds=[(0,0,255)]*360
            client.put_pixels(leds)
            time.sleep(.1)
       
        
 
        
def rainbow ():
    while True:
        for hue in range(0,360):
            s = 1.0 
            v = 1.0 
           
            leds= [(0,0,0)]*360
            
           
            rgb = colorsys.hsv_to_rgb(hue/180, s , v) 
           
            r_float = rgb[0] 
            g_float = rgb[1]
            b_float = rgb[2]

            rgb = (r_float*255, g_float*255, b_float*255)
            
            leds[hue] = rgb 
            client.put_pixels(leds) 

            time.sleep(0.01)
        break


def snowday ():
    while True:
        for line in range(360):
            leds = [ (0,0,0) ] * 360 # all leds black
           
            for led in range(30):
                leds[line *60 + led * 2] = (255,255,255) 
                

            client.put_pixels(leds)
            time.sleep(0.1)
        break





button= tk.Button(text = '???happy???', width = 10, height = 2, command= happy)
button.pack(padx = 5, pady = 5 )
button= tk.Button(text = '???pattern???', width = 10, height = 2, command= pattern)
button.pack(padx = 5, pady = 5 )
button= tk.Button(text = '???snowday???', width = 10, height = 2, command= snowday)
button.pack(padx = 5, pady = 5 )
button= tk.Button(text = '???rainbow???', width = 10, height = 2, command= rainbow)
button.pack(padx = 5, pady = 5 )
button= tk.Button(text = '???blinking???', width = 10, height = 2, command= blinking)
button.pack(padx = 5, pady = 5 )
window.mainloop()

