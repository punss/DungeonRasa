import random
import sys
import nlu_main as main
import nlu_movement as movement

availableRooms=[[0,0],[0,1],[1,1],[-1,1]]
restrictedRooms=[[0,2]]
playerPos=[0,0]
bag=[]
wl=[]
ans=''

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

def restrictedCondition(room):
    global bag
    global wl

    if room == [0,2]:

        if len(wl)>0:
            return True
        else:
            return False

def restrictedAccessDesc(room):
    if room == [0,2]:
        print("You don't have a weapon, you will not dare enter.")

def move(value):
    global playerPos
    global wl
    global availableRooms
    global restrictedRooms

    if value == 'north':
        goto= [playerPos[0], playerPos[1] + 1]
    
    elif value == 'south':
        goto= [playerPos[0], playerPos[1] - 1]
    
    elif value == 'east':
        goto= [playerPos[0] +1, playerPos[1] ]
    
    elif value == 'west':
        goto= [playerPos[0] -1, playerPos[1] ]


    if goto in restrictedRooms:
        if restrictedCondition(goto):
            playerPos = goto
            roomDescription(goto)
            return
        else:
            restrictedAccessDesc(goto)
            return
    
    elif goto in availableRooms:
        playerPos = goto
        roomDescription(goto)
        return
    else:
        cannotMove()
    
    



roomDescription(playerPos)

while(True):
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
            move('north')
        elif movement.run(resp['entities'][0]['value']) == 'South':
            move('south')
        elif movement.run(resp['entities'][0]['value']) == 'East':
            move('east')
        elif movement.run(resp['entities'][0]['value']) == 'West':
            move('west')
            
