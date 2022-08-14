from collections import Counter

def all_substrs(s):
    return [[s[j:j+i] for j in range(len(s) - i + 1)] for i in range(1, len(s))]

def countem(ll):
    c = Counter()
    s = 0
    for lst in ll:
        for e in lst:
            q = ''.join(sorted(e))
            c[q] += 1
    for e in c:
        s += int(c[e]*(c[e]-1)/2)
    return s
    
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(countem(all_substrs(s)))