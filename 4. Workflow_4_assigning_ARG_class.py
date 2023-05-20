import pandas as pd
import numpy as np
import os

os.chdir('C:/Users/myjac/OneDrive - University of Calgary/Scripts/Nicole_Hospital') # to set a working directory

df_ref=pd.read_csv('features.gene.length',sep='\t',skip_blank_lines=True,index_col=False,header=None,names=["ref", "length"])
df_sample_list=pd.read_csv('Nicole_Hospital_16S_mapped_reads_and_sample_list_v1.csv',sep=',',skip_blank_lines=True,index_col=False)
ls_samples=df_sample_list['Seq_ID'].tolist() # to assign a sample list to 'ls_samples'

### to create two empty lists for updating classification information of ARGs
ls_1=[] # an empty list where 'antibiotic subtype' will be updated

### to produce two columns of interest ('subtype|type')
for i in range(len(ls_samples)):
    df=pd.read_csv(ls_samples[i]+'.clean.deeparg.mapping.ARG_v3.csv',sep=',',skip_blank_lines=True,index_col=None)
    class_1=df['#ARG_NEW2'].tolist()
    ls_1.extend(class_1)
ls_class=pd.DataFrame(ls_1,columns=['subtype|type'])

### to add one column of interest to the specific location in the dataframe
df_new=pd.read_csv('Nicole_Hospital_deepARG_GP16S.v1.csv',sep=',',skip_blank_lines=True,index_col=None)
df_new.insert(1,'subtype|type',ls_class['subtype|type']) 

### to save the final dataframe as "v2.csv"
df_new.to_csv('Nicole_Hospital_deepARG_GP16S.v2.csv',sep=',',index=False)

