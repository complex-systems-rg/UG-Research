import random

class Player:
    def __init__(self, type, M):
        self.type = type
        self.score = 0
        self.attention = M
        self.memory = {}
        if M != 0:
            self.memoryFull = 0
        else:
            self.memoryFull = 1

    def save(self, Played):
        if id(Played) in self.memory.keys():
            #print("Already played with the player " + str(id(Played)))
            return
        elif (self.memoryFull)==0:
            
            #print("Player is added to the memory " + str(id(Played)))
            self.memory[id(Played)] = Played.type
            #now memory might become full.
            if len(self.memory)==self.attention:
                #print("Memory is full")
                self.memoryFull=1

        #Forgetting Mechanisms
        #Memory is full, we need to add additional information.
        elif (self.memoryFull==1):
            if self.attention == 0:
                #no save option for fishes.
                return
            
            #random forgetting.
            #print("Forgetting is started")
            key = random.choice(list(self.memory.keys()))
            self.memory.pop(key)
            self.memory[id(Played)] = Played.type
    

