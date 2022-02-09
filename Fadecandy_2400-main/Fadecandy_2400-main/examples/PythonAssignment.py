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









client = opc.Client('localhost:7890')
client.put_pixels(led_colour)
client.put_pixels(led_colour)






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


