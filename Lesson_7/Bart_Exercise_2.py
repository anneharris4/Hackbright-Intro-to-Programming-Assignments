def load_card (ones,fives,tens,twenties):
	return (1*ones) + (5*fives) + (10*tens) + (20 * twenties)

ones = int(raw_input("How many ones?"))
fives = int(raw_input("How many fives?"))
tens = int(raw_input("how many tens?"))
twenties = int(raw_input("How many twenties?"))


print load_card(ones,fives,tens,twenties)

card_value = load_card(ones,fives,tens,twenties)

fare_price=raw_input("where would you like to go?")

DUBLIN_TO_POWELL = 6.15
FRUITVALE_TO_UNION_CITY = 3.80
ORINDA_TO_RICHMOND = 3.35
HAYWARD_TO_CONCORD = 5.20
FREMONT_TO_COLMA = 6.60

def travel_to_destination(fare_price, card_value):
	if card_value >= fare_price:
		return 'Welcome aboard, enjoy your trip!'
	else:
		return 'You need more money!'

print travel_to_destination(fare_price, card_value)
