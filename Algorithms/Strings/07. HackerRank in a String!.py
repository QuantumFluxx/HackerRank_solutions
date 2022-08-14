import sys

word ="hackerrank"
q = int(input().strip())
d = ()
for a0 in range(q):
    s = input().strip()
    n = len(s)
    # your code goes here
    p = 0
    wi = 0
    for wi in range(len(word)):
        if wi < 9:
            p = s.find(word[wi], p) +1
            if p == 0:
                break
    if wi == 9:
        print("YES")
    else:
        print("NO")