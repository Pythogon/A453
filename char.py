import math,random,time # Importing required modules
def rollstats(large,small,basestat,maxstatbonus): # Roll stat function
    statbonustotal = maxstatbonus + basestat
    largedice = random.randint(1,large)
    time.sleep(1) # Rolling large and small dice, similar program feature as task 1.
    smalldice = random.randint(1,small)
    floored = math.floor(largedice / smalldice)
    if floored + basestat >= statbonustotal: # Stopping overpowered characters by stopping any stat value from becoming over 20, so no 21 or 22
        output = floored #  Nerfed output
    else:
        output = floored + basestat # Basic output
    return output

def write(stn,skl,scr,ign): # Define STN (STreNgth), SKL, (SKiLl), SCR (SCoRe) and IGN (In-Game Name, or name)
        with open('char.txt', 'a+') as file:
            toapp = "Hero " + str(ign) + " stats: " + str(skl) + " skill, and " + str(stn) + " strength. Score: "+ str(scr) +"\n" # Extensive formatting to allow it to be written
            file.write(toapp)
            print("Written data for",ign +'!')
                      
print("Welcome to your adventure, hero.")
maxbonus = 11
while True:
    while True:
        try:
            bulk = input("Would you like to bulk create character data? Y/N") # Bulk mode? Try except error proofed.
            bulk = bulk.lower()
            if bulk != 'y' and bulk != 'n':
                raise ValueError
            break
        except:
            print("That's not valid.")
    if bulk == 'n':
        name = input("Enter your character name!") # Enter name for saving to file later
        time.sleep(1)
        print("Rolling your stats!")
        skill = rollstats(12,4,10,maxbonus)
        strength = rollstats(12,4,10,maxbonus) # Roll stats
        score = (skill + strength) - 20
        print("Congratulations,",name,"as you rolled",skill,"skill and",strength,"strength. SCORE:",score) # After wait, tell the user what they rolled.
        time.sleep(1)
        print("Saving your progress...") # Illusion of taking time to save.
        write(strength,skill,score,name)
        time.sleep(3)
    else:
        print("Welcome to the bulk character data creation menu.") # Added bulk system
        names = input("Enter character names seperated by commas.") # Same code as singular character creation just edited for bulk.
        names = names.split(',')
        for x in range(len(names)):
            print("Rolling stats for",names[x] + ":")
            skill = rollstats(12,4,10,11)
            strength = rollstats(12,4,10,maxbonus)
            score = (skill + strength) - 20
            print(skill,'skill and',strength,'strength. Score:',score)
            write(strength,skill,score,names[x])
        print("Data creation complete!") # Confirmation message

    while True:
        try:
            breakaway = input("Do you wish to create more character data? Y/N")
            breakaway = breakaway.lower()
            if breakaway != 'n' and breakaway != 'y':
                raise ValueError
            break
        except:
            print("That's not correct. Please try again.")
            time.sleep(0.5)
    if breakaway == 'y':
        print("Restarting...")
    else:
        print("Come back soon, hero.")
        time.sleep(2)
        break



