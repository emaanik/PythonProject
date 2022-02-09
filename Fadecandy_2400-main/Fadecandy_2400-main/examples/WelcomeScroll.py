import os, random, time
import opc
import random
import colorsys

#WELCOME SCROLL

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
#1,7,61,67, 121,127,172, 232, 292, 293,234, 175, 236, 297, 298,178,238

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
led_colour[63]=(235, 210, 52);
led_colour[123]=(235, 210, 52);
led_colour[]=(235, 210, 52);






#M

#E


client = opc.Client('localhost:7890')
client.put_pixels(led_colour)
client.put_pixels(led_colour)


