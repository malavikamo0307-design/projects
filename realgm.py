
print("LEGENDS OF THE FORGOTTEN REALM")
print("-------------------------------")

print("1. New Game")
print("2. Continue")
print("3. Instructions")
print("4. Exit")

choice = input("Enter your choice: ")
if choice == "1":

    name = input("Enter Player Name: ")

    print("\nChoose Your Class")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Assassin")

    class_choice = input("Enter your choice: ")

    print("\nPlayer Name:", name)
    print("Class choice:", class_choice)

    if class_choice == "1":
        player_class = "Warrior"
        hp = 150
        mana = 50
        attack = 30
        defense = 25
        crit_chance = 10

    elif class_choice == "2":
        player_class = "Mage"
        hp = 100
        mana = 150
        attack = 35
        defense = 10
        crit_chance = 15

    elif class_choice == "3":
        player_class = "Archer"
        hp = 120
        mana = 100
        attack = 25
        defense = 15
        crit_chance = 25

    elif class_choice == "4":
        player_class = "Assassin"
        hp = 90
        mana = 100
        attack = 35
        defense = 10
        crit_chance = 30

    else:
        print("Invalid class choice") 
    print("\n===== PLAYER CREATED =====")
    print("Name:", name)
    print("Class:", player_class)
    print("HP:", hp)
    print("Mana:", mana)
    print("Attack:", attack)
    print("Defense:", defense)
    print("Critical Chance:", crit_chance, "%")       






    