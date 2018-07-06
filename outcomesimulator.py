dicesides = 6
import random as r,math as m,time as t
def mod(stata,statb):
    parta = stata - statb
    partb = parta/5
    partc = abs(partb)
    return m.floor(partb)
    
print("""Welcome to RPG Outcome Simulator!

      /|     ________________
O|===|* >________________>
      \|""")
while True:
    try:
        stra = int(input("Enter the strength stat for the first character.")) # Enter stats
        skla = int(input("Enter the skill stat for the first character."))
        strb = int(input("Enter the strength stat for the second character."))
        sklb = int(input("Enter the skill stat for the second character."))
        break
    except:
        print("That's not valid. Please re-enter your values.")
while True:
    sklmod = int(mod(skla,sklb))
    strmod = int(mod(stra,strb))
    basesklmod = m.floor((skla + sklb) / 10)
    basestrmod = m.floor((stra + strb) / 10)
    if sklmod < basesklmod:
        sklmod = basesklmod
    if strmod < basestrmod:
        strmod = basestrmod
    while True:
        adice = r.randint(1,(skla * 10))
        bdice = r.randint(1,(sklb * 10))
        if adice > bdice:
            print("\n 1's Turn \n")
            skla = skla + sklmod
            stra = stra + strmod
            sklb = sklb - sklmod
            strb = strb - strmod
            print("Player 2 lost",strmod,"strength!\n")
            break
        elif bdice > adice:
            print("\n2's Turn \n")
            sklb = sklb + sklmod
            strb = strb + strmod
            skla = skla - sklmod
            stra = stra - strmod
            print("Player 1 lost",strmod,"strength!\n")
            break
        else:
            print("\nSleeping...\n")
            t.sleep(1)
    if skla + (sklb / 3) < sklb:
        skla = m.floor(sklb - (sklb / 3))
    if stra <= 0:
        print("Player 2 wins!")
        t.sleep(3)
        quit()
    if sklb + (skla / 3) < skla:
        sklb = m.floor(skla - (skla / 3))
    if strb <= 0:
        print("Player 1 wins!")
        t.sleep(3)
        quit()
    print("Player 1's current stats:",skla,"skill and",stra,"strength.")
    print("Player 2's current stats:",sklb,"skill and",strb,"strength.")
    t.sleep(1)

    
    
    
        
    
