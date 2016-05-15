

def bacon_choice_1():
	should_bacon = raw_input ("should you eat that bacon? ")
	if should_bacon == 'no':
		print 'of course you should'
	else:
		print 'well obviously'

def bacon_choice_2():
	angels_of_bacon = raw_input("Do you want to feel like angels are frolicking on your tastebuds? ")
	if angels_of_bacon == 'no':
		print 'you have clearly never tasted bacon'
		print 'eat it'
	elif angels_of_bacon == 'yes':
		print 'eat it'
	elif angels_of_bacon == "I'm afraid":
		coward = raw_input("Are you a coward?")
		if coward == 'yes':
			print 'bacon will turn you into a true warrior '
		if coward == 'no':
			print 'then eat it!'
	
if __name__ == '__main__':
	bacon_choice_1()
	bacon_choice_2()


