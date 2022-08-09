s = input()
n = 1
while n * n < len(s):
    n += 1

a = s + ' ' * (n * n - len(s))
a = [a[i:i+n] for i in range(0, n * n, n)]

print(' '.join([''.join([a[j][i] for j in range(n)]).strip() for i in range(n)]))