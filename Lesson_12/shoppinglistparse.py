shop1 = "item : apples, quantity : 4, price : 1.50\n"
shop2 = shop1.split(',')
quantity_list = shop2[1].split(":")[1]
price_list=shop2[2].split(':')[1]

quantity_list = float(quantity_list)
price_list =float(price_list)

def calculate_bill (quantity_list,price_list):
	return quantity_list * price_list

print calculate_bill (quantity_list,price_list)
