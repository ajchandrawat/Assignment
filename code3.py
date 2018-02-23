#Write a factorisation function which accepts an integer (less than 100000) and prints all its factors greater than 1. It should also print whether a number is prime; if so.


def printFactors(n):
	flag = True
	for i in range(2,n):
		if n % i == 0:
			print i
			flag = False
	if flag:
		print "Prime number"
printFactors(int(input()))
