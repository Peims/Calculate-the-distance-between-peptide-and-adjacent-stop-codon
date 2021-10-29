import os
os.chdir(r"H:\工作盘\NCP2\图\图3\d")

import pandas as pd
file1=pd.read_csv("mRNA_location",sep="\t", header=0)
file1.sort_values(by=['chr','start'],ascending=[True,True],inplace=True)


file2=pd.read_csv("cpsweizi",sep="\t", header=0)
file2.sort_values(by=['chr','start'],ascending=[True,True],inplace=True)

dic1={}

for i in range(len(file1)):
    if file1.iloc[i,0] not in dic1:
        dic1.setdefault(file1.iloc[i,0],[])
    dic1[file1.iloc[i,0]].append(file1.iloc[i,1])

dic2={}
for i in range(len(file2)):
    
    chr=file2.iloc[i,0]
    start=file2.iloc[i,1]
    if chr in dic1:
        dic2.setdefault(chr,[])
        temp=[]
        for i in dic1[chr]:
            temp.append(i-start)
        dic2[chr].append(min([abs(i) for i in temp]))
    
with open("cp_TSS","w") as fout:
    for i in dic2.values():
        for j in i:
            fout.write(str(j)+"\n")