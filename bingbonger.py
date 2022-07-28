import matplotlib.pyplot as plt
import pandas as pd

#create DataFrame
df1 = pd.DataFrame({'bus2001': [130],'bus2003': [130],'bus2001soc':[40],'bus2003soc':[20],'bus2001miles':[90],'bus2003miles':[99]})

#add first bar to plot
ax = df1.plot(kind="bar")

#add axis labels
ax.set_xlabel('1', fontsize=14)
ax.set_ylabel('kwh',fontsize=16)

# #define second y-axis 
ax2 = ax.twinx()
ax2.plot(ax.get_xticks(),
    df1[['bus2001soc','bus2003soc']].values)

# #add second y-axis label
ax2.set_ylabel('soc', fontsize=16)

#define third y-axis 
ax3 = ax.twinx()
ax3.plot(ax.get_xticks(),
    df1[['bus2001miles','bus2003miles']].values)

# #add third y-axis label
ax3.set_ylabel('miles', fontsize=16,)



plt.show()
