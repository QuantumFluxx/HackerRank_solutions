import sys

q = int(input())
best = None
for _ in range(q):
    s = input().strip()
    
    found = False
    for i in range(len(s)//2):
        a = s[:i+1]
        f = n = int(s[:i+1])
        while len(a) < len(s):
            n += 1
            a += str(n)
        if a == s:
            found = True
            print('YES',f)
            break
    if not found:
        print('NO')