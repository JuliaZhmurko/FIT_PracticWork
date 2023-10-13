from collections import OrderedDict
print("Input 2 rows")
s1=input()
s2=input()

out_s = ""
s1 = OrderedDict.fromkeys(s1).keys()

for i in s1:
    
    n = s2.find(i)
    if n>=0:
        out_s+=i
   
print("Кількість унікальних символв що присутні в обох рядках = %i , такі символи : %s" %(len(out_s),out_s))sff