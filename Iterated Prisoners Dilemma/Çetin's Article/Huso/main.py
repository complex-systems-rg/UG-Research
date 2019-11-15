from cooperator import Cooperator
from defector import Defector
import random
import numpy as np
from itertools import combinations

def play(Player1, Player2, R,P,S,T,forgetType):
    if Player1.type == "C" and Player2.type == "C":
        #print("CC")
        Player1.score += R
        Player2.score += R
    elif Player1.type == "C" and Player2.type == "D":
        #print("CD")

        Player1.score += S
        Player2.score += T
    elif Player1.type == "D" and Player2.type == "C":
        #print("DC")

        Player1.score += T
        Player2.score += S
    elif Player1.type == "D" and Player2.type == "D":
        # print("DD")

        Player1.score += P
        Player2.score += P
    Player1.save(Player2,forgetType)
    Player2.save(Player1,forgetType)

def decideToPlay(Player1, Player2):
    if id(Player2) in Player1.memory.keys() and Player1.memory[id(Player2)]=="D":
        return False
    elif id(Player1) in Player2.memory.keys() and Player2.memory[id(Player1)]=="D":
        return False
    else:
        return True

def GAME(N, M, D, P, R, S, T,repet,forgetType):
    playerList = []
    pOfC = 0
    pOfD = 0
    for i in range(D):
        playerList.append(Defector(M))
    for k in range(N-D):
        playerList.append(Cooperator(M))

    for ri in range(repet):
        comb = combinations(playerList, 2)
        comb = list(comb)
        random.shuffle(comb)
        for match in comb:
            #if match[0].type=="C" and match[1].type=="D":
            if decideToPlay(match[0],match[1]):
                play(match[0],match[1], R,P,S,T,forgetType)
    
    for P in playerList:
        if P.type == "C":
            pOfC = pOfC + P.score
        else:
            pOfD = pOfD + P.score


    if N-D != 0:
        pOfC = pOfC / (N-D)
    else:
        pOfC = 0
    if D != 0:
        pOfD = pOfD / (D)
    else:
        pOfD = 0

    game_stats.append([(M/N), (D/N), pOfC, pOfD, (pOfC-pOfD)])


#### MAIN

gameStatistics = []

forgetType = "coop"
N = 100
M = 50
D= 80
R = 3
S =0
T=5
P=1
repet = 2

for x in range(10,100,10):
    for y in range(10,100,10):
        game_stats = []
        M = x
        D = y
        for i in range(10):
            #This for loop creates multiple datasets for better quality of datas.
            GAME(N, M, D, P, R, S, T,repet, forgetType)
        temp = np.array(game_stats)
        mean_arr = np.mean(temp, axis=0)
        gameStatistics.append(mean_arr)


    
    
arr = np.array(gameStatistics)
np.savetxt("simulation.csv", arr, delimiter=",")
