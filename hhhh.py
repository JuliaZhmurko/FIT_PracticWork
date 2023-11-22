import csv
countries={"Brazil":"8510000",
           "Peru":"1285000",
           "Chile":"756626",
           "Venezuela":"916445",
           "Uruguay":"176215",
           "Paraguay":"406752",
           "Argentina":"2780000",
           "Colombia":"1142000"}
def csv_dict_writer(path, fieldnames, data):
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
if __name__ == "__main__":
    data=countries
list1=[]
fieldnames=data[0]
for values in data[1:]:
    inner_dict=dict(zip(fieldnames,values))
    list1.append(inner_dict)
path="countries1.csv"
csv_dict_writer(path,fieldnames,list1)
   
