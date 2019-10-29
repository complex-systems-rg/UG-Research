from player import Player

class Cooperator(Player):
  def __init__(self, defectlevel, M):
    super().__init__("C", 1,M)