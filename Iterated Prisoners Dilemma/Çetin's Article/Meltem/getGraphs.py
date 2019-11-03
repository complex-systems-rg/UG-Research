from random import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys

table = pd.read_csv(sys.argv[1])

#table.drop(sys.argv[2], axis=1, inplace=True)
#table.drop(sys.argv[3], axis=1, inplace=True)

phase_1_2 = table.groupby(['mu', 'ro']).mean()
phase_1_2 = phase_1_2.reset_index()
table = phase_1_2

data_table = pd.DataFrame(table)    
plt.figure(figsize=(50,50))
pivot_table = data_table.pivot('ro','mu','avgpayoffofc')
plt.xlabel('mu', size = 15)
plt.ylabel('ro', size = 15)
plt.title('avgpayoffofc', size = 15)
sns.heatmap(pivot_table, annot=True, fmt=".1f", linewidths=.5, square = True, cmap = 'Blues_r')

plt.show()