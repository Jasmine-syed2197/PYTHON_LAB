s=input("Enter the sentence  :")
li=s.split()
s=set(li)
d={}
for i in s:
	    d[i]=li.count(i)
print(d)
