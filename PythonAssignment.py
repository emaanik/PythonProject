import random
f= open ('higherorlowergame.txt','r')

print(''.join([line for line in f]))

deck=[]

 for suit in = ['\u2663', '\u2660' , '\u2665', '\u2666']:
    for ranks in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
    deck.append(ranks+suit)
    
