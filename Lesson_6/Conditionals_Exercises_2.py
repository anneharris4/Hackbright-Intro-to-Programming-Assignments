name1 = raw_input("what is your name?")
name2 = raw_input("what is your partner's name?")
if len(name1) > len(name2):
	print "My name is greater!"
elif len(name1) == len(name2):
	print "Our names are the same length"
else:
	print "Their name is greater!"

date = int(raw_input("What is today's date?"))
if date >= 15:
	print "The month is more than halfway over!"
else:
	print "the month has just begun"

day_of_week = raw_input("what day of the week is it?").lower()
if day_of_week == 'monday':
	print "Ahh it's only Monday!"
elif day_of_week == 'tuesday':
	print "Class today!"
elif day_of_week == 'wednesday':
	print "humpday!"
elif day_of_week == 'thursday':
	print "class part 2"
elif day_of_week == 'friday':
	print "TGIF!"
else:
	print "Happy Weekend!!"

