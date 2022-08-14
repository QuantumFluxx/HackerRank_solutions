import sys


n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    p_set = set()
    for c in s:
        p_set.add(c)
    print(len(p_set))