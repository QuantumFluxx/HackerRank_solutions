from sys import exit
from math import floor
n, k = map(int, input().split())
num = list(input().strip())
unpaired = len(list(filter(lambda x: x[0] != x[1], zip(num[:int(floor(n / 2))], reversed(num)))))
if unpaired > k:
    print(-1)
    exit()
for i in range(int(floor(n / 2))):
    if unpaired < k and k >= 2:
        if num[i] != num[n - 1 - i]:
            unpaired -= 1
        if num[i] != '9':
            k -= 1
        if num[n - 1 - i] != '9':
            k -= 1
        num[i] = num[n - 1 - i] = '9'
        continue
    if num[i] == num[n - 1 - i]:
        continue
    k -= 1
    if k < 0:
        break
    num[i] = max(num[i], num[n - 1 - i])
    num[n - 1 - i] = num[i]
if k > 0 and n % 2 == 1:
    num[int(floor(n / 2))] = '9'
print(-1 if k < 0 else ''.join(num))