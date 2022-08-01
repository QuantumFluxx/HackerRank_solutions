import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    num = 0
    for i in range(0,n):
        gum = 1
        for j in range(i+1,n):
            if ar[i] == None:
                continue
            if ar[i] == ar[j] and gum ==1:
                num = num + 1
                gum = gum + 1
                ar[j] = None
            
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()