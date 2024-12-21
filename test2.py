import json,random

# data = json.load(open("rain.json","r"))

# testing = []
# training = []

# for i in data:
#     if random.random() < 0.8:
#         training.append(i)
#     else:
#         testing.append(i)

# json.dump(training,open("training.json","w"))
# json.dump(testing,open("testing.json","w"))

print(len(json.load(open("testing.json","r"))))