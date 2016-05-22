employee = {}
employee['age'] = 32
employee['height'] = float(raw_input('how tall is Jim?'))
employee['name'] = 'Jim'
print employee
employee['age'] = 33
print employee['name']
# for key in employee:
# 	print key

for i in employee:
	print i

for key, value in employee.items():
	print key, value 

