class rectangle():
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        return self.width*self.length

l=int(input("Enter length of rectangle 1: "))
w=int(input("Enter width of rectangle 1: "))
obj1=rectangle(l,w)
area1=obj1.area()
l=int(input("Enter length of rectangle 2:"))
w=int(input("Enter width of rectangle 2:"))
obj2=rectangle(l,w)
area2=obj2.area()

print("Area of rectangle 1:",obj1.area())
print("Area of rectangle 2:",obj2.area())

if area1 > area2:
    print("Area of the 1st rectangle is greater")
elif area1==area2:
    print("Area of both the rectangle is equal")
else:
    print("Area of the 2nd rectngle is greater")

print()

