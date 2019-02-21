import random
import sys
import nlu_main as main
import nlu_movement as movement


def help():
    print('''
    __HELP__
    Take an item
    Use an item
    Access their bag
    Move in any direction (North/South/East/West)
    Ask for help
    Look around them
    Exit the game at any time
    ''')

def cannotMove():
    print("You cannot move in that direction.")

def doesntExist():
    print("That object doesn't exist")

def roomDescription(room):
    if room==[0,0]:
        print("You are in a dimly lit room. There is a door towards the north. There is a key on the floor.")
    if room == [0,1]:
        print("You are now in a hallway. There are 4 doors around you. There are scary noises coming from the door in front of you.")
    if room == [1,1]:
        print("You are now in a room with a huge window with a sexy view. There is a shelf with a jar on it. The rest of the room is empty.")
    if room == [-1,1]:
        print("You are now in what looks like a weapons room. There are swords and axes.\nThere's also an err, candy bar on the floor.")

def move(value):
    pass

availableRooms=[[0,0],[0,1],[1,1],[-1,1],[0,2]]
playerPos=[0,0]
bag=[]
wl=[]
ans=''

while(True):
    ans=input()
    ans=input()
    resp=main.run(ans)
    if resp['intent']['name'] == 'get':
        if resp['entities'][0]['value'] == 'key':
            bag.append("key")
            print("You picked the key up.")
        else:
            doesntExist()

    elif resp['intent']['name'] == 'move':
        if movement.run(resp['entities'][0]['value']) == 'North':
            if [playerPos[0], playerPos[1] + 1] in availableRooms:
                if [playerPos[0], playerPos[1] + 1] == [0,2] and len(wl)>0:
                    playerPos[1] +=1
                else:
                    print("You don't have a weapon, you will not dare enter.")
            else:
                cannotMove()
        else:
            cannotMove()
'''
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }

    return switcher.get(argument, "nothing")

if __name__ == "__main__":
    argument=0
    print numbers_to_strings(argument)



def week(i):
        switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
         return switcher.get(i,"Invalid day of week")'''
