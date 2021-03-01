x = int(input("Introdu x: "))
y = int(input("Introdu y: "))
z = int(input("Introdu z: "))
n = int(input("Introdu n: "))
 

#cu for loops 
lst = []
i=0
j=0
k=0
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                lst.append([i,j,k])
print(lst) 

print("\n\n")

#cu list comprehension
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])
