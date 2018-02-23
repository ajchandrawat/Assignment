l=[]
print "enter the size of the list:"
N = int(input())
for x in range(N):
	x = raw_input("")
	l.append(x)
	l.sort(key=len)
print l