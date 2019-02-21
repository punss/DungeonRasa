import random
import sys
import nlu_model

bag=[]
wlist=[]
pu=0
train()
run("get sword")
print(" ")
print("take item --> Adds item to bag.")
print("use item --> Uses item.")
print("n,s,e,w --> Move north, south, east or west.")
print("desc --> Describes your surroundings.")
print("bag --> Shows your bag.")
print("help --> Displays this menu.")
print("exit --> Quits the game.")
print(" ")

def r1():
    if "key" in bag:
        print("You are in a dimly lit room. There is a door towards the north.")
    else:
        print("You are in a dimly lit room. There is a door towards the north. There is a key on the floor.")
    ans="hello"
    while(ans!="a20151"):
        ans=input("")
        if (ans=="help"):
            print("take item --> Adds item to inventory")
            print("use item --> Uses item.")
            print("n,s,e,w --> Move north, south, east or west.")
            print("desc --> Describes your surroundings.")
            print("bag --> shows your bag.")
            print("help --> Displays this menu.")
            print("exit --> Quits the game.")
        elif (ans=="exit"):
            sys.exit()
        elif (ans=="desc"):
            print("You are in a dimly lit room. There is a door towards the north.")
            if "key" not in bag:
                print("There is a key on the floor.")
        elif (ans=="take key"):
            if "key" in bag:
                print("You have already picked the key up.")
            else:
                print("Key taken.")
                bag.append("key")
        elif (ans=="bag"):
            print(bag)
        elif (ans=="n"):
            if "key" in bag:
                h1()
            else:
                print("The door is locked. You need a key to open it.")
        elif (ans=="use key"):
            if("key" in bag):
                print("You need to move towards a door to use the key.")
            else:
                print("You do not have a key.")
        elif (ans=="s"):
            print("You cannot move in that direction.")
        elif (ans=="e"):
            print("You cannot move in that direction.")
        elif (ans=="w"):
            print("You cannot move in that direction.")
        else:
            print("That is not a valid command. Type help for a list of valid commands.")

def h1():
    ans="desc"
    print("You are now in a hallway. There are 4 doors around you. There are scary noises coming from the door in front of you.")
    while(ans!="a20151"):
        ans=input("")
        if (ans=="exit"):
            sys.exit()
        elif (ans=="help"):
            print("take item --> Adds item to inventory")
            print("use item --> Uses item.")
            print("n,s,e,w --> Move north, south, east or west.")
            print("desc --> Describes your surroundings.")
            print("bag --> shows your bag.")
            print("help --> Displays this menu.")
            print("exit --> Quits the game.")
        elif (ans=="desc"):
            print("You are in a hallway. There are 4 doors around you.")
        elif(ans=="use key"):
            print("You need to move towards a door to use the key.")
        elif(ans=="use candy bar"):
            if "candy bar" in bag:
                pu=1
                print("Power Up!")
                print("Your attacks will now do more damage!")
            else:
                print("You do not have a candy bar.")
        elif(ans=="use sword"):
            if "sword" in bag:
                print("Oak's words echoed: There's a time and place for everything.")
            else:
                print("You do not have a sword.")
        elif(ans=="use axe"):
            if "axe" in bag:
                print("Oak's words echoed: There's a time and place for everything.")
            else:
                print("You do not have an axe.")
        elif (ans=="bag"):
            print(bag)
        elif (ans=="w"):
            r2()
        elif (ans=="e"):
            if "key 2" in bag:
                r3()
            else:
                print("The door is locked and the key that you have cannot unlock it.")
        elif (ans=="n"):
            if ("sword" in bag):
                br()
                print("bossroom")
            elif ("axe" in bag):
                br()
                print("bossroom")
            elif ("candy bar" in bag):
                br()
                print("bossroom")
            else:
                print("You don't have a weapon, you will not dare enter.")
        elif (ans=="s"):
            r1()
        else:
            print("That is not a valid command. Type help for a list of valid commands.")

def r2():
    ans="desp"
    print("You are now in a room with a huge window with a sexy view. There is a shelf with a jar on it. The rest of the room is empty.")
    while (ans!="a20151"):
        ans=input()
        if (ans=="help"):
            print("take item --> Adds item to inventory")
            print("use item --> Uses item.")
            print("n,s,e,w --> Move north, south, east or west.")
            print("desc --> Describes your surroundings.")
            print("bag --> shows your bag.")
            print("help --> Displays this menu.")
            print("exit --> Quits the game.")
        elif (ans=="desc"):
            print("There is a huge window with a sexy view outside it. There is a shelf with a jar on it. There is nothing else in the room.")
        elif (ans=="bag"):
            print(bag)
        elif (ans=="exit"):
            sys.exit()
        elif(ans=="take jar"):
            print("Sad life, no cookies for you. There's a key inside though. You pick it up.")
            bag.append("key 2")
        elif(ans=="use candy bar"):
            if "candy bar" in bag:
                pu=1
                print("Power Up!")
                print("Your attacks will now do more damage!")
            else:
                print("You do not have a candy bar.")
        elif(ans=="use sword"):
            if "sword" in bag:
                print("Oak's words echoed: There's a time and place for everything.")
            else:
                print("You do not have a sword.")
        elif(ans=="use axe"):
            if "axe" in bag:
                print("Oak's words echoed: There's a time and place for everything.")
            else:
                print("You do not have an axe.")
        elif(ans=="e"):
            h1()
        elif(ans=="n"):
            print("You cannot move in that direction.")
        elif(ans=="w"):
            print("You cannot move in that direction.")
        elif(ans=="s"):
            print("You cannot move in that direction.")
        else:
            print("That is not a valid command. Type help for a list of valid commands.")

