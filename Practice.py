import random


class Character():
	def __init__(self, HP=10, ATK=2, name=""):
		self.HP = HP
		self.ATK = ATK
		self.name = name
	def Travel(self):
		print "You travel, and bump into a line of code."
	def Status(self):
		print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nHere's your health  " + str(self.HP)
		print "How much damage you deal  " + str(self.ATK)
		print "Your name is  " + self.name + '\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
	def Attack():
		pass
	def Help(self):
		print '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nYour actions are... [status, attack, help, travel]\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
		pass





player = Character(HP=15, ATK=2)
enemy = Character(HP=7, ATK=1.5) 




# Status, Travel, Attack, Inventory, Sleep



def main_menu():
	print 'Hello young adventurer.\n'
	player.name = raw_input('Please enter your name   ')
	print '\nWelcome to my game, %s !' % player.name
	while(True):
		print 'type help to view actions\n'
		user_input = raw_input("enter something >  ")
		if user_input == 'travel':
			print '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nWOAH hold on buddy, this is still alpha....\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
			player.Travel()
		elif user_input == 'status':
			player.Status()
		elif user_input == 'attack':
			print '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nYou are very weak and have no weapon... o_o\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
		elif user_input == 'help':
			player.Help()
		else:
			print '%s says "I dont understand you."' % player.name


main_menu()




 	






