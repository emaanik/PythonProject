import os, random, time
import opc
import random
import colorsys

f= open ('higherorlowergame.txt','r')

print(''.join([line for line in f])) 

ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] 
suits = ['\u2663', '\u2660' , '\u2665', '\u2666']
deck = []

led_colour = [(0,0,0)]*360

#WELCOME SCROLL
for led in range(0,100,2)

#W
led_colour[1]=(235, 210, 52);
led_colour[7]=(235, 210, 52);
led_colour[61]=(235, 210, 52);
led_colour[67]=(235, 210, 52);
led_colour[121]=(235, 210, 52);
led_colour[127]=(235, 210, 52);
led_colour[181]=(235, 210, 52);
led_colour[241]=(235, 210, 52);
led_colour[301]=(235, 210, 52);
led_colour[302]=(235, 210, 52);
led_colour[243]=(235, 210, 52);
led_colour[184]=(235, 210, 52);
led_colour[245]=(235, 210, 52);
led_colour[306]=(235, 210, 52);
led_colour[307]=(235, 210, 52);
led_colour[187]=(235, 210, 52);
led_colour[247]=(235, 210, 52);


#E
led_colour[9]=(235, 210, 52);
led_colour[10]=(235, 210, 52);
led_colour[11]=(235, 210, 52);
led_colour[12]=(235, 210, 52);
led_colour[13]=(235, 210, 52);
led_colour[14]=(235, 210, 52);
led_colour[15]=(235, 210, 52);
led_colour[309]=(235, 210, 52);
led_colour[310]=(235, 210, 52);
led_colour[311]=(235, 210, 52);
led_colour[312]=(235, 210, 52);
led_colour[313]=(235, 210, 52);
led_colour[314]=(235, 210, 52);
led_colour[315]=(235, 210, 52);
led_colour[69]=(235, 210, 52);
led_colour[129]=(235, 210, 52);
led_colour[130]=(235, 210, 52);
led_colour[131]=(235, 210, 52);
led_colour[132]=(235, 210, 52);
led_colour[133]=(235, 210, 52);
led_colour[189]=(235, 210, 52);
led_colour[249]=(235, 210, 52);







#L


led_colour[17]=(235, 210, 52);
led_colour[77]=(235, 210, 52);
led_colour[137]=(235, 210, 52);
led_colour[197]=(235, 210, 52);
led_colour[257]=(235, 210, 52);
led_colour[317]=(235, 210, 52);
led_colour[318]=(235, 210, 52);
led_colour[319]=(235, 210, 52);
led_colour[320]=(235, 210, 52);
led_colour[321]=(235, 210, 52);
led_colour[322]=(235, 210, 52);
led_colour[323]=(235, 210, 52);


#C
led_colour[325]=(235, 210, 52);
led_colour[326]=(235, 210, 52);
led_colour[327]=(235, 210, 52);
led_colour[328]=(235, 210, 52);
led_colour[329]=(235, 210, 52);
led_colour[330]=(235, 210, 52);
led_colour[331]=(235, 210, 52);
led_colour[25]=(235, 210, 52);
led_colour[26]=(235, 210, 52);
led_colour[27]=(235, 210, 52);
led_colour[28]=(235, 210, 52);
led_colour[29]=(235, 210, 52);
led_colour[30]=(235, 210, 52);
led_colour[31]=(235, 210, 52);
led_colour[85]=(235, 210, 52);
led_colour[145]=(235, 210, 52);
led_colour[205]=(235, 210, 52);
led_colour[265]=(235, 210, 52);



#O
led_colour[33]=(235, 210, 52);
led_colour[34]=(235, 210, 52);
led_colour[35]=(235, 210, 52);
led_colour[36]=(235, 210, 52);
led_colour[37]=(235, 210, 52);
led_colour[38]=(235, 210, 52);
led_colour[39]=(235, 210, 52);
led_colour[93]=(235, 210, 52);
led_colour[153]=(235, 210, 52);
led_colour[213]=(235, 210, 52);
led_colour[273]=(235, 210, 52);
led_colour[333]=(235, 210, 52);
led_colour[334]=(235, 210, 52);
led_colour[335]=(235, 210, 52);
led_colour[336]=(235, 210, 52);
led_colour[337]=(235, 210, 52);
led_colour[338]=(235, 210, 52);
led_colour[339]=(235, 210, 52);
led_colour[99]=(235, 210, 52);
led_colour[159]=(235, 210, 52);
led_colour[219]=(235, 210, 52);
led_colour[279]=(235, 210, 52);





