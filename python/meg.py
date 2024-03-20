import numpy as np
data = [64,90,45]

sorted_data =sorted(data)

indexes = [0,0,0]
count=0;
for i in sorted_data:
    indexes[count] = data.index(i)
    count = count+1
    
print(indexes)
print(data)
print(sorted_data)