# Python program to display the Fibonacci sequence

def fib(n):
	f=0
	s=1
	t=0
	print(f,end=" ")
	print(s,end=" ")
	for i in range(n-2):
	    t=f+s
	    print(t,end=" ")
	    f=s
	    s=t
n=int(input("Enter n:"))
fib(n)
