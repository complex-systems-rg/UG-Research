from cooperator import Cooperator
from defector import Defector
import random

gameStatistics = []
playerList = []

def play(Player1, Player2, R,P,S,T):
  if Player1.type == "C" and Player2.type == "C":
    Player1.score =+ R
    Player2.score =+ R
  elif Player1.type == "C" and Player2.type == "D":
    Player1.score =+ S
    Player2.score =+ T
  elif Player1.type == "D" and Player2.type == "C":
    Player1.score =+ T
    Player2.score =+ S   
  elif Player1.type == "D" and Player2.type == "D":
    Player1.score =+ P
    Player2.score =+ P
  Player1.save(Player2)
  Player2.save(Player1)

def decideToPlay(Player1, Player2):
  if id(Player2) in Player1.memory.keys() and Player1.memory[id(Player2)]=="D":
    return False
  elif id(Player1) in Player2.memory.keys() and Player2.memory[id(Player1)]=="D":
    return False
  else:
    return True

def GAME(N, M, D, P, R, S, T,repet):
  pOfC = 0
  pOfD = 0
  for i in range(D):
    playerList.append(Defector(M))
  for k in range(N-D):
    playerList.append(Cooperator(M))
  for ri in range(repet):
    random.shuffle(playerList)
    for j in range(0,len(playerList),2):
      if(decideToPlay(playerList[j],playerList[j+1])):
        play(playerList[j],playerList[j+1], R,P,S,T)
  for P in playerList:
    if P.type == "C":
      pOfC =+ P.score
    else:
      pOfD =+ P.score
  pOfC = pOfC / (N-D)
  pOfD = pOfD / (D)
  gameStatistics.append([(M/N), (D/N), pOfC, pOfD, (pOfC-pOfD)])

N = 100
M = 50
D=50
R = 3
S =0
T=5
P=1
repet = 20

GAME(N, M, D, P, R, S, T,repet)
print(gameStatistics)

