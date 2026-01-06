print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = input("You are on a cross road. Where do you want to go? Type 'left' or 'right'. ").lower()

if cross_road == "left":
    choice1 = input("You have come to a lake. There is an island in the middle of the lake. "
                    "Type 'wait' to wait for a boat. "
                    "Type 'swim' to swim across.   ").lower()
    if choice1 == "wait":
        choice2 = input("You arrived at the island unharmed. There is a house with three doors. "
                        "One red, one blue, one yellow. Which colour of door would you choose? " 
                        "Type 'R' for red, 'B' for blue, 'Y' for yellow.  ").upper()
        if choice2 == "R":
            print("Game Over. You were stuck in a quick sand")
        elif choice2 == "B":
            print("Game Over. You entered fire")
        elif choice2 == "Y":
            print("Congratulations! You found the treasure.")
        else:
            print("Game Over. You choose a wrong door.")
    else:
        print("Game Over. You got attacked by Aligator")
        
else:
    print("Game Over. You Lose!")