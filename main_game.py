import player
import re
import sys
plas = player.Player()

def console(statement):             # this will be the "console" for the player
    print(statement,"\n>")

def show_help():        # this is the help if the player is confused
    print("""
    valid commands are:
    1. move to some place or use go
    2. Pick up some object
    3. Talk to any of the on-screen characters
    """)

def talk_to_bot(statement):         # this is the only way the player can interact with the game once they die, they enter a command and it goes to the bot
    if "move" in statement:
        dest = statement[statement.find("move")+1]
        plas.move(dest)
    elif "go" in statement:
        dest = statement[statement.find("go")+1]
        plas.move(dest)
    elif "pick" in statement:
        objects = item - set(statement)
        player.pick(item)
    elif "talk" in statement:
        player.talk()
    else:
        console("No, I don't understand that command, try again")
        show_help()

print('Do you want to see the help section')
choice=input()
if 'y' in choice:
    show_help()

while not plas.dead: # this is the loop for the player when they are in the first part, before they enter the underworld
    alive=open("alive.txt", "r" )
    print(alive.read())
    alive.seek(0)
    plas.dead = True

print('\n\n\n')
print('You died but there still may be a way')
print('Want to checkout')
choice=input()
if 'y' in choice:
    with open('scene-1.txt','r') as scene:
        print(scene.read())
else:
    print('Thanks for playing, Your Dead')
    sys.exit()
    
print('\nCongratulations The lord of death has given you a second chance\n')

with open('scene-2.txt','r') as scene:
        print(scene.read())
print('\nDo you want to help the detective\n')
choice=input()
if 'y' in choice:
    with open('scene-3.txt','r') as scene:
        three = scene.readlines()
    for i in range(0,5):
        print(three[i])
    print('\nDo you want to help the tramp\n')
    choice=input()
    if 'y'in choice:
        for i in range(10,20):
            print(three[i])
        bag=100
    else:
        for i in range(22,30):
            print(three[i])
        bag=0
else:
    print('Without the detective there is no hope \nYou try to investigate on your own')
    print('But end up failing \nThe item is lost forever')
    print('GAME OVER!!')
    sys.exit()

with open('scene-4.txt','r') as scene:
    print()
    print(scene.read())
    print()

with open('scene-5.txt','r') as scene:
    five=scene.readlines()

print(five[0])
if bag==100:
    for i in range(2,4):
        print(five[i])
else:
    for i in range(6,8):
        print(five[i])
for i in range(10,18):
    print(five[i])
print('\nDo wish to move on??\n')
choice=input()
with open('scene-6.txt','r') as scene:
    six = scene.readlines()
if 'y' in choice:
    for i in range(4,8):
        print(six[i])
    if bag==100:
        print('\nYou only have two options in this case\n Ok or No\n')
        for i in range(20,24):
            choice=input()
            choice=choice.lower()
            if 'ok' in choice:
                print(six[i])
            else:
                print('You Dies \nGAME OVER!!')
                sys.exit()
    if bag==0:
        print('\nYou only have two options in this case\n Ok or No\n')
        for i in range(10,16):
            choice=input()
            choice=choice.lower()
            if 'ok' in choice:
                print(six[i])
            else:
                print('You Dies \nGAME OVER!!')
                sys.exit()

else:
    print('They find you along with the detective')
    print('Both of you get killed')     
    print('GAME OVER!!')
    sys.exit()
    
print('*The player goes to the palace and finally returns the object*\nTHE END')


'''with open('records.txt','a') as record:
  record.write(plas.progress)

#closing all files
alive.close()
record.close()'''