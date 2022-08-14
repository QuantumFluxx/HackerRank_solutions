import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from math import factorial

fact = dict()
powr = dict()
dist = defaultdict(lambda : Counter(""))

m = 10 ** 9 + 7

def initialize(s):
    fact[0], powr[0], dist[0] = 1, 1, Counter(s[0])
    for j in range(1, len(s)):
        fact[j] = (j * fact[j - 1]) % m
        dist[j] = dist[j-1] + Counter(s[j])

def power(x, n, m):
    if n == 1:
        return x % m
    elif n % 2 == 0:
        return power(x ** 2 % m, n // 2, m)
    else:
        return (x * power(x ** 2 % m, (n - 1) // 2, m)) % m


def answerQuery(s, l, r):
    # Return the answer for this query modulo 1000000007.
    b = dist[r-1] - dist[l-2]
    p, count, value = 0, 0, 1
    for c in b.values():
        if c >= 2:
            count += c // 2
            value = (value * fact[c // 2]) % m
        if c % 2 == 1:
            p += 1
    return (max(1, p) * fact[count] * power(value, m - 2, m)) % m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)
    
    print(dist)
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(s,l, r)

        fptr.write(str(result) + '\n')

    fptr.close()