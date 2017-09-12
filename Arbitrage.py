#!/usr/bin/python
import math

def percentXInput(oddslist):
	sum = 0

	for i in oddslist:
		percent = (1/i)*100
		sum = sum + percent
		print(percent)

	print(sum)
	return sum

def percentOutcome(sum):

	profit = (100/sum)*100 

	print(profit)
	return profit

def rawProfitPercent(sum):
	percent = percentOutcome(sum)
	raw = percent - 100
	print(raw)
	return raw


def maxProfitValuesTwo(odds1,odds2,capital):
	apercent = (1/odds1)*100
	bpercent = (1/odds2)*100

	sum = apercent + bpercent

	print(apercent)
	print(bpercent)

	abet = (capital*apercent) / sum
	bbet = (capital*bpercent) / sum

	print(abet)
	print(bbet)



def maxProfitValuesX(oddslist,capital):
	percentlist = []
	sum = 0

	for i in oddslist:
		percent = (1/i)*100
		percentlist.append(percent)
		sum = sum + percent
		print(percent)

	print(sum)
	betlist = []

	for i in percentlist:
		bet = (capital*i)/sum
		betlist.append(bet)
		print(bet)

	return betlist


def roundUpOneDec(bet1,bet2):
	print(math.ceil(bet1))
	print(math.ceil(bet2))

def roundDownOneDec(bet1,bet2):
	print(math.floor(bet1))
	print(math.floor(bet2))

def roundOneDec(bet1,bet2):
	print(round(bet1))
	print(round(bet2))


def suggestedBets(odds1,odds2,capital):
	
	a = (odds1*100) + (odds2*100)
	b = capital/a
	c = math.floor(b)
	print(c)
	sugodds1 = (100*c*odds2)
	sugodds2 = (100*c*odds1)
	print("Suggested bet for odds1:%f" % sugodds1)
	print("Suggested bet for odds2:%f" % sugodds2)	


def modTenRec(odds1,odds2):
	a = (odds1*100)
	b = (odds2*100)
	print(a%10)
	print(b%10)

	if a % 10 == 0 and b % 10 == 0:
		a = a/10
		b = b/10
		print(a)
		print(b)
		return modTenRec(a/100,b/100)
	else:
		print(a)
		print(b)

	return (a,b)

def modXRec(odds1,odds2,mod):
	a = (odds1*100)
	b = (odds2*100)
	print(a%mod)
	print(b%mod)

	if a % mod == 0 and b % mod == 0:
		a = a/mod
		b = b/mod
		print(a)
		print(b)
		return modXRec(a/100,b/100,mod)
	else:
		print(a)
		print(b)

	return (a,b)

def suggestedBetsV2(odds1,odds2,capital,mod):
	a = modXRec(odds1,odds2,mod)
	b = a[0] + a[1]
	print(a[0])
	print(a[1])

	c = capital/b
	print(c)
	d = c - c % mod
	print(d)
	sugodds1 = (a[0]*d)
	sugodds2 = (a[1]*d)
	print("Suggested bet for odds1:%f" % sugodds1)
	print("Suggested bet for odds2:%f" % sugodds2)	



#maxProfitValuesX([3.3,3.0,2.9],1000)

#percentXInput([4.1,4.2,4.0,4.3])

#roundUpOneDec(96.342,71.104)
    
#suggestedBets(2.1,2.0,1000)

#modTenRec(2.1,2.0)
#modTenRec(2.23,2.41)

#modXRec(2.1,2.0,5)
#modXRec(2.1,2.0,10)
#modXRec(2.1,2.0,20)
#modXRec(2.1,2.0,2)
#modXRec(2.1,2.0,4)

suggestedBetsV2(2.0,2.0,2500,5)
