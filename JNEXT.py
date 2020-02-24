from itertools import permutations
for i in range(int(input())):
    n = int(input())
    numl = input().split()
    p = permutations(numl)
    p1=0
    num = "".join(numl)
    p2 = "".join(p.__next__())
    while(int(p2)>=int(num)):
        p2 = "".join(p.__next__())
    print(p2)





