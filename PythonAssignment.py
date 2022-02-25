import os, random, time
import opc
import random
import colorsys

client = opc.Client('localhost:7890')

f= open ('higherorlowergame.txt','r')

print(''.join([line for line in f])) 

ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] 
suits = ['\u2663', '\u2660' , '\u2665', '\u2666']
deck = []

led_colour = [(0,0,0)]*360

#Row1 = [1,7,9, 10, 11, 12, 13, 14, 15, 17, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 41, 42, 46, 47, 49, 50, 51, 52, 53, 54, 55]
#Row2 = [61, 67, 69, 77, 
#Row3 =
#Row4
#
#Row5
#Row6
#
#Led 59 is the last first row led. 0-59 row 1
#60-119 is row 2
#120-179 is row 3
#180 to 239 is row 4
#240 to row 299 is row 5
#300 to 359 is row 6

#WELCOME SCROLL
led= 0
while led< 60:
    for led in range (52):
       led_colour = [(0,0,0)]*360
       led_colour[1-led]=(235, 210, 52);
       led_colour[7-led]=(235, 210, 52);

       led_colour[61-led]=(235, 210, 52);
       led_colour[67-led]=(235, 210, 52);
       led_colour[121-led]=(235, 210, 52);
       led_colour[127-led]=(235, 210, 52);
       led_colour[181-led]=(235, 210, 52);
       led_colour[241-led]=(235, 210, 52);
       led_colour[301-led]=(235, 210, 52);
       led_colour[302-led]=(235, 210, 52);
       led_colour[243-led]=(235, 210, 52);
       led_colour[184-led]=(235, 210, 52);
       led_colour[245-led]=(235, 210, 52);
       led_colour[306-led]=(235, 210, 52);
       led_colour[307-led]=(235, 210, 52);
       led_colour[187-led]=(235, 210, 52);
       led_colour[247-led]=(235, 210, 52)
       client.put_pixels(led_colour)
       time.sleep(.1)
    break




    #E
led= 0
while led< 67:
    for led in range (59):
       led_colour = [(0,0,0)]*360
       led_colour[9-led]=(235, 210, 52);
       led_colour[10-led]=(235, 210, 52);
       led_colour[11-led]=(235, 210, 52);
       led_colour[12-led]=(235, 210, 52);
       led_colour[13-led]=(235, 210, 52);
       led_colour[14-led]=(235, 210, 52);
       led_colour[15-led]=(235, 210, 52);
       led_colour[309-led]=(235, 210, 52);
       led_colour[309-led+1]=(235, 210, 52);
       led_colour[309-led+2]=(235, 210, 52);
       led_colour[309-led+3]=(235, 210, 52);
       led_colour[309-led+4]=(235, 210, 52);
       led_colour[309-led+5]=(235, 210, 52);
       led_colour[309-led+6]=(235, 210, 52);
       led_colour[69-led]=(235, 210, 52);
       led_colour[129-led]=(235, 210, 52);
       led_colour[130-led]=(235, 210, 52);
       led_colour[131-led]=(235, 210, 52);
       led_colour[132-led]=(235, 210, 52);
       led_colour[133-led]=(235, 210, 52);
       led_colour[189-led]=(235, 210, 52);
       led_colour[249-led]=(235, 210, 52);
       client.put_pixels(led_colour)
       time.sleep(.1)
    break




#L
led= 0
while led< 60:
    for led in range (52):
        led_colour = [(0,0,0)]*360
        led_colour[17-led]=(235, 210, 52);
        led_colour[77-led]=(235, 210, 52);
        led_colour[137-led]=(235, 210, 52);
        led_colour[197-led]=(235, 210, 52);
        led_colour[257-led]=(235, 210, 52);
        led_colour[317-led]=(235, 210, 52);
        led_colour[318-led]=(235, 210, 52);
        led_colour[319-led]=(235, 210, 52);
        led_colour[320-led]=(235, 210, 52);
        led_colour[321-led]=(235, 210, 52);
        led_colour[322-led]=(235, 210, 52);
        led_colour[323-led]=(235, 210, 52);
        client.put_pixels(led_colour)
        time.sleep(.1)
    break


    #C
