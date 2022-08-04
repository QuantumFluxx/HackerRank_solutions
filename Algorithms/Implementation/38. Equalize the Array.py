import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    return (len(arr) - arr.count(max(set(arr), key = arr.count)))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()