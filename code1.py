#Write a function that accepts a list of strings from stdin, and sorts it based on length of those strings. The output is the sorted list of strings.

l=[]
print "enter the size of the list:"
N = int(input())
for x in range(N):
	x = raw_input("")
	l.append(x)
	l.sort(key=len)
print l
