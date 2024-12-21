import json
import csv


dic = {}

files = ["weather.csv","weather2023.csv","weather2021-2022.csv","weather2019-2020.csv"]
for i in files:
    file = open(i)
    reader = list(csv.reader(file))

    head = reader[0][1::]
    for i in reader[1::]:
        temp = {}
        for j in head:
            temp[j] = i[head.index(j)+1]
        dic[i[0]] = temp
        
json.dump(dic,open("data.json","w"))


