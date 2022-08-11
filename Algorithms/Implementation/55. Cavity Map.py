n = int(input())
a = [list(input()) for _ in range(n)]

def getval(p, off):
    px = p[0] + off[0]
    py = p[1] + off[1]
    pi = a[px][py]
    return 10 if pi == 'X' else int(pi)

for i in range(1, n-1):
    for j in range(1, n-1):
        p = (i, j)
        if getval(p, (0, 0)) > max(getval(p, off) for off in (
            (0, 1), (0, -1), (-1, 0), (1, 0))):
            a[i][j] = 'X'
            
for row in a:
    print(''.join(row))