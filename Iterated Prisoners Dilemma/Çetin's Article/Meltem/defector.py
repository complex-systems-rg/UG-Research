from player import Player

class Defector(Player):
  def __init__(self, defectlevel, M):
    super().__init__("D", 1, M)