led= 0
while led< 60:
    for led in range (52):
        led_colour = [(0,0,0)]*360
        led_colour[325-led]=(235, 210, 52);
        led_colour[326-led]=(235, 210, 52);
        led_colour[327-led]=(235, 210, 52);
        led_colour[328-led]=(235, 210, 52);
        led_colour[329-led]=(235, 210, 52);
        led_colour[330-led]=(235, 210, 52);
        led_colour[331-led]=(235, 210, 52);
        led_colour[25-led]=(235, 210, 52);
        led_colour[26-led]=(235, 210, 52);
        led_colour[27-led]=(235, 210, 52);
        led_colour[28-led]=(235, 210, 52);
        led_colour[29-led]=(235, 210, 52);
        led_colour[30-led]=(235, 210, 52);
        led_colour[31-led]=(235, 210, 52);
        led_colour[85-led]=(235, 210, 52);
        led_colour[145-led]=(235, 210, 52);
        led_colour[205-led]=(235, 210, 52);
        led_colour[265-led]=(235, 210, 52);
        client.put_pixels(led_colour)
        time.sleep(.1)
    break




    #O
led= 0
while led< 60:
    for led in range (52):
        led_colour = [(0,0,0)]*360
        led_colour[33-led]=(235, 210, 52);
        led_colour[34-led]=(235, 210, 52);
        led_colour[35-led]=(235, 210, 52);
        led_colour[36-led]=(235, 210, 52);
        led_colour[37-led]=(235, 210, 52);
        led_colour[38-led]=(235, 210, 52);
        led_colour[39-led]=(235, 210, 52);
        led_colour[93-led]=(235, 210, 52);
        led_colour[153-led]=(235, 210, 52);
        led_colour[213-led]=(235, 210, 52);
        led_colour[273-led]=(235, 210, 52);
        led_colour[333-led]=(235, 210, 52);
        led_colour[334-led]=(235, 210, 52);
        led_colour[335-led]=(235, 210, 52);
        led_colour[336-led]=(235, 210, 52);
        led_colour[337-led]=(235, 210, 52);
        led_colour[338-led]=(235, 210, 52);
        led_colour[339-led]=(235, 210, 52);
        led_colour[99-led]=(235, 210, 52);
        led_colour[159-led]=(235, 210, 52);
        led_colour[219-led]=(235, 210, 52);
        led_colour[279-led]=(235, 210, 52);
        client.put_pixels(led_colour)
        time.sleep(.1)
    break





    #M
led= 0
while led< 60:
    for led in range (52):
        led_colour = [(0,0,0)]*360
        led_colour[41-led]=(235, 210, 52)
        led_colour[42-led]=(235, 210, 52)
        led_colour[46-led]=(235, 210, 52)
        led_colour[47-led]=(235, 210, 52)
        led_colour[107-led]=(235, 210, 52)
        led_colour[167-led]=(235, 210, 52)
        led_colour[227-led]=(235, 210, 52)
        led_colour[287-led]=(235, 210, 52)
        led_colour[347-led]=(235, 210, 52)
        led_colour[101-led]=(235, 210, 52)
        led_colour[103-led]=(235, 210, 52)
        led_colour[105-led]=(235, 210, 52)
        led_colour[161-led]=(235, 210, 52)
        led_colour[164-led]=(235, 210, 52)
        led_colour[221-led]=(235, 210, 52)
        led_colour[281-led]=(235, 210, 52)
        led_colour[341-led]=(235, 210, 52)
        client.put_pixels(led_colour)
        time.sleep(.1)
    break


    #E
led= 0
while led< 60:
    for led in range (52):
        led_colour = [(0,0,0)]*360
        led_colour[49-led]=(235, 210, 52)
        led_colour[50-led]=(235, 210, 52)
        led_colour[51-led]=(235, 210, 52)
        led_colour[52-led]=(235, 210, 52)
        led_colour[53-led]=(235, 210, 52)
        led_colour[54-led]=(235, 210, 52)
        led_colour[55-led]=(235, 210, 52)
        led_colour[109-led]=(235, 210, 52)
        led_colour[169-led]=(235, 210, 52)
        led_colour[170-led]=(235, 210, 52)
        led_colour[171-led]=(235, 210, 52)
        led_colour[172-led]=(235, 210, 52)
        led_colour[173-led]=(235, 210, 52)
        led_colour[229-led]=(235, 210, 52)
        led_colour[289-led]=(235, 210, 52)
        led_colour[349-led]=(235, 210, 52)
        led_colour[350-led]=(235, 210, 52)
        led_colour[351-led]=(235, 210, 52)
        led_colour[352-led]=(235, 210, 52)
        led_colour[353-led]=(235, 210, 52)
        led_colour[354-led]=(235, 210, 52)
        led_colour[355-led]=(235, 210, 52)
        client.put_pixels(led_colour)
        time.sleep(.1)
    break

