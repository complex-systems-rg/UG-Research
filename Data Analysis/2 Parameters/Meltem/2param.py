from random import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



def f(x,y):
    return x*x - x*y + 5*y*y*x + 7*y*y + 21

def error():
    return random()*24-12

def experiment(repet):
    table = {'x':[], 'y':[], 'f(x,y)':[]} 
    for i in np.arange(0, 1, 0.05):
        for j in np.arange(0,1.0, 0.05):
            sum = 0
            for _ in range(repet):
                sum += f(i,j) + error()
            mean = sum/repet
            table['x'].append(round(i,2))
            table['y'].append(round(j,2))
            table['f(x,y)'].append(round(mean,2))
    return pd.DataFrame(table)

def actual():
    table = {'x':[], 'y':[], 'f(x,y)':[]} 
    for i in np.arange(0, 1, 0.05):
        for j in np.arange(0,1.0, 0.05):
            sum = 0
            table['x'].append(round(i,2))
            table['y'].append(round(j,2))
            table['f(x,y)'].append(round(f(i,j),2))
    return pd.DataFrame(table)    

data_table = experiment(200)
plt.figure(figsize=(50,50))
pivot_table = data_table.pivot('x','y','f(x,y)')
plt.xlabel('y', size = 15)
plt.ylabel('x', size = 15)
plt.title('my heatmap', size = 15)
sns.heatmap(pivot_table, annot=True, fmt=".1f", linewidths=.5, square = True, cmap = 'Blues_r')

actual_table = actual()
plt.figure(figsize=(50,50))
pivot_table2 = actual_table.pivot('x','y','f(x,y)')
plt.xlabel('y', size = 15)
plt.ylabel('x', size = 15)
plt.title('true values', size = 15)
sns.heatmap(pivot_table2, annot=True, fmt=".1f", linewidths=.5, square = True, cmap = 'Blues_r')
plt.show()