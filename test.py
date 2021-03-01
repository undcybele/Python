from itertools import groupby
# A = list(map(int, input().split(' ')))
# print(A)
# 
# string = input().split()
# print(string[0])
# print(int(string[1]))
# 

def key(number):
    return 1 if int(number) % 2 == 0 else 0
n = "1112222333447"
print(*[(len(list(c)), int(k)) for k, c in groupby(n, key(n))])