led_colour = [(0,0,0)]*360
client.put_pixels(led_colour)

#camoflagesnake

#diagonal swipe with hsv

#s= 1.0
#v = 1.0

#for hue in range(360):
 #   rgb_fractional = colorsys.hsv_to_rgb(hue/360, s,v)
 #   print(rgb_fractional)
 #   r_float = rgb_fractional[0]
  #  g_float = rgb_ fractional[1]
   # b_float = rgb_ fractional[2]
#Diagonalrow = [0, 61, 122, 183, 244, 305]

#led_colour[Diagonalrow + led] = (76, 36, 209)





#led_colour[3]=(235, 210, 52); #1st Smile Outline
#led_colour[4]=(235, 210, 52);
#led_colour[5]=(235, 210, 52);
#led_colour[6]=(235, 210, 52);
#led_colour[7]=(235, 210, 52);
#led_colour[61]=(235, 210, 52);
#led_colour[68]=(235, 210, 52);
##led_colour[120]=(235, 210, 52);
#led_colour[129]=(235, 210, 52);
#led_colour[180]=(235, 210, 52);
#led_colour[189]=(235, 210, 52);
#led_colour[241]=(235, 210, 52);
#led_colour[248]=(235, 210, 52);
#led_colour[303]=(235, 210, 52);
#led_colour[304]=(235, 210, 52);
#led_colour[305]=(235, 210, 52);
#led_colour[306]=(235, 210, 52);
#led_colour[307]=(235, 210, 52);


#led_colour[62]=(235, 210, 52); #1st Smile Shading
#led_colour[64]=(235, 210, 52);
#led_colour[65]=(235, 210, 52);
#led_colour[67]=(235, 210, 52);
#led_colour[121]=(235, 210, 52);
#led_colour[122]=(235, 210, 52);
#led_colour[123]=(235, 210, 52);
#led_colour[124]=(235, 210, 52);
#led_colour[125]=(235, 210, 52);
#led_colour[126]=(235, 210, 52);
#led_colour[127]=(235, 210, 52);
#led_colour[128]=(235, 210, 52);
#led_colour[181]=(235, 210, 52);
#led_colour[183]=(235, 210, 52);
#led_colour[184]=(235, 210, 52);
#led_colour[185]=(235, 210, 52);
#led_colour[186]=(235, 210, 52);
#led_colour[188]=(235, 210, 52);
#led_colour[242]=(235, 210, 52);
#led_colour[247]=(235, 210, 52);

#led_colour[182]=(232, 37, 37); #1st Smile MOUTH
#led_colour[187]=(232, 37, 37);
#led_colour[243]=(232, 37, 37);
#led_colour[244]=(232, 37, 37);
#led_colour[245]=(232, 37, 37);
#led_colour[246]=(232, 37, 37);
#led_colour[63]=(52, 217, 235); # 1st Smile EYES
#led_colour[66]=(52, 217, 235);

#SECOND SMILE
#led_colour[23]=(235, 210, 52); #2nd Smile CIRCLE
#led_colour[24]=(235, 210, 52);
#led_colour[25]=(235, 210, 52);
#led_colour[26]=(235, 210, 52);
#led_colour[27]=(235, 210, 52);
#led_colour[81]=(235, 210, 52);
#led_colour[88]=(235, 210, 52);
#led_colour[140]=(235, 210, 52);
#led_colour[149]=(235, 210, 52);
#led_colour[200]=(235, 210, 52);
#led_colour[209]=(235, 210, 52);
#led_colour[261]=(235, 210, 52);
#led_colour[268]=(235, 210, 52);
#led_colour[323]=(235, 210, 52);
#led_colour[324]=(235, 210, 52);
#led_colour[325]=(235, 210, 52);
#led_colour[326]=(235, 210, 52);
#led_colour[327]=(235, 210, 52);

#led_colour[82]=(235, 210, 52); #2nd Smile Shading
#led_colour[84]=(235, 210, 52);
#led_colour[85]=(235, 210, 52);
#led_colour[87]=(235, 210, 52);
#led_colour[141]=(235, 210, 52);
#led_colour[142]=(235, 210, 52);
#led_colour[143]=(235, 210, 52);
#led_colour[144]=(235, 210, 52);
#led_colour[145]=(235, 210, 52);
#led_colour[146]=(235, 210, 52);
#led_colour[147]=(235, 210, 52);
#led_colour[148]=(235, 210, 52);
#led_colour[201]=(235, 210, 52);
#led_colour[203]=(235, 210, 52);
#led_colour[204]=(235, 210, 52);
#led_colour[205]=(235, 210, 52);
#led_colour[206]=(235, 210, 52);
#led_colour[208]=(235, 210, 52);
#led_colour[262]=(235, 210, 52);
#led_colour[267]=(235, 210, 52);

