# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/s10-quartiles/problem
# Difficulty: Easy
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

def getMedian(ar):
    ar.sort()
    mid=len(ar)//2
    if len(ar)%2 != 0:
        return ar[mid]
    else:
        return (ar[mid] + ar[mid-1])/2

def quartiles(arr):
    q2 = getMedian(arr)
    n = len(arr)
    mid = len(arr)//2
    start=0
    if n % 2 != 0:
        q1 = getMedian(arr[0:mid])
        q3 = getMedian(arr[mid+1:n])
    else:
        q1 = getMedian(arr[0:mid])
        q3 = getMedian(arr[mid:n])
    return [int(x) for x in [q1,q2,q3]]