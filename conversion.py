#!/usr/bin/python

def fractionToDecimal(fraction):
	strspl = fraction.split("/")

	intlist = []

	for i in strspl:
		intlist.append(int(i))

	decimal = 1 + (intlist[0]/intlist[1])
	print(decimal)

def americanToDecimal(american):
	
	americanNum = int(american)
	decimal = 0

	if americanNum > 0:
		decimal = (americanNum/100) + 1
	else:
		decimal = (100/americanNum) + 1

	print(decimal)		

str = input("Enter your fractional input: ");
fractionToDecimal(str)


str = input("Enter your american input: ");
americanToDecimal(str)











