import random, time # Imports all the modules required.
def roll(dnum):
    return random.randint(1,dnum) # Roll a random number and return it from the function.
print("Welcome to the dice.") # Welcome print outside of the while True.

while True:
    
    while True:
        try:
            dsides = int(input("Please choose how many sides your dice will have. 4, 6, or 12? ")) # Try except clause to error proof this input.
            if dsides != 4 and dsides != 6 and dsides != 12: 
                raise ValueError # We only want the dice to work if the side number is 4, 6 or 12.
            break
        except:
            print("Sorry, that's not a valid number. Please try again.") # Handles the error - in case the user types something like 'a' or '7'.
            
    print("Okay, rolling the",dsides,"sided dice.") # Telling the user what dice is being rolled.
    dresult = roll(dsides) # Storing the result for later.
    time.sleep(2)
    print("You rolled a", dresult,"this time.") # Telling the user what was rolled.
    while True:
        try:
            restart = input("Do you wish to roll another dice? Y/N ")
            if restart.lower() != 'y' and restart.lower() != 'n': # Checking for errors
                raise ValueError # Raise an eror
            break
        except:
            print("That's not Y or N, please try again.") # Error message
    if restart.lower() == 'y': # Checking if it's y
        print("Restarting...")
        time.sleep(1)
    else:
        print("Thanks for using the dice program today.") # If it's not y or n, it can't have gotten through error handling, so it's definitely n.
        time.sleep(1)
        print("Shutting down...")
        time.sleep(2)
        print("Powered off.")
        break
        
            
            
    

