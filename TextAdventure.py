
def Venture():
	print "You approach the fawn, and find that there is a wolf stalking the fawn, the fawn hasn't noticed yet.\nWhat do you do?"
	whate = ('Attack the fawn') + ('\n>Enter "Attack fawn" ')
 	whatf = ('Attack the wolf') + ('\n>Enter "Attack wolf" ')
 	what6answer = '' or 'venture'
 	what7answer = 'Back' or 'back'
 	while(True):
 		user_input = raw_input(whatc + '\n \n Or \n \n' + whatd);
 		if(user_input == what4answer):
 			KeepGoing()
 			break;
 		elif(user_input == what5answer):
 			Deeper()
 			break;


def Admire():
	print 'You admire the fawn...'

def KeepGoing():
	print 'You keep venturing and find the exit out of the forest...'




def Away():
	print "\n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=|Oh look light!|=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-= \nYou head toward the light peeking behind the branches of the somewhat gloomy forest.\nShould I keep going towards this light? \n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=|<><><><><><><>|=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-="
	whatc = ('Keep going...  ') + ('\n>Enter "Venture" ')
 	whatd = ('Go back the other way...  ') + ('\n>Enter "Back" ')
 	what4answer = 'Venture' or 'venture'
 	what5answer = 'Back' or 'back'
 	while(True):
 		user_input = raw_input(whatc + '\n \n Or \n \n' + whatd);
 		if(user_input == what4answer):
 			KeepGoing()
 			break;
 		elif(user_input == what5answer):
 			Deeper()
 			break;




def Deeper():
	print "\n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=|Dry Beginning|=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-= \nYou go deeper into the dark forest, hoping for more adventure ahead.\nYou walk down, stepping deeper into the forest.\nThere is no turning back now...You see a beautiful fawn that seems to be lost\n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=|<><><><><><><>|=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-="
	whata = ('Approach the deer?  ') + ('\n>Enter "Venture" ')
 	whatb = ('Admire the fawn from a distance?  ') + ('\n>Enter "Admire" ')
 	what2answer = 'Venture' or 'venture'
 	what3answer = 'Admire' or 'admire'
 	while(True):
 		user_input = raw_input(whata + '\n \n Or \n \n' + whatb);
 		if(user_input == what2answer):
 			Venture()
 			break;
 		elif(user_input == what3answer):
 			Admire()
 			break;







def GetUp():
	print "\n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=|Second Breath|=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-= \nYou get up and look around, the feel the spirit of the forest as it's breeze sweeps against your face.\n The gravel path leads seems to lead deeper into the forest... The opposite direction of \nthe path appears a faint glow of light behind the branches.\n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=|<><><><><><><>|=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-="
	what0 = ('Do you wish to follow the path deeper into the forest?  ') + ('\n>Enter "Deeper" ')
 	what1 = ('Do you wish to go towards the light peeking behind the branches?  ') + ('\n>Enter "Away" ')
 	what0answer = 'Deeper' or 'deeper'
 	what1answer = 'Away' or 'deeper'
 	while(True):
 		user_input = raw_input(what0 + '\n \n Or \n \n' + what1);
 		if(user_input == what0answer):
 			Deeper()
 			break;
 		elif(user_input == what1answer):
 			Away()
 			break;





def LayFlat():
	print '\n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=|Laziness|=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-= \n You fall asleep on the ground and dream about cookies, for the next 7 hours, you lay motionless. \n \n"You wake up and are greeted by a hungry wolf."\n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=|<><><><>|=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-='




password = "Enter"

print "\n =-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-= \n Hey Everyone and welcome to my very first interactive, Python programmed,\n adventure game.\n =-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-= "
print "     Type Enter to continue     "
user_input = raw_input()
while user_input != password:
	user_input = raw_input()
	if user_input == password:
		print "Welcome to TextAdventure.... \nVery little people have made it this far... \nType anything to continue!"
	else:
		print "You didn't type Enter, what the heck bro?"

print "\n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-=\n \nWelcome to TextAdventure! Pre-Alpha .-.\nI plan on adding a health bar and a battle system, so yeah! xD it'll take a while..\n Controls\n>Type 'I' for inventory \n>Type 'Char' to view your person \n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-= \n \nVery little people have made it this far... \nType anything to continue!"

user_input = raw_input()

print ('=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=|First Breath|=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-=\nYou awaken in the midst of a small path in a huge forest. \nAs you wake up you feel the breeze of life brush upon your face.\n You lay flat on the floor admiring the night stars...\n=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=|<><><><><><>|=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-=')

what = ('Do you wish to get up?  ') + ('\n>Enter "Get up" ')
what2 = ('Do you wish to lay flat on the ground for 2 more hours?  ') + ('\n>Enter "Lay flat" ')
whatanswer = 'Get up' or 'get up'
what2answer = 'Lay flat' or "lay flat"

while(True):
	user_input = raw_input(what + '\n \n Or \n \n' + what2);
	if(user_input == whatanswer):
		GetUp()
		break;
	elif(user_input == what2answer):
		LayFlat()
		break;
	else:
		print "\n =-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-=o=-=-=-=-=-=-=-=-=-=-=-=-=  \nThat isn't an option silly goose... o_O\n Try again...\n \n"



















