class Player:
  def __init__(self, type, defectlevel, M):
    self.type = type
    self.score = 0
    self.attention = M
    self.memory = {}
    self.memoryFull = False
    self.M = M

  def save(self, Played):
    if id(Played) in self.memory.keys():
      return
    elif (self.memoryFull)==False:
      self.memory[id(Played)] = Played.type
      if(len(self.memory) == self.M):
            memoryFull = True
    elif Played.type == "D": #and memory is full
      for key, value in self.memory:
        if value == "C":
          self.memory.pop(key)
          self.memory[id(Played)] = Played.type
          break
    

