import random
with open('RefinedData.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('RandomizedData.txt','w') as target:
    for _, line in data:
        target.write( line )
