print("- Pythagorean Triple -")

def check():
    while True:
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
        if((a*a + b*b) == c*c):
            print("(" + str(a) + ", " + str(b) + ", " + str(c) + ") - Pythagorean Triple.")
        else:
            print("Nope.")
        if(input("Wanna try again? : y = yes, n = no\n") != "y"):
            break

check()
