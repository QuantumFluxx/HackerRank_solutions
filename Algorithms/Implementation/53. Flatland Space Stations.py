import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c.sort()
maxgap = max(a-b for a, b in zip(c[1:], c)) if len(c) > 1 else 0
ans = max(maxgap//2, c[0], n-1-c[-1])
print(ans)