#M
led_colour[41]=(235, 210, 52)
led_colour[42]=(235, 210, 52)
led_colour[46]=(235, 210, 52)
led_colour[47]=(235, 210, 52)
led_colour[107]=(235, 210, 52)
led_colour[167]=(235, 210, 52)
led_colour[227]=(235, 210, 52)
led_colour[287]=(235, 210, 52)
led_colour[347]=(235, 210, 52)
led_colour[101]=(235, 210, 52)
led_colour[103]=(235, 210, 52)
led_colour[105]=(235, 210, 52)

led_colour[161]=(235, 210, 52)
led_colour[164]=(235, 210, 52)
led_colour[221]=(235, 210, 52)
led_colour[281]=(235, 210, 52)
led_colour[341]=(235, 210, 52)


#E
led_colour[49]=(235, 210, 52)
led_colour[50]=(235, 210, 52)
led_colour[51]=(235, 210, 52)
led_colour[52]=(235, 210, 52)
led_colour[53]=(235, 210, 52)
led_colour[54]=(235, 210, 52)
led_colour[55]=(235, 210, 52)
led_colour[109]=(235, 210, 52)
led_colour[169]=(235, 210, 52)
led_colour[170]=(235, 210, 52)
led_colour[171]=(235, 210, 52)
led_colour[172]=(235, 210, 52)
led_colour[173]=(235, 210, 52)
led_colour[229]=(235, 210, 52)
led_colour[289]=(235, 210, 52)
led_colour[349]=(235, 210, 52)
led_colour[350]=(235, 210, 52)
led_colour[351]=(235, 210, 52)
led_colour[352]=(235, 210, 52)
led_colour[353]=(235, 210, 52)
led_colour[354]=(235, 210, 52)
led_colour[355]=(235, 210, 52)



led_colour[3]=(235, 210, 52); #1st Smile Outline
led_colour[4]=(235, 210, 52);
led_colour[5]=(235, 210, 52);
led_colour[6]=(235, 210, 52);
led_colour[7]=(235, 210, 52);
led_colour[61]=(235, 210, 52);
led_colour[68]=(235, 210, 52);
led_colour[120]=(235, 210, 52);
led_colour[129]=(235, 210, 52);
led_colour[180]=(235, 210, 52);
led_colour[189]=(235, 210, 52);
led_colour[241]=(235, 210, 52);
led_colour[248]=(235, 210, 52);
led_colour[303]=(235, 210, 52);
led_colour[304]=(235, 210, 52);
led_colour[305]=(235, 210, 52);
led_colour[306]=(235, 210, 52);
led_colour[307]=(235, 210, 52);


led_colour[62]=(235, 210, 52); #1st Smile Shading
led_colour[64]=(235, 210, 52);
led_colour[65]=(235, 210, 52);
led_colour[67]=(235, 210, 52);
led_colour[121]=(235, 210, 52);
led_colour[122]=(235, 210, 52);
led_colour[123]=(235, 210, 52);
led_colour[124]=(235, 210, 52);
led_colour[125]=(235, 210, 52);
led_colour[126]=(235, 210, 52);
led_colour[127]=(235, 210, 52);
led_colour[128]=(235, 210, 52);
led_colour[181]=(235, 210, 52);
led_colour[183]=(235, 210, 52);
led_colour[184]=(235, 210, 52);
led_colour[185]=(235, 210, 52);
led_colour[186]=(235, 210, 52);
led_colour[188]=(235, 210, 52);
led_colour[242]=(235, 210, 52);
led_colour[247]=(235, 210, 52);

led_colour[182]=(232, 37, 37); #1st Smile MOUTH
led_colour[187]=(232, 37, 37);
led_colour[243]=(232, 37, 37);
led_colour[244]=(232, 37, 37);
led_colour[245]=(232, 37, 37);
led_colour[246]=(232, 37, 37);
led_colour[63]=(52, 217, 235); # 1st Smile EYES
led_colour[66]=(52, 217, 235);

#SECOND SMILE
led_colour[23]=(235, 210, 52); #2nd Smile CIRCLE
led_colour[24]=(235, 210, 52);
led_colour[25]=(235, 210, 52);
led_colour[26]=(235, 210, 52);
led_colour[27]=(235, 210, 52);
led_colour[81]=(235, 210, 52);
led_colour[88]=(235, 210, 52);
led_colour[140]=(235, 210, 52);
led_colour[149]=(235, 210, 52);
led_colour[200]=(235, 210, 52);
led_colour[209]=(235, 210, 52);
led_colour[261]=(235, 210, 52);
led_colour[268]=(235, 210, 52);
led_colour[323]=(235, 210, 52);
led_colour[324]=(235, 210, 52);
led_colour[325]=(235, 210, 52);
led_colour[326]=(235, 210, 52);
led_colour[327]=(235, 210, 52);

