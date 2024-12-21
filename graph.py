import json
# import matplotlib.pyplot as plt
import torch
device = torch.device('cuda')
data = json.load(open("data.json","r"))
rain = []

for i in data.keys():
    if data[i]["precip"] == "0":
        rain.append([1,float(data[i]["humidity"]),float(data[i]["sealevelpressure"]),0])
    else:
        rain.append([1,float(data[i]["humidity"]),float(data[i]["sealevelpressure"]),1])
        


# w = [0,0,0]
w = torch.zeros(3, device=device)
a = 0.01

for epoch in range(100):
    for t in rain: 
        y = t[-1]
        # print(t)
        x = torch.tensor(t[:-1], device=device)
        h = torch.dot(w, x) 
        error = y - (1 if h >= 0 else 0) 
        w += a * error * x # Update weights

# w=[0,0,0]
# for k in range(100):
#     for b, x1,x2,y in rain:
#         x = [b,x1,x2]
#         h =0
#         for j in range(0,3):
#             h+=w[j]*x[j]
#         er = y - (1 if h>=1 else 0)
#         for l in range(0,3):
#             w[l] = w[l] + a*er*x[l]
#         # print(w)
print(w)
# try:
#     print((w[0]/w[2])-(w[1]/w[2]))
# except:
#     pass