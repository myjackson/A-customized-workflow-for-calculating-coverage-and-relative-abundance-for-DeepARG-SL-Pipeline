import pandas as pd
import os
import numpy as np
import ast

os.chdir('C:/Users/myjac/OneDrive - University of Calgary/Scripts/Nicole_Hospital') # to set a working directory

df_ref=pd.read_csv('features.gene.length',sep='\t',skip_blank_lines=True,index_col=False,header=None,names=["ref", "length"])
df_sample_list=pd.read_csv('Nicole_Hospital_16S_mapped_reads_and_sample_list_v1.csv',sep=',',skip_blank_lines=True,index_col=False)
ls_samples=df_sample_list['Seq_ID'].tolist()

ls=[] # an empty list - for updating index-id (sample name (M17) + geneid (LNUD), e.g. 'M17_LNUD')

### to produce an index column dataframe (consolidating the index of whole samples)
for i in range(len(ls_samples)):
    df=pd.read_csv(ls_samples[i] + '.clean.deeparg.mapping.ARG_v3.csv',sep=',',skip_blank_lines=True,index_col=None)
    df['idx']=df['#ARG_NEW2']+';'+ls_samples[i]
    df.to_csv(ls_samples[i] + '.clean.deeparg.mapping.ARG_v4.csv',sep=',',index=False)
    df=pd.read_csv(ls_samples[i] + '.clean.deeparg.mapping.ARG_v4.csv',sep=',',skip_blank_lines=True,index_col=None)
    idx=df['idx'].tolist()
    ls.extend(idx)
ls_idx=pd.DataFrame(ls,columns=['idx']) # index dataframe

for j in ls_samples:
    df_new=pd.read_csv(j + '.clean.deeparg.mapping.ARG_v4.csv',sep=',',skip_blank_lines=True,index_col=None) # a reference dataframe 
    ls_idx[j]=0 # to add a column for each sample to the index dataframe (ls_idx)
    for k in range(len(ls_idx['idx'])):
        obj=ls_idx['idx'][k] # to designate obj as a index value
        if obj in df_new['idx'].tolist():
            num=np.where(df_new['idx']==obj) # to locate the index value from a reference dataframe
            ls_idx.loc[k,j]=df_new['ARGper16S'][num[0][0]]
        else:
            pass

ls_idx.to_csv('Nicole_Hospital_deepARG_GP16S.v1.csv',sep=',',index=False)
