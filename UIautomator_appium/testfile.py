import time

print(time.time())

z = []
d = []
for x in range(3):
    for y in range(3):
        if x>0 or y >0:
            z =[x,y]
            d.append(z)

if len(d) > 5:
    for xy in range(len(d)):
        print(d[xy][0],d[xy][1])