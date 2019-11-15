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

    def save(self, Played, forgetType):
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

        elif (self.memoryFull==1):
            if self.attention == 0:
                #no save option for fishes.
                return
        
            random.shuffle(list(self.memory.keys()))
            id_list = list(self.memory.keys())
            if forgetType == "rand":
                self.memory.pop(id_list[0])
                self.memory[id(Played)] = Played.type

            elif forgetType == "coop":
                for idd in id_list:
                    if self.memory[idd] == "C":
                        self.memory.pop(idd)
                        self.memory[id(Played)]=Played.type
                        break

            elif forgetType == "def":
                for idd in id_list:
                    if self.memory[idd] == "D":
                        self.memory.pop(idd)
                        self.memory[id(Played)]=Played.type
                        break

            elif forgetType == "maj":
                if D > (N-D):
                    maj = "D"
                else:
                    maj = "C"

                for idd in id_list:
                    if self.memory[idd] == maj:
                        self.memory.pop(idd)
                        self.memory[id(Played)]=Played.type
                        break

            elif forgetType == "eqpos":
                eqpos = random.choice(["C","D"])
                for idd in id_list:
                    if self.memory[idd] == eqpos:
                        self.memory.pop(idd)
                        self.memory[id(Played)]=Played.type
                        break





