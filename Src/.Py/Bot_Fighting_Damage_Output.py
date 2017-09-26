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
		ran = randint(1,15)
		bot2HP = bot2HP - ran
		print("Bot 1 does", ran, "damage!")
	else:
		ran = randint(1,15)
		bot1HP = bot1HP - ran
		print("Bot 2 does", ran, "damage!")
	if(bot1HP<1):
		print("Bot 2 wins!")
		break
	if(bot2HP<1):
		print("Bot 1 wins!")
		break

# random.randint(a,b)
# a <= Ran <= b