import matplotlib.pyplot as plt
import pandas as pd

#create DataFrame
df1 = pd.DataFrame({'GoRTS - 2001 - Energy Used': [250],'GoRTS - 2003 - Energy Used': [214],'GoRTS - 2001 - SOC Used':[82],'GoRTS - 2003 - SOC Used':[64],'GoRTS - 2001 - Distance Driven':[93],'GoRTS - 2003 - Distance Driven':[90]})

#add first bar to plot
ax = df1.plot(kind="bar")

#x-axis delete
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

#sets tick and labels for initial y-axis
ax.set_yticks([0,40,80,120,160,200,240,280])
ax.set_yticklabels(['0 kWh','40 kWh','80 kWh','120 kWh','160 kWh','200 kWh','240 kWh','280 kWh']) 

# #define second y-axis 
ax2 = ax.twinx()
ax2.plot(ax.get_xticks(),
     df1[['GoRTS - 2001 - SOC Used','GoRTS - 2003 - SOC Used']].values)

#sets tick and labels for second y-axis
ax2.set_yticks([0,15,30,45,60,75,90,105])
ax2.set_yticklabels(['0%','15%','30%','45%','60%','75%','90%','105%']) 

#define third y-axis 
ax3 = ax.twinx()
ax3.plot(ax.get_xticks(),
    df1[['GoRTS - 2001 - Distance Driven','GoRTS - 2003 - Distance Driven']].values)

#aligns third y-axis due to overlapping
ax3.spines['right'].set_position(('outward',50))

#sets ticks and labels for third y-axis
ax3.set_yticks([0,15,30,45,60,75,90,105])
ax3.set_yticklabels(['0 mi','15 mi','30 mi','45 mi','60 mi','75 mi','90 mi','105 mi'])

#moves legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=3)

plt.show()