def r3():
    ans="bru"
    print("You are now in what looks like a weapons room. There are swords and axes.")
    print("There's also an err, candy bar on the floor.")
    while(ans!="yeet"):
        ans=input()
        if (ans=="help"):
            print("take item --> Adds item to inventory)")
            print("use item --> Uses item.")
            print("n,s,e,w --> Move north, south, east or west.")
            print("desc --> Describes your surroundings.")
            print("bag --> shows your bag.")
            print("help --> Displays this menu.")
            print("exit --> Quits the game.")
        elif (ans=="desc"):
            print("There are swords and axes and a candy bar around you.")
        elif (ans=="exit"):
            sys.exit()
        elif (ans=="bag"):
            print(bag)
        elif (ans=="take sword"):
            if ("sword" in bag):
                print("You have already taken the sword")
            else:
                print("Sword taken")
                bag.append("sword")
                wlist.append("sword")
        elif (ans=="take axe"):
            if ("axe" in bag):
                print("You have already taken the axe")
            else:
                print("axe taken")
                bag.append("axe")
                wlist.append("axe")
        elif (ans=="take candy bar"):
            if ("candy bar" in bag):
                print("You have already taken the candy bar")
            else:
                print("Candy Bar taken")
                bag.append("candy bar")
                wlist.append("candy bar")
        elif(ans=="use candy bar"):
            if "candy bar" in bag:
                pu=1
                print("Power Up!")
                print("Your attacks will now do more damage!")
            else:
                print("You do not have a candy bar.")
        elif(ans=="use sword"):
            if "sword" in bag:
                print("Oak's words echoed: There's a time and place for everything.")
            else:
                print("You do not have a sword.")
        elif(ans=="use axe"):
            if "axe" in bag:
                print("Oak's words echoed: There's a time and place for everything.")
            else:
                print("You do not have an axe.")
        elif (ans=="w"):
            h1()
        elif (ans=="n"):
            print("You cannot move in that direction.")
        elif (ans=="s"):
            print("You cannot move in that direction.")
        elif (ans=="e"):
            print("You cannot move in that direction.")
        else:
            print("That is not a valid command. Type help for a list of valid commands.")

def br():
    ans="bru"
    print("You are now in the final room, there seem to be a boss in front of you. You can choose to fight it or to chicken out.")
    print("Do you want to fight the boss? (y/n): ")
    while(ans!="yeet"):
        ans=input()
        if (ans=="y"):
            print("Choose the weapon you want to fight with: ")
            while (ans!="kbye"):
                ans=input()
                if (ans=="sword"):
                    if ("sword" in bag):
                        fight()
                    else:
                        print("You don't have a sword.")
                elif (ans=="axe"):
                    if ("axe" in bag):
                        fight()
                    else:
                        print("You don't have an axe.")
                elif (ans=="candy bar"):
                    if ("candy bar" in bag):
                        print("You cannot go into battle with just a candy bar!")
                    else:
                        print("You don't have any candy.")
                elif (ans=="list"):
                    print(*wlist, sep=', ')
                else:
                    print("That is not a valid choice. Type list to see your choices")
        elif (ans=="n"):
            print("You walk back to the previous room.")
            h1()
        else:
            print("That is not a valid command. Enter y for yes and n for no.")

def fight():
    health0=100
    ans="bru"
    print("My mans looks hella mad, apparently someone called his mom gay.")
    print("HEY. Wasn't it you that was going around calling people's mom gay?")
    print("Lmao he's seen you and he's coming for you.")
    print(" ")
    print(" attack --> Attacks the opponent")
    print(" run --> You run like a bitch")

    while (health0>0):
        ans=input("What do you want to do? (attack/run)")
        if (ans=="attack"):
            if pu==1:
                dmg=random.randint(40,61)
            else:
                dmg=random.randint(20,51)
            if dmg>health0:
                dmg=health0
                health0=health0-dmg
                print("That attack did " + str(dmg)+" damage!")
            else:
                health0=health0-dmg
                print("That attack did " + str(dmg)+" damage!")
        elif (ans=="run"):
            print("You run away!")
            h1()
        else:
            print("That is not a valid command.")
    print("You killed the boss! Good job!")
    sys.exit()

r1()
