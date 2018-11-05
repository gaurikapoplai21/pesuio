import player
import re
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
        player.move(dest)
    elif "go" in statement:
        dest = statement[statement.find("go")+1]
        player.move(dest)
    elif "pick" in statement:
        objects = item - set(statement)
        player.pick(item)
    elif "talk" in statement:
        player.talk()
    else:
        console("No, I don't understand that command, try again")
        show_help()

while not plas.dead: # this is the loop for the player when they are in the first part, before they enter the underworld
    alive=open("alive.txt", "r" )
    for x in alive:
        print(x.strip())

while plas.dead:    # this is the loop for the player once they are dead, this is the main loop when they can interact with the bot
    pass
with open('records','a') as record:
  record.write(plas.progress)
