from collections import defaultdict

n, k = [int(item) for item in input().strip().split()]
S = [int(item) for item in input().strip().split()]
mods = [item % k for item in S]
freqs = defaultdict(int)
for elem in mods:
    freqs[elem] += 1
total = 0
for key, val in freqs.items():
    if val == 0:
        continue
    if key == 0:
        total += 1
    elif (k - key) == key:
        total += 1
    elif key > (k - key):
        if (k - key) in freqs:
            total +=  max([val, freqs[k - key]])
        else:
            total += val
    elif key < (k - key):
        if (k - key not in freqs):
            total += val

print(total)