a=int(input("enter num of ele"))
b=int(input("enter num of ele"))

o=(input("enter the operand \n1.+\n2.-\n3*\n4./"))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

if(o=='+'):
    print("ans:",add(a,b))
elif o=='-':
    print("ans:",sub(a,b))
elif(o=='*'):
    print("ans:",mul(a,b))
elif(o=='/'):
    print("ans:",div(a,b))
else:
    print("\nInvalid")
