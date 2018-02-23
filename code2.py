def printSeries(m,n):
	for i in range(m-1,n):
		if i>=26:
				print chr(int(i/26)-1 + 65), 
		print chr(i%26 + 65)
printSeries(25,29)