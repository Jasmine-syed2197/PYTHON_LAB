import math

def are(a):
 return math.pi*a*a

def per(a):
 return 2*math.pi*a

a=int(input("\nEnter length"))
#b=int(input("\nEnter breadth"))

print( "area:",are(a))
print(" primeter",per(a))
