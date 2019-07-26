'''

Let's' roll a fucking DICE

'''

from random import randint
from time import sleep

#Function to prompt to user an input for the number to guess
def get_user_guess():
    guess = int(input('Guess a number: '))
    return guess


#Roll the dice function
def roll_dice(number_of_sides):
    
    #setting the limit for the random rolling
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    
    #Setting the maximum value for the dices
    max_val = number_of_sides * 2
    
    #Presenting the maximum number to the user
    print ("The maximum possible value is %d " % max_val)
    guess = get_user_guess()
    
    #If the user inputs a number higher than the maximum number of the dice, gets an error message
    if (guess> max_val):
        print("Guess number higher then maximum %d " % max_val)
        
    #Now is game on!
    else:
        print("Rolling")
        sleep(2)
        
        #Value of first roll
        print("First roll: %d" % first_roll)
        sleep(2)
        
        #Value of Second roll
        print("Second roll: %d" % second_roll)
        
        #total roll value and present to user
        sleep(1)
        total_roll = first_roll + second_roll
        print ("Result %d" % total_roll)
        
        #Check if user actually guessed the number
        sleep(1)
        if guess == total_roll:
            
            #Win message
            print("You won!")
        else:
            #Lose message
            print("You lose!")

#Call the function to test your code!
roll_dice(9)    

