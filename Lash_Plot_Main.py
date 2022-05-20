# Lash Test Plots
# James Burrier
# 05.13.2021


## The main purpose of this program is to plot lash data. There is also code 
## to distinguish between "good" and "bad" parts, but it was deemed that lash 
## was not adequate in distiguishing between the two.


# Imported libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import more_itertools as mit
from tabulate import tabulate
import File_Info
import New_Excel_Creator
import easygui
import os

#import magic
#import num_runs


# Extracts data from Excel file
#file = r'C:\Users\jxb21b\Desktop\Lash Test\Timed AQ_X.csv'
csv = easygui.fileopenbox("Select a file")
file = csv +'.csv'

plot_loc = os.path.abspath(easygui.filesavebox("Where do you want the plot to go?"))
info = File_Info.File_Info(file)
new_file = New_Excel_Creator.New_Excel(file)

#num = int(easygui.enterbox("How many parts were ran?"))
#new_file = New_Excel_Creator.New_Excel(file)

# Iterates through the Excel file created from the New_Excel_Creator function
# and plots each part run
num = len(new_file)
for k in range(num+2):
  df = pd.read_excel(new_file, sheet_name='Sheet{}'.format(k)) 

  plt.figure(k)
  plt.plot(df['Displacement'], df['Force'])
  plt.title(info[k-1])
  plt.xlabel('Displacement, mm')
  plt.ylabel('Force, N')
  plt.xlim(-2,2)
  plt.ylim(-600,600)
  plt.grid()
        #plt.show()
  plt.savefig(plot_loc + '{}.jpeg'.format(k))
  

# Everything below this is old code that I was too afraid to delete becuase
# anxiety.   
    
# Finds the rolling average over 3 data points
# This rolling average value may need to change, but 3 seems like a decent
# value at the moment.
    # df['mean'] = df['Force'].rolling(3).mean()

# Finds forces between -200N and 200N (area most frequented by hook)
    # df['Bad Force'] = df['Force'] > -200
    # df['Badder Force'] = df['Bad Force'] < 200


# Iterate through the rolling mean in search of negative values, 
# then picks out only those within -200N to 200N
# Note: If the mean force[x] - mean force[x-1] < 0 and mean force[x-2] - mean force[x-2]-1 > 0
    # bad = []
    # for i in range(20, len(df['mean'])):
    #     if (df['mean'][i] - df['mean'][i-1]<0).all() & (df['mean'][i-2] - df['mean'][(i-2)-1]>0).all():
    #         if (df['Bad Force']).any() == True & (df['Badder Force']).any() == True:
    #             bad.append(i)

# Groups consecutive runs    
    # groups = [list(group) for group in mit.consecutive_groups(bad)]
    # print(len(groups))

# If there are more than 16 groups, hook may be present.
# Reasoning: 4 "decent" cycles, so there should be 8 turn arounds
    # if len(groups) > 16:
    #     message = 'Hook is present'
    # else:
    #     message = "Hook may not be present"

#print(info)
# easygui.textbox(message)

# plt.plot(df['Displacement'], df['Force'])
# plt.title('Part 46, X Direction Lash')
# plt.xlabel('Displacement, mm')
# plt.ylabel('Force, N')
# plt.xlim(-2,2)
# plt.ylim(-600,600)
# plt.grid()
# plt.show()
