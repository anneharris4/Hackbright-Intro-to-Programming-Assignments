shopping_list = ['milk', 'jam', 'bread']

def add_item(new_item):
	# global shopping_list
	new_item = new_item.lower()
	if new_item not in shopping_list:
		shopping_list.append(new_item)
	else:
		print "item already in list. "

def alphabetical_items():
	# global shopping_list
	shopping_list.sort()
	print shopping_list

def remove_item(item):
	item = item.lower() 
	if item not in shopping_list:
		print 'item not on list'
	else:
		 shopping_list.remove(item)
	# del shopping_list[2]
	print shopping_list

def main():
	add_item('cheese')
	alphabetical_items()
	remove_item('cheese')

if __name__ == '__main__':
	main()
