import pandas as pd
import os

os.chdir('C:/Users/leejangw/AppData/Local/Programs/Python/Scripts/Nicole_Hospital') # to set a working directory
df_ref=pd.read_csv('Nicole_Hospital_16S_mapped_reads_and_sample_list_v1.csv',sep=',',skip_blank_lines=True,index_col=False)

ls_samples=df_ref['Seq_ID'].tolist()

for i in range(len(ls_samples)):
    df=pd.read_csv(ls_samples[i] + '.clean.deeparg.mapping.ARG_v2.csv',sep=',',skip_blank_lines=True,index_col=False)
    df['ARGper16S']=df['coverage']/(150*df_ref.loc[i,'#16S_reads']/1432)
    df.to_csv(ls_samples[i] + '.clean.deeparg.mapping.ARG_v3.csv',sep=',',index=False) # to merge two dataframes and finally generate a rpk-updated 16S dataframe

