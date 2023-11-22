from collections import Counter
import pandas as pd

with open("word_row.txt","r") as infile:
        word_list= infile.read().split()

wl=list(map(str.lower,word_list))
#print(wl)
ws = pd.Series(wl)
#print(ws)

zvuk=[ "а", "о", "у", "и", "і", "е"]
LV = []
for w in ws:
        #print(w)
        c=Counter(c for line in w for c in line if c in zvuk).total()
        #print(c)
        if c >= 3:
                LV.append(w)
#print(LV)            
with open('Vowels.txt', 'w') as fp:
    for item in LV:
        fp.write("%s\n" % item)
    print('Done')