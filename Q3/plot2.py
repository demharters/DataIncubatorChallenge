import pandas as pd
import matplotlib.pylab as plt
import numpy as np
import seaborn as sns

df_init = pd.read_csv('sampleSize2.csv', index_col = 0)
df_init.plot.box()

print 'Number of studies with sample size >1000'
print (df_init > 1000).sum()

print 'Number of studies with sample size >10000'
print (df_init > 10000).sum()

plt.ylim(0,1500)
plt.title('Distribution of sample sizes from 2000-2016\n(Studies over 1500 in size are not shown)')
plt.savefig("openTrials_sampleSizes.png", dpi=300)
#plt.show()
