#Assuming the following cipher: 1=A, 2=B, 3=C,...,26=Z,27=AA, 28=AB, … write a python function which takes two integers m and n (1 < m < n < 676) and prints the character equivalents of each in a new line. For eg. if the input was m=25 and n=29, it will output:
#Y
#Z
#AA
#AB
#AC




def printSeries(m,n):
	for i in range(m-1,n):
		if i>=26:
				print chr(int(i/26)-1 + 65), 
		print chr(i%26 + 65)
m, n = [int(x) for x in raw_input("Enter values of m & n here: ").split()]
printSeries(m,n)
