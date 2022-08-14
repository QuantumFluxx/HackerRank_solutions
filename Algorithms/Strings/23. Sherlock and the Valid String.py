import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    d = Counter(s)
    counts = Counter(d.values())
    if len(counts) == 1:
        return "YES"
    elif len(counts) > 2:
        return "NO"
    else:
        max_v = max(counts.values())
        k1, k2 = counts.keys()
        if (max_v == len(d) - 1):
            if (abs(k1 - k2) == 1):
                return "YES"
            elif (min(k1, k2) == 1):
                if counts[1] == 1:
                    return "YES"
                else:
                    return "NO"
            else:
                return "NO"
        else:
            return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()