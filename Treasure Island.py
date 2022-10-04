print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("welcome to Treasure Island.")
print("Your mission is to find the hidden treasure.")
choice1 = input('You\'re at a crossroad. Which direction do you head in? Type "Right" or "Left?"\n').lower()

if choice1 == "left":
    choice2 = input('You come to a lake that is eerily black. You see an island in the middle and know that\'s where '
                    'the treasure is. Type "wait" to wait for the ferry. Type "swim" to swim.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a castle that has 3 doors for you to choose. One "
                        "is red, "
              "one is blue, and one is yellow. Which door to go through?\n").lower()
        if choice3 == "red":
            print("CONGRATS YOU HAVE FOUND THE ANCIENT TREASURE OF THE KING!!! ALL THE FORTUNE IS YOURS!")
        elif choice3 == "blue":
            print("A very angry undead king sees you snooping for his treasure. He makes sure you don't share the tale. GAME OVER")
        elif choice3 == "yellow":
            print("You see a quick flash of light and before you know it your head has been chopped off. GAME OVER")
    else:
        print("While swimming you get eaten to death by a very hungry shark. GAME OVER")
else:
    print("You run into a goblin and get merked. GAME OVER")