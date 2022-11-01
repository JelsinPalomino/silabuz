import random

a = [[random.randint(0, 99),random.randint(0, 99)],[random.randint(0, 99),random.randint(0, 99)]]
b = [[random.randint(0, 99),random.randint(0, 99)],[random.randint(0, 99),random.randint(0, 99)]]

#a= [[2,4],[8,3]]
#b= [[7,5],[3,1]]


print (a)
print (b)
C=[[0,0],[0,0]]

# iterate through rows of X
for i in range(len(a)):
   # iterate through columns of Y
   for j in range(len(b[0])):
       # iterate through rows of Y
       for k in range(len(b)):
           C[i][j] += a[i][k] * b[k][j]

for r in C:
   print(r)