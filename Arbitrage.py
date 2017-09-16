#!/usr/bin/python
import math

def percentXInput(oddslist):
	sum = 0

	for i in oddslist:
		percent = (1/i)*100
		sum = sum + percent

	return sum

def percentOutcome(sum):

	profit = (100/sum)*100 

	return profit

def rawProfitPercent(oddslist):
	sum = percentXInput(oddslist)
	percent = percentOutcome(sum)
	raw = percent - 100
	return raw


def maxProfitValuesTwo(odds1,odds2,capital):
	apercent = (1/odds1)*100
	bpercent = (1/odds2)*100

	sum = apercent + bpercent

	abet = (capital*apercent) / sum
	bbet = (capital*bpercent) / sum

	return(abet,bbet)



def maxProfitValuesX(oddslist,capital):
	percentlist = []
	sum = 0

	for i in oddslist:
		percent = (1/i)*100
		percentlist.append(percent)
		sum = sum + percent

	betlist = []

	for i in percentlist:
		bet = (capital*i)/sum
		betlist.append(bet)

	return betlist


def roundUpOneDec(bet1,bet2):
	ceil1 = (math.ceil(bet1))
	ceil2 = (math.ceil(bet2))

	return(ceil1,ceil2)

def roundDownOneDec(bet1,bet2):
	floor1 = (math.floor(bet1))
	floor2 = (math.floor(bet2))

	return(floor1,floor2)

def roundOneDec(bet1,bet2):
	round1 = (round(bet1))
	round2 = (round(bet2))

	return(round1,round2)


def suggestedBets(odds1,odds2,capital):
	
	a = (odds1*100) + (odds2*100)
	b = capital/a
	c = math.floor(b)
	sugodds1 = (100*c*odds2)
	sugodds2 = (100*c*odds1)
	print("Suggested bet for odds1:%f" % sugodds1)
	print("Suggested bet for odds2:%f" % sugodds2)	


def modTenRec(odds1,odds2):
	a = (odds1*100)
	b = (odds2*100)

	if a % 10 == 0 and b % 10 == 0:
		a = a/10
		b = b/10
		return modTenRec(a/100,b/100)
	else:
		return (a,b)

def modXRec(odds1,odds2,mod):
	oddsone = odds1*100
	oddstwo = odds2*100

	mod1 = oddsone % mod
	mod2 = oddstwo % mod

	if odds1 == odds2 and mod1 == 0 :
		return (1,1)
	elif odds1 == odds2:
		return (oddsone,oddstwo)
	elif mod1 == 0 and mod2 == 0:
		return modXRec((oddsone/mod)/100,(oddstwo/mod)/100,mod)
	else:
		return (oddsone,oddstwo)


def modXRec2(oddslist,mod):
	expanded = [100*x for x in oddslist]

	modlist = [x % mod for x in expanded]

	retlist = []

	if all(x == oddslist[0] for x in oddslist) and modlist[0] == 0:
		for i in oddslist:
			retlist.append(1)
		return retlist
	else:
		return null


def suggestedBetsV2(odds1,odds2,capital,mod):

	print("The potential profit on this bet is %f%%" % rawProfitPercent([odds1,odds2]))

	profitlist = maxProfitValuesX([odds1,odds2],capital)

	print("The ideal betting values for maximum profit would be %f and %f" % (profitlist[0], profitlist[1]))

	a = modXRec(odds1,odds2,mod)
	b = a[0] + a[1]
	c = capital/b
	d = c - (c % mod)
	if d == 0:
		print("You do not have sufficient Capital to make clean bets that round to %d and that do not sacrifice your profit margin" % mod)
		return (0,0)
	else:
		sugodds1 = (a[0]*d)
		sugodds2 = (a[1]*d)
		print("Suggested bet for odds1:%f" % sugodds1)
		print("Suggested bet for odds2:%f" % sugodds2)
		return (sugodds1,sugodds2)	

suggestedBetsV2(3.0,1.57,1000,5)

def suggestedBetsX(oddslist,capital,mod):
	print("The potential profit on this bet is %f%%" % rawProfitPercent(oddslist))

	profitlist = maxProfitValuesX(oddslist,capital)

	print("The ideal betting values for maximum profit would be:" + ",".join(map(str,profitlist)))




suggestedBetsX([3.1,3.0,3.2],5000,10)