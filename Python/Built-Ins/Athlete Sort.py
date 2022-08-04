import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    P=sorted(arr,key=lambda row:row[k])
    for i in range(len(P)):
        for j in range(len(P[i])):
            print(P[i][j], end=' ')
        print()