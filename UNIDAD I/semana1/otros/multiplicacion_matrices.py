import random

matrix_1 = [[random.randint(0, 99),random.randint(0, 99)],[random.randint(0, 99),random.randint(0, 99)]]
matrix_2 = [[random.randint(0, 99),random.randint(0, 99)],[random.randint(0, 99),random.randint(0, 99)]]

print (a)
print (b)
matrix_sum=[[0,0],[0,0]]

# iterate through rows of X
for i in range(len(matrix_1)):
   # iterate through columns of Y
   for j in range(len(matrix_2[0])):
       # iterate through rows of Y
       for k in range(len(matrix_2)):
           matrix_sum[i][j] += matrix_1[i][k] * matrix_2[k][j]

for r in matrix_sum:
   print(r)