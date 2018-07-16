import math

print("Welcome to Quadratic Equation Solver...")

a = int(input("Enter your a value :"))
b = int(input("Enter your b value :"))
c = int(input("Enter your c value :"))

abc=b*b-4*a*c
d=math.sqrt(abc*(-1))

x1=(-b+d)/(2*a)
x2=(-b-d)/(2*a)

print('result=',x1,x2)
