# Must import
import random
from random import randint
# End of imports

bot1HP = 100
bot2HP = 100

print(" ")
print("When naming bots please try to avoid spaces.")
print(" ")
name1 = input("What will you name bot 1: ")
print(" ")
name2 = input("What will you name bot 2: ")
print(" ")

while(1==1):

	#Attack Numbers
	ran = randint(1,15)
	crit = randint(12,25)
	
	#Attack Chances
	bot1Attack = randint(1,50)
	bot2Attack = randint(1,50)
	
	#Critical Chance
	bot1Crit = randint(1,100)
	bot2Crit = randint(1,100)
	
	#Healing Chance 1
	bot1Heal = randint(1,50)
	bot2Heal = randint(1,50)
	
	#Healing Amount
	heal = randint(1,15)
	heal2 = randint(15,20)
	
	#Healing Chance 2
	bot1HealPt2 = randint(1,100)
	bot2HealPt2 = randint(1,100)
	
	#Bot 1 Items
	if(bot1Attack>bot2Attack):
		#Bot 1 Healing Checking
		if(bot1Heal==50):
			bot1HP += heal
			print(name1 + "'s self repair activated!")
			print(name1 + " healed", heal, "HP")
			print(" ")
		if(bot1HealPt2==100):
			bot1HP += heal2
			print(name1 + "'s self repair activated!")
			print(name1 + " healed", heal2, "HP")
			print(" ")
		#Bot 1 Critical Checking
		if(bot1Crit==100):
			bot2HP -= crit
			print(name1 + " does a critical, dealing", crit, "damage!")
			if(bot2HP<1):
				print("*" + name2 + " begins to spark* *Later bursting into flames*")
				print(name1 + " wins!")
				break
		else:
			bot2HP -= ran
			print(name1 + " does", ran, "damage!")			
	
	#Bot 2 attack
	else:
		#Bot 2 Healing Checking
		if(bot2Heal==50):
			bot2HP += heal
			print(name2 + "'s self repair activated!")
			print(name2 + " healed", heal, "HP")
			print(" ")
		if(bot2HealPt2==100):
			bot2HP += heal2
			print(name2 + "'s self repair activated!")
			print(name2 + " healed", heal2, "HP")
			print(" ")
		#Bot 2 Critical Checking
		if(bot2Crit==100):
			bot1HP -= crit
			print(name2 + " does a critical, dealing", crit, "damage!")
			if(bot1HP<1):
				print("*" + name1 + " begins to spark* *Later bursting into flames*")
				print(name2, "wins!")
				break
		else:
			bot1HP -= ran
			print(name2 + " does", ran, "damage!")
	
	print(" ")

	#Checking to see who won
	if(bot1HP<1):
		print(name2 + " wins!")
		break
	if(bot2HP<1):
		print(name1 + " wins!")
		break

# random.randint(a,b)
# a <= Ran <= b