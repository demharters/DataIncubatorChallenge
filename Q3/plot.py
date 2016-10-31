import pandas as pd
import matplotlib.pylab as plt
import numpy as np

df_init = pd.read_csv('conditionCounts4.csv', index_col = 0)
grouped = df_init.groupby('name', axis=0, as_index=False)
df = pd.DataFrame()
for group in grouped.groups.keys():
     df = pd.concat([df,grouped.get_group(group)])

fig, axes = plt.subplots(4,4)

j = 1
for i in range(2001,2017):
    myData = df.where(df['year'] == i).sort_values('counts').dropna()
    ax = plt.subplot(4,4,j)
    plt.bar(np.arange(20),myData['counts'], align='center')
    plt.xticks(np.arange(20),rotation='vertical')
    ax.yaxis.set_ticks(np.arange(0, 150, 50))
    #ax.set_xticklabels(df['name'].where(df['year'] == i).dropna(), fontsize = 8)
    ax.set_xticklabels(myData['name'].str[:14], fontsize = 6)
    plt.ylim(0,150)
    plt.xlim(0,21)
    plt.title(i)
    j += 1

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=2)

plt.savefig("openTrials_conditionCounts.png", dpi=300)
#plt.show()
