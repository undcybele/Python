text = list(input())
counter = 0
for s in set(text):
    if text.count(s) > 1 :
        counter += 1
print(counter)