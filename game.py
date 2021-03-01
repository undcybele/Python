import random

class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Gun:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

number_of_shots = 0

weapons = {"Pistols" : 10, "Shotgun" : 30, "Minigun" : 50, "Flamethrower" : 40, "Thompson" : 60, "Lasergun" : 70, "Cannon" : 80}
enemies = {"Kamikaze" : 30, "Gnaar" : 40, "Kleer Scheleton" : 50, "Bio-mechanoid" : 80}

def print_dic(dictionary):
    i = 0
    for k, v in dictionary.items():
        print("{} : {}\t-\t{}".format(i, k, v))
        i += 1

def generator():
    global current_enemy
    index_enemy = random.randint(0, len(enemies) - 1)
    current_enemy = Entity(list(enemies.items())[index_enemy][0], list(enemies.items())[index_enemy][1])
    print("Enemy :\t" + current_enemy.name)
    print("\t{}".format(current_enemy.health))

    global current_weapon
    print("\n")
    print_dic(weapons)
    index_weapon = int(input("\nChoose your weapon : "))
    current_weapon = Gun(list(weapons.items())[index_weapon][0], list(weapons.items())[index_weapon][1])
    print("Weapon:\t" + current_weapon.name)
    print("\t{}".format(current_weapon.damage))
       

def spawn():
    return random.randint(0, 1)

def dmg():
    current_enemy.health -= current_weapon.damage
    return current_enemy.health

def main():
    global number_of_shots
    generator()
    while int(input("\nPress \'1\' to shoot : ")) == 1:
        dmg()
        print("\t{}".format(current_enemy.health))
        number_of_shots += 1
        if current_enemy.health <= 0:
            print("Dead in {} shots.\n".format(number_of_shots))
            break
        
while spawn():
    main()