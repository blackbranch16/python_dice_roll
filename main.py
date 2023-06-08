# Dice Roll Assignment
print("WELCOME TO THE DICE ROLL SIMULATOR")

# Import Math Functions
import random

# Main Program Loop
loop = True
while loop: 
    # Print Main Menu
    print("\nMAIN MENU")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times")
    print("4. Roll Dice until Snake Eyes")
    print("5. Exit")

    # Get Menu Selector from User Selection 
    selection = input("Select an option (1-5): ")

    # Take Action Based on Menu Selection 
    if selection == "1":
        randNum = random.randrange(1,6)
        randNum2 = random.randrange(1,6)
        sum = randNum + randNum2
        print(str(randNum) + ", " + str(randNum2) + " (sum: " + str(sum) + ")")
    elif selection == "2":
        for n in range(5):
            randNum = random.randrange(1,6)
            randNum2 = random.randrange(1,6)
            sum = randNum + randNum2
            print(str(randNum) + ", " + str(randNum2) + " (sum: " + str(sum) + ")")
    elif selection == "3":
        userInput = input("How many rolls would you like? ")
        for n in range(int(userInput)):
            randNum = random.randrange(1,6)
            randNum2 = random.randrange(1,6)
            sum = randNum + randNum2
            print(str(randNum) + ", " + str(randNum2) + " (sum: " + str(sum) + ")")
    elif selection == "4":
        total = 0
        snakeRandNum = 1
        snakeRandNum2 = 1
        randNum = random.randrange(1,6)
        randNum2 = random.randrange(1,6)
        while randNum != snakeRandNum and randNum2 != snakeRandNum2:
            randNum = random.randrange(1,6)
            randNum2 = random.randrange(1,6)
            total = total + 1
            sum = randNum + randNum2
            print(str(randNum) + ", " + str(randNum2) + " (sum: " + str(sum) + ")")
        print("SNAKE EYES!")
    elif selection == "5":
        print("EXIT")
        loop = False

