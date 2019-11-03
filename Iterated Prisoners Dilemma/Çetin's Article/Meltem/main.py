from cooperator import Cooperator
from defector import Defector
from itertools import combinations 
import random
import sys
import pandas as pd

gameStatistics = {'mu':[], 'ro':[],'avg payoff of c':[],'avg payoff of d':[],'remainder':[] }

playerList = []

def play(Player1, Player2, R,P,S,T):
  if Player1.type == "C" and Player2.type == "C":
    Player1.score += R
    Player2.score += R
  elif Player1.type == "C" and Player2.type == "D":
    Player1.score += S
    Player2.score += T
  elif Player1.type == "D" and Player2.type == "C":
    Player1.score += T
    Player2.score += S   
  elif Player1.type == "D" and Player2.type == "D":
    Player1.score += P
    Player2.score += P
  Player1.save(Player2)
  Player2.save(Player1)

def decideToPlay(Player1, Player2):
  if id(Player2) in Player1.memory.keys() and Player1.memory[id(Player2)]=="D":
    return False
  elif id(Player1) in Player2.memory.keys() and Player2.memory[id(Player1)]=="D":
    return False
  else:
    return True

def GAME(N, M, D, P, R, S, T,ti):
  playerList = []
  pOfC = 0
  pOfD = 0
  for i in range(D):
    playerList.append(Defector(1,M))
  for k in range(N-D):
    playerList.append(Cooperator(1,M))
  for ri in range(ti):
    comb = combinations(playerList, 2)
    comb = list(comb)
    random.shuffle(comb)
    for pair in list(comb):
      if(decideToPlay(pair[0],pair[1])):
        play(pair[0],pair[1], R,P,S,T)
  for P in playerList:
    if P.type == "C":
      pOfC += P.score
    else:
      pOfD += P.score
  pOfC = pOfC / (N-D)
  pOfD = pOfD / (D)
  gameStatistics["mu"].append(round((M/N),3))
  gameStatistics["ro"].append(round((D/N),3))
  gameStatistics["avg payoff of c"].append(round(pOfC,3))
  gameStatistics["avg payoff of d"].append(round(pOfD,3))
  gameStatistics["remainder"].append(round((pOfC-pOfD),3))

N,R,S,T,P,ti = 100,3,0,5,1,2

for M in range(10, 100, 10):
  for D in range(10, 100, 10):
    for i in range(20):
      GAME(N, M, D, P, R, S, T,ti)
  print("M is " + str(M))

gameStatistics =  pd.DataFrame.from_dict(gameStatistics)
gameStatistics.to_csv("experiment.csv")

