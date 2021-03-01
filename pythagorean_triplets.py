import math

choice=1
while choice==1:
    x = int(input('Give 1st nr = '))
    y = int(input('Give 2nd nr = '))
    z = int(input('Give 3rd nr = '))
    
    if((x*x)+(y*y)==(z*z) or (x*x)+(z*z)==(y*y) or (z*z)+(y*y)==(x*x)):
        print('The numbers represent a pythagorean triplet')
    else: print('The numbers arent a triplet')

    choice = int(input('Wanna go again? 1 - yes// 0 - nope ' ))
    if choice == 0:
        print("Ok bye heathen")
        break


