import opc
import random
import colorsys

f= open ('higherorlowergame.txt','r')

print(''.join([line for line in f])) 

ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] #
suits = ['\u2663', '\u2660' , '\u2665', '\u2666']
deck = []

leds = [(255,255,255)]*360 #white leds

#3,4,5,6,62,67, 121, 128, 181,188, 242, 247,303,304,305 list of leds for 1 circle
 


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


    
