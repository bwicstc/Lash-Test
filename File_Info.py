import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import more_itertools as mit
from tabulate import tabulate

# This function pulls part information from the original Excel file and stores
# it into a DataFrame to be used on the main script.

def File_Info(file):

# Extracts data from Excel file
#file = r'C:\Users\jxb21b\Desktop\Lash Test\Timed AQ_X.csv'
#information = pd.read_csv(file, skiprows = 1)

    df = pd.read_csv(file,header = None, skiprows=1)
    #df2 = pd.read_csv(file, header=None, skiprows=11)
    df_list = np.split(df, df[df.isnull().all(1)].index)
    #f_list2 = np.split(df2, df2[df2.isnull().all(1)].index)
#print(df_list)
    info = []
    #avg = []
    #force =[]
    for i in df_list[::1]: 
        df_list = df.astype('|S')
    
        if len(i) % 2 == 0:
        
            EWR = i[2:3][1]
            part_num = i[3:4][1]
            unit_num = i[4:5][1]
            date = i[1:2][9]
            date_time = date.to_string()[5:]
            EWR2 = EWR.to_string()[5:]
            part = part_num.to_string()[5:]
            unit = unit_num.to_string()[-4:]
            info.append([EWR2, part, unit, date_time])
        
        #print(unit[2:])

    return info[1:]
    
    

# Need to create for loop to loop through and title each plot correctly

    
    
    # else:
    #     i['Displacement'] = (i[4:][0])
    #     i['Force'] = (i[4:][1]).astype(float)
        
    #     i['Time'] = (i[4:][2]).astype(float)
    #     i['mean'] = i['Force'].rolling(3).mean()
        
    #     avg.append(i['mean'])
    #     force.append(i['Force'])
        



            
           


              
        

             
        # plt.plot(i['Time'],i['Force'], marker='*')
        # plt.axis([23.682,23.694,25,45])
        
        
        # plt.show()
        # plt.xlim(23.682, 23.694)
        # plt.ylim(25, 50)
        # for k in range(30, len(i['Force'])):
        #     if i['mean'][k] - i['mean'][k-1]<0 & (i['mean'][k-2] - i['mean'][(k-2)-1]>0).all():
        #          if i['Force'].any() > -200 and i['Force'].any() < 200 == True:
        #              print(k)
        # for k in range(10, len(i['Force'])):
        #     if i['mean'][k] - i['mean'][k-1]<0 & (i['mean'][k-2] - i['mean'][(k-2)-1]>0).all():
        #         if i['Force'].any() > -200 and i['Force'].any() < 200 == True:
        #             print(k)
                    
        #Special_Forces = i['Force'].any() > -200 and i['Force'].any() < 200 
       # i['mean'] = i['Force'].rolling(3).mean() 
        
        #print(i['Special Force'].head())
        #for k in 
       # if (i['mean'][k] - i['mean'][k-1]<0).all() & (i['mean'][k-2] - i['mean'][(k-2)-1]>0).all():
                        #bad.append(k)
                        #print(bad)
#         i['mean'] = i[1].rolling(3).mean()
#         i['Bad Force'] = i[1] > -200
#         i['Badder Force'] = i['Bad Force'] < 200

#         bad = []
#         for k in range(20, len(df['mean'])):
#             if (j['mean'][k] - j['mean'][k-1]<0).all() & (j['mean'][k-2] - j['mean'][(k-2)-1]>0).all():
#                 if (j['Bad Force']).any() == True & (j['Badder Force']).any() == True:
#                     bad.append(k)

# # Groups consecutive runs    
# groups = [list(group) for group in mit.consecutive_groups(bad)]
# print(len(groups))

# # If there are more than 16 groups, hook may be present.
# # Reasoning: 4 "decent" cycles, so there should be 8 turn arounds
# if len(groups) > 16:
#     print('Hook is present')
# else:
#     print("Hook may not be present")
# EWR = information.iloc[1,1]
# part_num = information.iloc[2,1]
# unit_num = information.iloc[3,1]
# date = information.iloc[0,9]


#print(tabulate(information))