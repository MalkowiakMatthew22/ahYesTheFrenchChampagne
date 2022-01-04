import random
#strength
#dexterity
#intelligence
#wisdo
#charisma

points = 250

print("Welcome, adventurer! Skill point time! (250 points available)")

strength = int(input("How strong are you? This impacts you ability to fight, run for long distances, and other muscle-bound activities. (0-100) \n>"))

if strength > 100 or strength < 0 or strength > points:
    print("I am afraid that isn't a valid number. In a place like this, one wrong step is enough to get you killed.\nYOU LOSE!")
    exit()
points = points - strength
print("Hey, you chose that, not me. STRENGTH SET TO " + str(strength) + "\n")
print("You have " + str(points) + " skill points remaining.")

dexterity = int(input("How nimble are you? This impacts your ability to move unseen, be flexible, or other deft movements of the limbs and fingers. (0-100) \n>"))

if dexterity > 100 or dexterity < 0 or dexterity > points:
    print("I am afraid that isn't a valid number. In a place like this, one wrong step is enough to get you killed.\nYOU LOSE!")
    exit()
points = points - dexterity
print("DEXTERITY SET TO " + str(dexterity) + "\n")
print("You have " + str(points) + " skill points remaining.")

intelligence = int(input("How smart are you? This affects your ablitiy to recall facts, understand puzzles, and casting classical magic spells. (0-100) \n>"))

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

#Stats Screen

print("You have completed stat selection. Here are your stats: \n- STRENGTH: "+ str(strength) +" \n- DEXTERITY: "+ str(dexterity) +" \n- INTELLIGENCE: "+ str(intelligence) +" \n- WISDO: "+ str(wisdo) +" \n- CHARISMA: "+ str(charisma) +"")

#Intro

print("\n Your eyes dart open as you arise from mound of warm sand. Confused, you stare at your body and quickly brush yourself off as cool air breezes over you. 'Ah, I see you have awoken. It's about time,' a loud voice echos.\n You look around to find the source of the voice and find that you are in what appears to be a muggy sand-ridden cave with magically lit torch sconces")

#First Encounter
print("You encounter an imposing wall with large worn stalagmites standing close to the base. The wall stands tall, cracked, and unmoving. What do you do?")

print("1. punch the wall")
print("2. climb the wall")
print("3. magic the wall")
choice = input("Please, choose a number above>")

if choice == "1":
    if int(strength) > 80:
        print("--The wall shatters in awe of your divine strength.--")

    else:

        roll = random.randrange(0, strength)
        if roll >  20:
            print("--The wall shatters as you laugh in the face of chance.--")
    
        else:
            print("--Your fist is shattered as you lean into your mighty blow. Ouch, you will need to rest that off.--\nYOU LOSE")
            exit()

elif choice == "2":
    if int(dexterity) > 70:
        print("--You find cracks in the wall--")

    else:

        roll = random.randrange(0, strength)
        if roll >  20:
            print("--.--")
    
        else:
            print("--You clammer unto and up the wall and make a small amount of headway Your footing isn't as sure as you thought it would be.--\nYOU LOSE")
            exit()

elif choice == "3":
    print("cool")
else:
    print("I am afraid that isn't a valid number. One wrong step is enough to get you killed, and that's not any less true here.\nYOU LOSE!")
    exit()
