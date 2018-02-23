def printFactors(n):
	flag = True
	for i in range(2,n):
		if n % i == 0:
			print i
			flag = False
	if flag:
		print "Prime number"
printFactors(int(input()))

