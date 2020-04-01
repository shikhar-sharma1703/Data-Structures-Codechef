import math
source = int(input())
destination = int(input())
factor = -1
c = 0
if source == destination:
    c = 0
while source != destination:
    for i in range(int(math.sqrt(source)), source):
        if source % i == 0:
            factor = i
    source += factor
    c += 1
    if factor == -1:
        break
    difference = destination - source

    if source > destination:
        break

    print(source)
    print(c)