#led_colour[202]=(232, 37, 37); #2nd Smile MOUTH
#led_colour[207]=(232, 37, 37);
#led_colour[263]=(232, 37, 37);
#led_colour[264]=(232, 37, 37);
#led_colour[265]=(232, 37, 37);
#led_colour[266]=(232, 37, 37);
#led_colour[83]=(52, 217, 235); #2nd Smile EYES
#led_colour[86]=(52, 217, 235);


#THIRD SMILE
#led_colour[43]=(235, 210, 52); #3rd Smile CIRCLE
#led_colour[44]=(235, 210, 52);
#led_colour[45]=(235, 210, 52);
#led_colour[46]=(235, 210, 52);
#led_colour[47]=(235, 210, 52);
#led_colour[101]=(235, 210, 52);
#led_colour[108]=(235, 210, 52);
#led_colour[160]=(235, 210, 52);
#led_colour[169]=(235, 210, 52);
#led_colour[220]=(235, 210, 52);
#led_colour[229]=(235, 210, 52);
#led_colour[281]=(235, 210, 52);
#led_colour[288]=(235, 210, 52);
#led_colour[343]=(235, 210, 52);
#led_colour[344]=(235, 210, 52);
#led_colour[345]=(235, 210, 52);
#led_colour[346]=(235, 210, 52);
#led_colour[347]=(235, 210, 52);

#led_colour[102]=(235, 210, 52); #3rd Smile Shading
#led_colour[104]=(235, 210, 52);
#led_colour[105]=(235, 210, 52);
#led_colour[107]=(235, 210, 52);
#led_colour[161]=(235, 210, 52);
#led_colour[162]=(235, 210, 52);
#led_colour[163]=(235, 210, 52);
#led_colour[164]=(235, 210, 52);
#led_colour[165]=(235, 210, 52);
#led_colour[166]=(235, 210, 52);
#led_colour[167]=(235, 210, 52);
#led_colour[168]=(235, 210, 52);
#led_colour[221]=(235, 210, 52);
#led_colour[223]=(235, 210, 52);
#led_colour[224]=(235, 210, 52);
#led_colour[225]=(235, 210, 52);
#led_colour[226]=(235, 210, 52);
#led_colour[228]=(235, 210, 52);
#led_colour[282]=(235, 210, 52);
#led_colour[287]=(235, 210, 52);

#led_colour[222]=(232, 37, 37); #3rd Smile MOUTH
#led_colour[227]=(232, 37, 37);
#led_colour[283]=(232, 37, 37);
#led_colour[284]=(232, 37, 37);
#led_colour[285]=(232, 37, 37);
#led_colour[286]=(232, 37, 37);
#led_colour[103]=(52, 217, 235); #3rd Smile EYES
#led_colour[106]=(52, 217, 235);





#client.put_pixels(led_colour)
#client.put_pixels(led_colour)


value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + suit, value])#combines rank and suit
    value = value + 1

random.shuffle(deck)
no_of_lives = 3
card1 = deck.pop(0)

while True:
    
    print("Your number of lives is", no_of_lives)
    print("The current card is", card1[0])
    while True:
        choice = input("higher or lower?")
        if len(choice) > 0:
            if choice[0].lower() in ["h","l"]:
                break
        

    card2 = deck.pop(0)
    print("The next card picked is", card2[0])
    time.sleep(1)

    if choice[0].lower() == "h" and card2[1] > card1[1]:
        print("Correct!")
        no_of_lives +=0
        time.sleep(1)
    if choice[0].lower() == "h" and card2[1] < card1[1]:
        print("Wrong!")
        time.sleep(1)
        no_of_lives -=1
        
    if choice[0].lower() == "l" and card2[1] < card1[1]:
        print("Correct!")
        no_of_lives +=0
        time.sleep(1)
    if choice[0].lower() == "l" and card2[1] > card1[1]:
        print("Wrong!")
        time.sleep(1)
        no_of_lives -=1

    if no_of_lives <= 0:
        print("you lose!")
    else:
        print("draw!")

    card1 = card2


print("Game over!")

time.sleep(4)











    
