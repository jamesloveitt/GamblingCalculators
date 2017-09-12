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



maxProfitValuesX([3.3,3.0,2.9],1000)

percentXInput([4.1,4.2,4.0,4.3])

roundUpOneDec(96.342,71.104)
    



