total_bill = 0.0
tip = 0.0
bill_before_tip = 0.0
people_number = 1.0
bill_per_person= 0.0

def prompt_user(): 
	global total_bill
	global tip
	global bill_before_tip
	global people_number
	bill_before_tip = float(raw_input('how much is on the bill not including tip?'))
	dine_alone = raw_input('did you dine alone? y/n') 
	if dine_alone == 'no':
			people_number = float(raw_input('how many people were at dinner?'))
	else:
		 people_number = 1.0
	tip_percentage = raw_input('is 18% tip ok?')
	if tip_percentage == 'no':
		tip = float(raw_input('how much would you like to leave for tip?'))
	else:
		tip = .18
	
def calculate_bill():
	global bill_before_tip
	global tip
	global bill_per_person
	global total_bill
	total_bill = bill_before_tip + (tip * bill_before_tip)
	bill_per_person = total_bill/people_number

def display_bill_amounts():
	global bill_before_tip
	global tip
	global bill_per_person
	global total_bill
	print 'the bill before tip is', bill_before_tip
	print 'the tip is', tip
	print 'the bill with tip is', total_bill
	print 'the bill per person is', bill_per_person

def main():
	prompt_user()
	calculate_bill()
	display_bill_amounts()

if __name__ == '__main__':
	main()





	

