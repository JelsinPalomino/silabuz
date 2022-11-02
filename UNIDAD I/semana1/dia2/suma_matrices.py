import random

matrix_1 = [[random.randint(0, 99),random.randint(0, 99)],[random.randint(0, 99),random.randint(0, 99)]]
matrix_2 = [[random.randint(0, 99),random.randint(0, 99)],[random.randint(0, 99),random.randint(0, 99)]]
print (matrix_1)
print (matrix_2)
matrix_sum=[[0,0],[0,0]]

for i in range(len(matrix_1)):
    for j in range(len(matrix_2)):
        matrix_sum[i][j]=matrix_1[i][j]+matrix_2[i][j]
        j=+1
    i+=1
print(matrix_sum)