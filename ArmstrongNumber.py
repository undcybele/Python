x = int(input("Da un x = "))
rev = 0
sum = 0
i = 0
number = []
y = x
while(y > 0):
    dig=y%10
    rev=rev*10+dig
    y=y//10 
    number.append(dig)

print(number)

while i < len(number): 
     sum = sum + pow(number[i], len(number))
     i = i+1

if sum == x:
    print("Nr este un nr Armstrong")
else:
    print("Nr nu este un nr Armstrong")

    