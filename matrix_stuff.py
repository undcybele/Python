#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    sum1 = 0
    sum2 = 0
    i=0
    j=0

    suma1 = [arr[i][j] for i in range(n) for j in range(n) if i==j]
    sum1 = sum(suma1)
    
    suma2 = [arr[i][j] for i in range(n) for j in range(n) if i==n-j-1]
    sum2 = sum(suma2)

    

    return abs(sum1-sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()