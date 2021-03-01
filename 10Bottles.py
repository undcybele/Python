

for x in (range(11, 0, -1)):
    if x == 1:
        print(str(x) + "bottle of beer on the wall, " + str(x) + " bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.")
    else:
        print(str(x) + " bottles of beer on the wall, " + str(x) + " bottle of beer. Take one down and pass it around, " + str(x-1) + " bottles of beer on the wall")

