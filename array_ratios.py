import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr,n):
    print(len([i for i in arr if i>0])/n)
    print(len([i for i in arr if i<0])/n)
    print(len([i for i in arr if i==0])/n)
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)
