
print("Enter 3 numbers \n")
n1=int(input("first number : "))
n2=int(input("second number : "))
n3=int(input("third number : "))


if n1>n3 and n1>n2:
	print(n1," is large")
elif n2>n3:
	print(n2," is large")
else:
	print(n3," is large")
