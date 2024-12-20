import pandas as pd
import os
import numpy as np
import ast

os.chdir('C:/Users/myjac/OneDrive - University of Calgary/Scripts/Nicole_Hospital') # to set a working directory

df_ref=pd.read_csv('features.gene.length',sep='\t',skip_blank_lines=True,index_col=False,header=None,names=["ref", "length"]) # to read a reference data where the lengths of reference genes are there
df_sample_list=pd.read_csv('Nicole_Hospital_16S_mapped_reads_and_sample_list_v1.csv',sep=',',skip_blank_lines=True,index_col=False) # to read the data for sample list (Seq_ID) & the corresponding the number of 16S reads (#16S_reads)
ls_samples=df_sample_list['Seq_ID'].tolist() # to assign a sample list to 'ls_samples'

### a look-up table for updating 'ref_length' & 'coverage'
for i in range(len(ls_samples)):
    ls_2=[] # an empty list where a calculated coverage ('coverage) for each gene (each row for #ARG_NEW2 column) will be saved

    df=pd.read_csv(ls_samples[i] + '.clean.deeparg.mapping.ARG',sep='\t',skip_blank_lines=True,index_col=False)
    df['#ARG_NEW']=df["best-hit"].str.split('|').str[2]
    df['#ARG_NEW2']=df['#ARG_NEW']+'|'+df['predicted_ARG-class']

    for j in range(len(df['best-hit'].tolist())):
        if df.loc[j,'best-hit'] in df_ref['ref'].tolist():
            num=np.where(df_ref['ref']==df.loc[j,'best-hit']) # to locate the row number in df_ref for each ARG-subtype of interest ('best-hit') 
            cov=1*150/df_ref.loc[num[0][0],'length'] # to calculate coverage (=copy) for each ARG read
            ls_2.append(cov)
        else:
            ls_2.append('NA')

    ### to merge two dataframes
    df_new_2=pd.DataFrame(ls_2,columns=['coverage']) # to convert 'coverage' list to a dataframe 
    df_merged=pd.concat([df,df_new_2],axis=1) # to merge those two dataframes into the mother data
    # df_merged.to_csv(ls_samples[i] + '.clean.deeparg.mapping.ARG_intermediate.csv',sep=',',index=False) # to generate an intermediate file (if you want to double-check!)

    ### to aggregate data matrix by group, and save it as an output file
    df_merged_2=df_merged.groupby(['#ARG_NEW2'],as_index=False).sum() # to aggregate (sum) coverage values by group (i.e., #ARG_NEW2)
    df_merged_2[['#ARG_NEW2','coverage']].to_csv(ls_samples[i] + '.clean.deeparg.mapping.ARG_v2.csv',sep=',',index=False) # to generate a intermediate dataframe (will be a feeder for the next workflow code)



