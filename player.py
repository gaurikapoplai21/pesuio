class Player():
    valid_locations = []
    def __init__(self):
        self.dead = False
        self.Virtue = 0
        self.bag = []
        self.position = "home"
    def move(self,dest):
        if dest in self.valid_locations:
            self.position = dest
            else:
            print("You cannot go there")
    def talk(self):     # this needs to be filled up with the valid command and so do the previous two functions
        return "continue"
    def pick(self,obj):
        if obj not in self.bag:
            bag.append(obj)
    
