import random
#strength
#dexterity
#intelligence
#wisdo
#charisma

points = 250

print("Welcome, adventurer! Skill point time! (250 points available)")

strength = int(input("How strong are you? This impacts you ability to fight, run for long distances, and other muscle bound activities. (0-100) \n>"))

if strength > 100 or strength < 0 or strength > points:
    print("I am afraid that isn't a valid number. In a place like this, one wrong step is enough to get you killed.\nYOU LOSE!")
    exit()
points = points - strength
print("Hey, you chose that, not me. STRENGTH SET TO " + str(strength) + "\n")
print("You have " + str(points) + " skill points remaining.")

dexterity = int(input("How nimble are you? This impacts your ability to move unseen, be flexible, or  (0-100) \n>"))

if dexterity > 100 or dexterity < 0 or dexterity > points:
    print("I am afraid that isn't a valid number. In a place like this, one wrong step is enough to get you killed.\nYOU LOSE!")
    exit()
points = points - dexterity
print("DEXTERITY SET TO " + str(dexterity) + "\n")
print("You have " + str(points) + " skill points remaining.")

intelligence = int(input("How smart are you? (0-100) \n>"))

if intelligence > 100 or intelligence < 0 or intelligence > points:
    print("I am afraid that isn't a valid number. In a place like this, one wrong step is enough to get you killed.\nYOU LOSE!")
    exit()
points = points - intelligence
print("Nice IQ. INTELLIGENCE SET TO " + str(intelligence) + "\n")
print("You have " + str(points) + " skill points remaining.")


wisdo = int(input("How wise are you? (0-100) \n>"))

if wisdo > 100 or wisdo < 0 or wisdo > points:
    print("I am afraid that isn't a valid number. In a place like this, one wrong step is enough to get you killed.\nYOU LOSE!")
    exit()
points = points - wisdo
print("WISDO SET TO " + str(wisdo) + "\n")
print("You have " + str(points) + " skill points remaining.")

charisma = int(input("How charming are you? (0-100) \n>"))

if charisma > 100 or charisma < 0 or charisma > points:
    print("I am afraid that isn't a valid number. In a place like this, one wrong step is enough to get you killed.\nYOU LOSE!")
    exit()
points = points - charisma
print("CHARISMA SET TO " + str(charisma) + "\n")
print("You have " + str(points) + " skill points remaining.")

#First Encounter
print("You encounter an imposing wall. It stands tall and unmoving... for now. What do you do?")

print("1. punch the wall")
print("2. climb the wall")
print("3. magic the wall")
choice = input("Please, choose a number above>")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll >  20:
        print("The wall shatters in awe of your divine strength")
    
    else:
        print("Your fist is shattered as you lean into your mighty blow. Ouch, you will need to rest that off.\nYOU LOSE")
        exit()

elif choice == "2":
    print("cool")
elif choice == "3":
    print("cool")
else:
    print("I am afraid that isn't a valid number. One wrong step is enough to get you killed, and that's not any less true here.\nYOU LOSE!")
    exit()
