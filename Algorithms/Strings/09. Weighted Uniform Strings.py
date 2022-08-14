import sys
from collections import Counter

def weight_of_letter(l):
    return ord(l) - 96

def get_uniform_subsets(s):
    cnt = Counter()
    curr = 0
    last = ""
    for ch in s:
        if ch == last:
            curr += 1
        else:
            last = ch
            curr = 1
        if curr > cnt[ch]: cnt[ch] = curr

    weights = set()
    for i in cnt:
        for j in range(cnt[i]):
            weights.add((j+1)*weight_of_letter(i))
    return weights
            
s = input().strip()
weights = get_uniform_subsets(s)
n = int(input().strip())
for a0 in range(n):
    x = int(input().strip())
    # your code goes here
    if x in weights:
        print("Yes")
    else:
        print("No")