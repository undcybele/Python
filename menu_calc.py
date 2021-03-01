
def menu():
    print("This is the menu: ")
    print("--------------------")
    print("""           1. Chicken Strips - $3.50
              2. French Fries - $2.50
              3. Hamburger - $4.00
              4. Hotdog - $3.50
              5. Large Drink - $1.75
              6. Medium Drink - $1.50
              7. Milk Shake - $2.25
              8. Salad - $3.75
              9. Small Drink - $1.25""")

    price={1:3.5, 2:2.5, 3:4, 4:3.5 ,5:1.75, 6:1.25, 7:2.25, 8:3.75, 9:1.25}
    
    order = list(map(int, input("Input your order \n").split()))

    total=0
    for i in order:
        total += (price[i])
    print("Total = $", total)

#driver code
menu()

