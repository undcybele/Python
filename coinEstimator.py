from math import floor

class Coin:
    def __init__(self, name, mass, value, wrap, numberOfCoins = 0, totalWeight = 0, wrappers = 0):
        self.name = name
        self.mass = mass
        self.value = value
        self.wrap = wrap
        self.numberOfCoins = 0
        self.totalWeight = 0
        self.wrappers = 0

class Penny(Coin):
    def __init__(self):
        super().__init__(name = "Pennies", mass = 2.5, value = 0.01, wrap = 50)

class Nickel(Coin):
    def __init__(self):
        super().__init__(name = "Nickels", mass = 5, value = 0.05, wrap = 40)

class Dime(Coin):
    def __init__(self):
        super().__init__(name = "Dimes", mass = 2.268, value = 0.1, wrap = 50)

class Quarter(Coin):
    def __init__(self):
        super().__init__(name = "Quarters", mass = 5.67, value = 0.25, wrap = 40)

penny = Penny()
nickel = Nickel()
dime = Dime()
quarter = Quarter()

def coinEstimator():

    # -- CALCULATIONS --
    def getMass(self):
        print(self.name, ": ")
        self.totalWeight = input("  Total weight: ")
        print("\n")
    
    def getNumberOfCoins(self):
        self.numberOfCoins = round(float(self.totalWeight)/self.mass)
    
    def getNumberOfWrappers(self):
        self.wrappers = floor(self.numberOfCoins/self.wrap)
    

    getMass(penny)
    getMass(nickel)
    getMass(dime)
    getMass(quarter)
    
    getNumberOfCoins(penny)
    getNumberOfCoins(nickel)
    getNumberOfCoins(dime)
    getNumberOfCoins(quarter)

    getNumberOfWrappers(penny)
    getNumberOfWrappers(nickel)
    getNumberOfWrappers(dime)
    getNumberOfWrappers(quarter)

    totalValue = (penny.numberOfCoins * penny.value +
    		nickel.numberOfCoins * nickel.value +
    		dime.numberOfCoins * dime.value +
    		quarter.numberOfCoins * quarter.value)

    # -- PRINT --
    def printNumber(self):
        print("     ", self.name, self.numberOfCoins)

    def printWrappers(self):
        print("     ", self.name, self.numberOfCoins)

    print("\nNumber of each coin type: ")
    printNumber(penny)
    printNumber(nickel)
    printNumber(dime)
    printNumber(quarter)

    print("\nNumber of wrappers needed for each coin type: ")
    printWrappers(penny)
    printWrappers(nickel)
    printWrappers(dime)
    printWrappers(quarter)

    print("Total value: $", totalValue)

    
coinEstimator()