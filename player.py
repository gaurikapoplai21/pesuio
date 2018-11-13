class Player():
    valid_locations = ['home','Underworld','grim street','medical shop','Headquarters',]
    def __init__(self):
        self.dead = False
        self.Virtue = 0
        self.bag = set()
        self.position = "home"
    def move(self,dest):
        if dest in self.valid_locations:
            self.position = dest
        else:
            print("You cannot go there")
    def talk(self):     # this needs to be filled up with the valid command and so do the previous two functions
        return "continue"
    def pick(self,obj):
        self.bag.add(obj)
