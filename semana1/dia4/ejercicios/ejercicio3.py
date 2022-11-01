"""
CSES - Missing Numbers - resolution in O(n) y O(1)

You are given all numbers between 1,2,…,n except one. 
Your task is to find the missing number.

"""

# O(1)

import random

number = int(input("Ingrese el numero: "))
list = list(range(1, number+1))
list.pop(random.randrange(len(list)))
sum_of_n = number * (number +1) / 2
list_sum = sum(list)
missing_number = sum_of_n - list_sum
print(list)
print(int(missing_number))