import pandas as pd
import os

os.chdir('C:/Users/myjac/OneDrive - University of Calgary/Scripts/Nicole_Hospital') # to set a working directory

df=pd.read_csv('Nicole_Hospital_deepARG_GP16S.v2.csv',sep=',',skip_blank_lines=True,index_col=None) # to read-in an data input file

df_new=df.groupby(['subtype|type'],as_index=False).sum() # to aggregate rows by classification (i.e., subtype|type)
df_new.to_csv('Nicole_Hospital_deepARG_GP16S.v3.csv',sep=',',index=False) # to save the "aggregated" results by 'subtype|type'

