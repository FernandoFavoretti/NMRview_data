
# coding: utf-8

# In[31]:

import pandas as pd
import re 
import numpy as np
import argparse


parser = argparse.ArgumentParser(description='KAPLA!')
parser.add_argument('-file', '--file', help='nome do arquivo xpk')
parser.add_argument('-names', '--names', help='nome do arquivo dicionario')
args = vars(parser.parse_args())


# In[32]:
print("Working in file:"+ str(args["file"]))

file_name = args["file"]
file_residues_names = args["names"]
with open(file_residues_names) as f:
    list_residues_names = f.read().splitlines()[1:]
    list_residues_names = ''.join(list_residues_names)
num_residuos = len(list_residues_names)


# In[33]:

df = pd.read_csv(file_name, sep=" ", skiprows=5)


# In[52]:

name = pd.read_csv(file_name, skiprows=1, nrows=1)


# In[34]:

df['peak'] = df.index


# In[35]:

df = df[["peak","HN.L", "vol","HN.P", "N15.P"]]


# In[36]:

def lockpick(line):
    try:
        return int(re.search(r'\d+', line).group())
    except:
        return line
    


# In[37]:

df["residue"] = map(lockpick, df["HN.L"])
df = df.drop(["HN.L"], axis=1)


# In[38]:

df = df.sort_values('residue')


# In[39]:

def add_lines_of_zeros(df, residue):
    line = [0 for x in range(1,df.shape[1])]
    line.append(residue)
    df.loc[len(df)] = line
    return df


# In[40]:

for i in range(1,num_residuos):
    if df.loc[df['residue'] == i].shape[0] == 0:
        df = add_lines_of_zeros(df, i)
        


# In[41]:

df = df.sort_values('residue')


# In[42]:

def get_name_residuos(residuo, string_names):
    try:
        return string_names[int(residuo-1)]
    except:
        return None


# In[43]:

df["aminoacids"] = df.apply(lambda k: get_name_residuos(k['residue'], list_residues_names), axis=1)


# In[47]:

df_final = df[['peak', 'aminoacids', 'residue', 'HN.P', 'N15.P', 'vol']]


# In[64]:

new_file = str(file_name[:-4])+'.csv'
df_final.to_csv(new_file, index=False)


# In[66]:

fd = open(new_file,'a')
fd.write(name.values[0][0])
fd.close()

