import json

# file = open("data.json")

data = json.load(open("data.json","r"))
rain = []

for i in data.keys():
    if data[i]["precip"] == "0":
        rain.append([1,float(data[i]["humidity"]),float(data[i]["sealevelpressure"]),0])
    else:
        rain.append([1,float(data[i]["humidity"]),float(data[i]["sealevelpressure"]),1])
        

json.dump(rain,open("rain.json","w"))