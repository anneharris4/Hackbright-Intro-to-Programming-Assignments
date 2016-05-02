def load_card (ones,fives,tens,twenties):
	return (1*ones) + (5*fives) + (10*tens) + (20 * twenties)

ones = int(raw_input("How many ones?"))
fives = int(raw_input("How many fives?"))
tens = int(raw_input("how many tens?"))
twenties = int(raw_input("How many twenties?"))


print load_card(ones,fives,tens,twenties)