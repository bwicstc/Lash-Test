# Function used to create a separate Excel file to put separate runs in their
# respective sheets. This is at least a temporary solution to the problem of
# having all the runs on the same sheet, which messed up the data.



import pandas as pd
import numpy as np
import easygui
import num_runs


def New_Excel(file):
    #read_file = pd.read_excel(file)
    #df = read_file.to_csv(file+".csv", header=None)
    df = pd.read_csv(file, header=None)
    df_list = np.split(df, df[df.isnull().all(1)].index)
    # dict_of_df = {}
    
    # for i in df:
    #     rows = df[df.isnull().all(axis=1)==True].index.tolist()[0]
    #     num = df.loc[0:rows-1]
    #     print(num)   
    
    #nul_rows = list(df[df.isnull().all(1)].index)
    
    list_of_dataframes = []
    list2 =[]
    
    #global num
    num = num_runs.number_of_runs()
    # Uses user input to name new file
    new_file_name = easygui.enterbox("Name for the new file") + '.xls'
    
    # For loop, if statment to pull numerical data from original Excel sheet,
    # Loop iterates through and separates according to blank rows. For instance,
    # each header for a part is its own block as well as each set of data. So,
    # for instance, if you have 10 parts, there should be 20 blocks, alternating
    # between part information and part data. This loop skips odd blocks and only 
    # retrieves data from even blocks.
    
    for i in range(num*2+1):
        if i % 2 == 0:
            new_list = pd.DataFrame(df_list[i][5:])
        
            new_df = pd.DataFrame(data={'Displacement': new_list[0], 'Force':new_list[1], 'Time': new_list[2]})
            #new_df['Diplacement'] = new_list[0]
            #new_df['Force'] = new_list[1]
            #new_df['Time'] = new_list[2]
            list2.append(new_df)
            
    df_new = {}
    # This part of code writes the even blocks of data to the new Excel sheets.
    writer = pd.ExcelWriter(new_file_name, engine='xlsxwriter')
    for j in range(num+1):
       globals()["df{}".format(j)] = list2[j]
       list2[j].to_excel(writer, sheet_name='Sheet{}'.format(j)) 
    writer.save()
    
    return new_file_name

    # for i in range(len(df_list)):
    #     if i % 2 == 0:
    #        # writer = pd.ExcelWriter('name.xlsx', engine='xlsxwriter')
    #         list_of_dataframes.append(df_list[2])
    #         #return list_of_dataframes
    # print(list_of_dataframes)
            #print(list_of_dataframes)
            #list2 = (list_of_dataframes)
            #list2.rename['Displacement', 'Force','Time']
           
                
                   
            
            
            
    
    #for j in range(len(r))
    #for j in range(len(list_of_dataframes)):
        
        
        
#New_Excel(r'C:\Users\jxb21b\Desktop\Lash Test\Timed AQ_X.csv')