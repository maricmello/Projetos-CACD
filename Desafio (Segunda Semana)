# (EASY) Capitalize the first letter of each word while preserving numbers and spaces. 
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# (INTERMEDIATE) The task is to calculate the total happiness (starting at 0) based on whether elements from an array are in 
# - set A (increase happiness +1)
# - set B (decrease happiness -1)
#  If the element is in neither set, the happiness remains unchanged.

array = []
a = set()  
b = set() 
happiness = 0

n, m = input().split()
array = input().split()
a = set(input().split())
b = set(input().split())

for i in array:
    if i in a:
        happiness += 1  
    elif i in b:
        happiness -= 1  

print(happiness)



