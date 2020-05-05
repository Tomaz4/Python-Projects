import random

keyPress = "y"

while keyPress == "y":
    numberOnDice = random.randint(1,6)
    if(numberOnDice == 1):
        print("----------")
        print("|        |")
        print("|   0    |")
        print("|        |")
        print("----------")
    elif(numberOnDice == 2):
        print("----------")
        print("|        |")
        print("|  0  0  |")
        print("|        |")
        print("----------")
    elif(numberOnDice == 3):
        print("----------")
        print("| 0      |")
        print("|    0   |")
        print("|      0 |")
        print("----------")
    elif(numberOnDice == 4):
        print("----------")
        print("| 0    0 |")
        print("|        |")
        print("| 0    0 |")
        print("----------")
    elif(numberOnDice == 5):
        print("----------")
        print("| 0    0 |")
        print("|    0   |")
        print("| 0    0 |")
        print("----------")
    elif(numberOnDice == 6):
        print("----------")
        print("| 0    0 |")
        print("| 0    0 |")
        print("| 0    0 |")
        print("----------")

    keyPress = input("Press y for another roll...")

