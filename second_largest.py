n = int(input("Introdu n: "))
arr = map(int, input().split())
maximum = max(arr)
arr = [x for x in arr if x != maximum]
print(max(arr))