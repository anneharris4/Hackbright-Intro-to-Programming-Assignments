def add (num1, num2):
	return num1+num2
num1 =int(raw_input("what is your first number?"))
num2 =int(raw_input("what is your second number?"))
print add(num1, num2)

def subtract(num1,num2):
	return num1-num2
num1 =int(raw_input("what is your first number?"))
num2 =int(raw_input("what is your second number?"))
print subtract(num1,num2)

def multiply(num1,num2):
	return num1*num2
num1= int(raw_input("what is your first number?"))
num2 =int(raw_input("what is your second number?"))
print multiply(num1,num2)

def divide(num1,num2):
	return num1/num2
num1 =int(raw_input("what is your first number?"))	
num2 =int(raw_input("what is your second number?"))
print divide (num1,num2)

def modulo(num1,num2):
	return num1%num2
num1 =int(raw_input("what is your first number?"))	
num2 =int(raw_input("what is your second number?"))
print modulo (num1,num2)

def power(base,exponent):
	return base**exponent
base=int(raw_input("what is the base value?"))
exponent=int(raw_input("what is the exponent?"))
print power (base,exponent)

def square(num):
	return num**2
num=int(raw_input("what is your value to be squared?"))
print square(num)