class Player():
    def __init__(self):
        self.dead = False
        self.Virtue = 0
        self.bag = []
        self.position = "home"
    def move(self,dest):
        self.positon = dest
    def talk(self):     # this needs to be filled up with the valid command and so do the previous two functions
        return "continue"
    def pick(self,obj):
        if obj not in self.bag:
            bag.append(obj)
    
