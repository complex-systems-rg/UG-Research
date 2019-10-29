from random import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys

table = pd.read_csv(sys.argv[1])

table.drop(sys.argv[2], axis=1, inplace=True)
table.drop(sys.argv[3], axis=1, inplace=True)

data_table = pd.DataFrame(table)    
plt.figure(figsize=(50,50))
pivot_table = data_table.pivot('mu','ro',sys.argv[2])
plt.xlabel('ro', size = 15)
plt.ylabel('mu', size = 15)
plt.title(sys.argv[2], size = 15)
sns.heatmap(pivot_table, annot=True, fmt=".1f", linewidths=.5, square = True, cmap = 'Blues_r')

plt.show()