led_colour[82]=(235, 210, 52); #2nd Smile Shading
led_colour[84]=(235, 210, 52);
led_colour[85]=(235, 210, 52);
led_colour[87]=(235, 210, 52);
led_colour[141]=(235, 210, 52);
led_colour[142]=(235, 210, 52);
led_colour[143]=(235, 210, 52);
led_colour[144]=(235, 210, 52);
led_colour[145]=(235, 210, 52);
led_colour[146]=(235, 210, 52);
led_colour[147]=(235, 210, 52);
led_colour[148]=(235, 210, 52);
led_colour[201]=(235, 210, 52);
led_colour[203]=(235, 210, 52);
led_colour[204]=(235, 210, 52);
led_colour[205]=(235, 210, 52);
led_colour[206]=(235, 210, 52);
led_colour[208]=(235, 210, 52);
led_colour[262]=(235, 210, 52);
led_colour[267]=(235, 210, 52);

led_colour[202]=(232, 37, 37); #2nd Smile MOUTH
led_colour[207]=(232, 37, 37);
led_colour[263]=(232, 37, 37);
led_colour[264]=(232, 37, 37);
led_colour[265]=(232, 37, 37);
led_colour[266]=(232, 37, 37);
led_colour[83]=(52, 217, 235); #2nd Smile EYES
led_colour[86]=(52, 217, 235);


#THIRD SMILE
led_colour[43]=(235, 210, 52); #3rd Smile CIRCLE
led_colour[44]=(235, 210, 52);
led_colour[45]=(235, 210, 52);
led_colour[46]=(235, 210, 52);
led_colour[47]=(235, 210, 52);
led_colour[101]=(235, 210, 52);
led_colour[108]=(235, 210, 52);
led_colour[160]=(235, 210, 52);
led_colour[169]=(235, 210, 52);
led_colour[220]=(235, 210, 52);
led_colour[229]=(235, 210, 52);
led_colour[281]=(235, 210, 52);
led_colour[288]=(235, 210, 52);
led_colour[343]=(235, 210, 52);
led_colour[344]=(235, 210, 52);
led_colour[345]=(235, 210, 52);
led_colour[346]=(235, 210, 52);
led_colour[347]=(235, 210, 52);

led_colour[102]=(235, 210, 52); #3rd Smile Shading
led_colour[104]=(235, 210, 52);
led_colour[105]=(235, 210, 52);
led_colour[107]=(235, 210, 52);
led_colour[161]=(235, 210, 52);
led_colour[162]=(235, 210, 52);
led_colour[163]=(235, 210, 52);
led_colour[164]=(235, 210, 52);
led_colour[165]=(235, 210, 52);
led_colour[166]=(235, 210, 52);
led_colour[167]=(235, 210, 52);
led_colour[168]=(235, 210, 52);
led_colour[221]=(235, 210, 52);
led_colour[223]=(235, 210, 52);
led_colour[224]=(235, 210, 52);
led_colour[225]=(235, 210, 52);
led_colour[226]=(235, 210, 52);
led_colour[228]=(235, 210, 52);
led_colour[282]=(235, 210, 52);
led_colour[287]=(235, 210, 52);

led_colour[222]=(232, 37, 37); #3rd Smile MOUTH
led_colour[227]=(232, 37, 37);
led_colour[283]=(232, 37, 37);
led_colour[284]=(232, 37, 37);
led_colour[285]=(232, 37, 37);
led_colour[286]=(232, 37, 37);
led_colour[103]=(52, 217, 235); #3rd Smile EYES
led_colour[106]=(52, 217, 235);




client = opc.Client('localhost:7890')
client.put_pixels(led_colour)
client.put_pixels(led_colour)


#circle_1=[3, 4, 5, 6, 62, 67, 121, 128, 181, 188, 242, 247, 303, 304, 305]  #circle 1
#circle_2= [13, 14, 15, 16, 72, 77, 131, 138, 191, 198, 252, 257, 313, 314,315]  #circle 2
#circle_3= [23,24,25,26,82,87, 141,148,201,208,262, 267, 323,324,325]  #circle 3
#eyes= [63,65, 73,75, 83,85] #eyes
#mouth_1=[183, 186, 244, 245] #mouth1
#mouth_2=[193, 196, 254, 255] #mouth 2
#mouth_3=[203, 206, 264, 265] #mouth3
#235, 210, 52 # circle colour
#52, 217, 235 #eye colour
#232, 37, 37 #mouth colour
#led_colour[circle_1] = (235, 210, 52)



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
    print("\n\nThe current card is", card1[0])
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




    
