import math
import csv
with open("data.csv",newline="") as f :
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data :
        total += int(i)
    mean = total/n
    return mean

squared_list = []
for x in data :
    a = int(x) - mean(data)
    a = a**2
    squared_list.append(a)
sum = 0
for a in squared_list :
    sum += a
result = sum/(len(data)-1)
std = math.sqrt(result)
print("Standard Deviation is " , str(std))