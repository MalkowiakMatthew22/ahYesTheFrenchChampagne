import random
#strength
#dexterity
#intelligence
#wisdo
#charismag

points = 250

print("Welcome, adventurer! Skill point time! (250 points available)")

strength = int(input("How strong are you? This impacts you ability to fight, run for long distances, and other muscle-bound activities. (0-100) \n>"))

if strength > 100 or strength < 0 or strength > points:
    print("I am afraid that isn't a valid number. In a place like this, one wrong step is enough to get you killed.\nYOU LOSE!")
    exit()
points = points - strength
print("Hey, you chose that, not me. STRENGTH SET TO " + str(strength) + "\n")
print("You have " + str(points) + " skill points remaining.")

dexterity = int(input("How nimble, agile, and quick are you? This impacts your ability to move unseen, be flexible, or other deft and precise movements of the limbs and fingers. (0-100) \n>"))

if dexterity > 100 or dexterity < 0 or dexterity > points:
    print("I am afraid that isn't a valid number. In a place like this, one wrong step is enough to get you killed.\nYOU LOSE!")
    exit()
points = points - dexterity
print("DEXTERITY SET TO " + str(dexterity) + "\n")
print("You have " + str(points) + " skill points remaining.")

intelligence = int(input("How smart are you? This affects your ablitiy to recall facts, understand puzzles, and cast classical magic spells. (0-100) \n>"))

if intelligence > 100 or intelligence < 0 or intelligence > points:
    print("I am afraid that isn't a valid number. In a place like this, one wrong step is enough to get you killed.\nYOU LOSE!")
    exit()
points = points - intelligence
print("Nice IQ. INTELLIGENCE SET TO " + str(intelligence) + "\n")
print("You have " + str(points) + " skill points remaining.")


wisdo = int(input("How wise are you? This impacts(0-100) \n>"))

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

print("\n Your eyes dart open as you arise from mound of warm sand. Confused, you stare at your body and quickly brush yourself off as cool air breezes over you. 'Ah, I see you have awoken. It's about time,' a loud voice echos.\n You look around to find the source of the voice and find that you are in what appears to be a muggy sand-ridden cave with magically lit torch sconces lining the inside.\n'If you survive and escape I will drop all charges against you for your crimes. I simply want to see if the rumors about your feats are true. Please, move forward lest you wish to stay stranded.'")

#First Encounter
print("You encounter an imposing wall with large worn stalagmites standing close to the base. The wall stands tall, cracked, and unmoving. What do you do?")

print("1. punch the wall")
print("2. climb the wall")
print("3. magic the wall")
choice = input("Please, choose a number-->")

if choice == "1":
    if int(strength) > 80:
        print("--Your muscles, wrought as iron and machined to near perfection, delivers a quaking punch. The wall shatters in awe of your strength.--")

    else:

        roll = random.randrange(0, strength)
        if roll >  30:
            print("--The wall is sturdy and tall, but not without faults. You manage to land a strike in a fault line in the stone by shear luck. The wall shatters as you laugh in the face of chance.--")
    
        else:
            print("--Your fist is shattered as you lean into your blow. Ouch, you will need to rest that off.--\nYOU LOSE")
            exit()

elif choice == "2":
    if int(dexterity) > 70:
        print("--You find cracks in the wall and you scale the wall with ease. 'Impressive speed,'.--")

    else:

        roll = random.randrange(0, dexterity)
        if roll >  20:
            print("--You take your time and find some spots along where the wall and the cave meet and spot some rocks which you use the climb up.--")
    
        else:
            print("--You clammer unto and up the wall and make a small amount of headway. Aaly, your footing isn't as sure as you thought it would be. You slip and are dashed upon the rocks below.--\nYOU LOSE")
            exit()

elif choice == "3":
    print("\nCool, I guess it just works. I mean, magic is so subjective and in this setting, which you don't know anything about, and just having any 'level' of intelligence is totally abstract and doesn't mean you spent your time working towards magic specifically while gaining 'intelligence'.\nBut sure, fine I guess it just works, books are boring, magic is dumb, but sure just cast 'wizard skip' or something and skip to the next trial or whatever.\nYou hear the voice speak, 'Ah, a practioner of magic yourself! Maybe they weren't lying about you. God! Wizards are so cool!'\n")
else:
    print("I am afraid that isn't a valid number. One wrong step is enough to get you killed, and that's not any less true here.\nYOU LOSE!")
    exit()


#Second Encounter

print("After bypassing the wall you manage to stumble upon a chamber just above it. As you walk through the doorway you see that there is dense folliage covering the walls and the floor have a light moss carpet, cool and refreshing. As you look around you also notice a door set into the side of the room with the IMAGE OF A 3D CUBE ENGRAVED INTO IT. There is also a marble pedestal standing off to the side of the door with a scrambled 3x3 colored cube.")

print("1. punch ")
print("2. ")
print("3. ")
choice = input("Please, choose a number-->")