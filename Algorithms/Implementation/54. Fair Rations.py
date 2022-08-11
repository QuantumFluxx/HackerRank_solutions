import sys

def solve(b):
    if sum(b) % 2 == 1: return 'NO'
    tot = 0
    for i in range(len(b) - 1):
        if b[i] % 2 == 1:
            b[i] = b[i] + 1
            b[i+1] = b[i+1] + 1
            tot = tot + 2
    return tot



N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]
print(solve(B))