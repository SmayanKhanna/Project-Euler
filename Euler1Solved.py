#Solved in 5 minutes

import math

li1 = []

li2 = []

li3 = []

for x in range(1,1000):
    if x % 3 ==0 and x% 5 ==0:
        li1.append(x)

for y in range(1,1000):
    if y % 3 ==0:
        li2.append(y)

for z in range(1,1000):
    if z % 5 ==0:
        li3.append(z)


Sol = (sum(li3) + sum(li2)) - sum(li1)

print(Sol)
