import pandas as pd
from numpy import *
import csv
fname='input.csv'
df=pd.read_csv(fname,sep=';', encoding='cp1251')
print(df)
listName=[]
sum=0
listName=(df.iloc[0:0,0:3])
for n in listName:
    #print(n)
    for i in df[n]:
        #print(i)
        sum+=i
    print(n,sum)
    

