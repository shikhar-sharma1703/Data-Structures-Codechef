import itertools
import math


def primes(a):
    a = int(a)
    isPrime = 1
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            isPrime = 0
    if a == 1 or a == 0:
        return False
    if isPrime == 1:
        return True
    else:
        return False


def smallestProduct(abc):
    result = list(itertools.permutations(abc))
    list1 = list(map(lambda x: ''.join(x), result))
    list2 = []
    smallestproduct = 99999999999999
    for permutation in list1:
        for i in range(1, len(permutation)+1):
            for j in range(i + 1, len(permutation)):
                a = permutation[:i]
                b = permutation[i:j]
                c = permutation[j:len(permutation)]
                if a[0] == '0' or b[0] == '0' or c[0] == '0':
                    continue
                if primes(a) and primes(b) and primes(c) and ((int(a) * int(b) * int(c)) < smallestproduct):
                    smallestproduct = int(a) * int(b) * int(c)
                    list2.clear()
                    list2.append(a)
                    list2.append(b)
                    list2.append(c)

    print(list2)


abc = input()
smallestProduct(abc)