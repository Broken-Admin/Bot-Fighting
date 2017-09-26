# Must import
import random
from random import randint
# End of imports

bot1HP = 100
bot2HP = 100

while(1==1):

	bot1Attack = randint(1,50)
	bot2Attack = randint(1,50)
	bot1Crit = randint(1,100)
	bot2Crit = randint(1,100)
	
	if(bot1Attack>bot2Attack):
		ran = randint(1,15)
		crit = randint(5,25)
		if(bot1Crit==100):
			bot2HP -= crit
			print("Bot 1 does a critical, dealing", crit, "damage!")
		else:
			bot2HP -= ran
			print("Bot 1 does", ran, "damage!")
	else:
		ran = randint(1,20)
		ctit = randint(5,25)
		if(bot2Crit==100):
			bot1HP -= crit
			print("Bot 2 does a critical, dealing", crit, "damage!")
		else:
			bot1HP -= ran
			print("Bot 2 does", ran, "damage!")
	if(bot1HP<1):
		print("Bot 2 wins!")
		break
	if(bot2HP<1):
		print("Bot 1 wins!")
		break

# random.randint(a,b)
# a <= Ran <= b