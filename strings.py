b = "Hello, World!"
print(b[0:5])

#a = """Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua."""
#print(a)

print(b[-6:-1])
print(b.replace('l', 'r'))
print(b.lower())
print(b.upper())
print(b.split(","))
x = b.split(", ")
for i in range(len(x)):
    print(x[i])
print(len(x))

age = 36
txt = "My name is John , and I am {}"
print(txt.format(age))

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


for x in list2:
  list1.append(len(list2) - x + 1)

print(list1)