#Christopher Holmes
#Patrick Gonzalez

#Import random library to be used
from random import *

#Roll Dice function to simulate rolling a dice
def rollDice():
    return randint(1,6)

#Loop control variable and variable to store the point in
loopControl = True
point = 0

#While loop to continue looping as long as the game hasn't been lost
while loopControl:

    #Roll both dice, and store the total of both dice into total
    dice1 = rollDice()
    dice2 = rollDice()
    total = dice1 + dice2
    
    #Print out what two numbers you rolled
    print("You rolled a %s and a %s.")%(dice1, dice2)
    
    #Check to see if this is the first roll by seeing if point equals 0
    if point == 0:
        #If total equals 7 or 11, print you win and end the game.
        if total == 7 or total == 11:
            print("Congrats you rolled a %s! You win!")%total
            loopControl = False
        #If total equals 2, 3, or 12, print what you rolled and that you lost
        elif total == 2 or total == 3 or total == 12:
            print("You rolled a %s, you lose.")%total
            loopControl = False
        #For all other rolls, print the roll and that you get to roll again. 
        #Prompt for any key to allow users to roll. Set point variable to total
        else:
            print("You rolled a %s. Roll again.")%total
            raw_input("Press any key to roll again.")
            point = total
    #Any roll after the first roll
    else:
        #Check to see if total equals point, print you win if it does
        if total == point:
            print("Congrats you rolled the point %s again! You win!")%total
            loopControl = False
        #Check to see if roll equals 7, print you lose if it does
        elif total == 7:
            print("You rolled a %s, you lose.")%total
            loopControl = False
        #Any other roll print total and roll again
        else:
            print("You rolled a %s. Roll again.")%total
            point = total
            raw_input("Press any key to roll again.")
            
            
