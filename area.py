import math 


a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
s=(a+b+c)/2

area=math.squr(s*(s-a)*(s-b)*(s-c))
print(area)