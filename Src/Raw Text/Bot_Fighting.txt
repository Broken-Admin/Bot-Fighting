# Must import
import random
from random import randint
# End of imports

bot1HP = 50
bot2HP = 50

while(1==1):

	bot1Attack = randint(1,50)
	bot2Attack = randint(1,50)
	
	if(bot1Attack>bot2Attack):
		bot2HP = bot2HP - randint(1,15)
	else:
		bot1HP = bot1HP - randint(1,15)
		
	if(bot1HP<1):
		print("Bot 2 wins!")
		break
	if(bot2HP<1):
		print("Bot 1 wins!")
		break

# random.randint(a,b)
# a <= Ran <= b
