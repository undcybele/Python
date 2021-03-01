list = [l for l in range(0, 10) if l % 2 == 0]
for _ in range(int(input())):
    list.pop()

print(list)