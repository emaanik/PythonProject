import os, random, time
import opc
import random
import colorsys
import numpy
import tkinter as tk


#window = tk.Tk()

#text = tk.Button(text = 'happy',command = happy)
#text.pack()

#window.mainloop()


client = opc.Client('localhost:7890')

led_colour = [(0,0,0)]*360

        

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
def

#leds= [(0,0,0)] *360
#client.put_pixels(led_colour)



#led_colour = [(255,0,0)]*10
#led_colour[5] = (0, 255,0)

#r, g, b = led_colour[7]
#while r > 0:
#    r -=5
#    b +=5
#newValue= (r,g,b)
#led_colour[7] = newValue
#client.put_pixels(led_colour)

def pattern () :
    leds= [(0,0,0)] *360
    led = 0
    s= 1.0
    v = 1.0
    pixels=[]
    for led in range (0,360,2):
        leds[led]= (random.randint(0, 256), random.randint(0, 256), random.randint(0,256))
        leds[led+1]=(255,0,255)
        client.put_pixels(leds)

        time.sleep(.1)


leds= [(0,0,0)] *360

    
##def snowday ():
##    for led in range(360):
##        leds= [(0,0,0)]*360
##        leds[led] = (255,255,255)
##        leds[1-led+61] = (255,255,255)
##        leds[1-led+122] = (255,255,255)
##        leds[1-led+183]= (255,255,255)
##        leds[1-led+244]= (255,255,255)
##        leds[led+4] = (255,255,255)
##        leds[4-led+65] = (255,255,255)
##        leds[4-led+126] = (255,255,255)
##        leds[4-led+187]= (255,255,255)
##        leds[4-led+248]= (255,255,255)
##        leds[led+8] = (255,255,255)
##        leds[8-led+69] = (255,255,255)
##        leds[8-led+130] = (255,255,255)
##        leds[8-led+191]= (255,255,255)
##        leds[8-led+252]= (255,255,255)
##        leds[led+12] = (255,255,255)
##        leds[12-led+73] = (255,255,255)
##        leds[12-led+134] = (255,255,255)
##        leds[12-led+195]= (255,255,255)
##        leds[12-led+256]= (255,255,255)
##        leds[led+16] = (255,255,255)
##        leds[led+77] = (255,255,255)
##        leds[led+138] = (255,255,255)
##        leds[led+199]= (255,255,255)
##        leds[led+260]= (255,255,255)
##        leds[led+20] = (255,255,255)
##        leds[led+81] = (255,255,255)
##        leds[led+142] = (255,255,255)
##        leds[led+203]= (255,255,255)
##        leds[led+264]= (255,255,255)
##        leds[led+24] = (255,255,255) #start
##        leds[led+85] = (255,255,255)
##        leds[led+146] = (255,255,255)
##        leds[led+207]= (255,255,255)
##        leds[led+268]= (255,255,255)#stop
##        leds[led+28] = (255,255,255) #start
##        leds[led+89] = (255,255,255)
##        leds[led+150] = (255,255,255)
##        leds[led+211]= (255,255,255)
##        leds[led+272]= (255,255,255)#
##        leds[led+32] = (255,255,255) #start
##        leds[led+93] = (255,255,255)
##        leds[led+154] = (255,255,255)
##        leds[led+215]= (255,255,255)
##        leds[led+276]= (255,255,255)
##        leds[led+36] = (255,255,255) #start
##        leds[led+97] = (255,255,255)
##        leds[led+158] = (255,255,255)
##        leds[led+219]= (255,255,255)
##        leds[led+280]= (255,255,255)
##        leds[led+40] = (255,255,255) #start
##        leds[led+101] = (255,255,255)
##        leds[led+162] = (255,255,255)
##        leds[led+223]= (255,255,255)
##        leds[led+284]= (255,255,255)
##        leds[led+44] = (255,255,255) #start
##        leds[led+105] = (255,255,255)
##        leds[led+166] = (255,255,255)
##        leds[led+227]= (255,255,255)
##        leds[led+288]= (255,255,255)
##        leds[led+48] = (255,255,255) #start
##        leds[led+109] = (255,255,255)
##        leds[led+170] = (255,255,255)
##        leds[led+231]= (255,255,255)
##        leds[led+292]= (255,255,255)
##        leds[led+52] = (255,255,255) #start
##        leds[led+113] = (255,255,255)
##        leds[led+174] = (255,255,255)
##        leds[led+235]= (255,255,255)
##        leds[led+296]= (255,255,255)
##        leds[led+56] = (255,255,255) #start
##        leds[led+117] = (255,255,255)
##        leds[led+178] = (255,255,255)
##        leds[led+239]= (255,255,255)
##        leds[led+300]= (255,255,255)
##        leds[led+60] = (255,255,255) #start
##        leds[led+121] = (255,255,255)
##        leds[led+182] = (255,255,255)
##        leds[led+243]= (255,255,255)
##        leds[led+304]= (255,255,255)
##        
##
##     
##        for led in range(300, 360):
##            if led== 359:
##                led=0
##        client. put_pixels(leds)       
##        time.sleep(.1)
##
##


s = 1.0 ##maximum colour
v = 1.0 ##maximum brightness


def snowday ():
    while True:
        for line in range(8):
            led_colour = [ (0,0,0) ] * 360
            for i in range(30):
                    led_colour[line * 60 + i * 2] = (255,255,255)

                    # Label all strips always
                    
            client.put_pixels(led_colour)
            time.sleep(0.5)
happy()
pattern()
snowday()
#firework()
#








