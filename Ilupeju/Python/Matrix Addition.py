# Program to add two matrices using nested loop
print("LAGOSCODE PROJECT FOR FOLASHADE ADETOMIWA-OGUNLEYE")
print("")
print("")
message1 = "Hello and welcome, this platform helps you to generate and add entries in two matrices"
print(message1)
print("")
print("please ensure to input your entries across rows")
print("")
print("ENTRIES FOR THE MATRIX P")
a = int(input("input your matrix entries"))
b = int(input("input your matrix entries"))
c = int(input("input your matrix entries"))
d = int(input("input your matrix entries"))
e = int(input("input your matrix entries"))
f = int(input("input your matrix entries"))

##Dummy matrix to house the variables for the first matrix
P =  [[a, b, c],
     [d, e, f]]

##Display the first matrix
print(P)

print("")
print("")

print("ENTRIES FOR THE MATRIX Q")
m = int(input("input your matrix entries"))
n = int(input("input your matrix entries"))
o = int(input("input your matrix entries"))
r = int(input("input your matrix entries"))
s = int(input("input your matrix entries"))
t = int(input("input your matrix entries"))

##Dummy matrix to house the variables for the second matrix
Q =  [[m, n, o],
     [r, s, t]]

##Display the second matrix
print(Q)

##Dummy matrix to house the result of the operations performed using entries in the individual matrix
result = [[0,0,0],
         [0,0,0]]
         

##for all entries in the rows
for i in range(len(P)):
     
     ##for all entries in the columns
     for j in range(len(P[0])):
       result[i][j] = P[i][j] + Q[i][j]
       
print("")
print("")

##Return result for every entries in the dummy matrix
for r in result:
   print(r)
