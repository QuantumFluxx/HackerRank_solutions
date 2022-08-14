import sys

def canSort(l):
    s = sorted(l)
    for i in s[:-2]:
        if l.index(i) % 2:
            l.remove(i)
            l[0],l[1]=l[1],l[0]
        else:
            l.remove(i)
    if l[0]<l[1]:
        return True
    else:
        return False

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        A = list(map(int, sys.stdin.readline().split()))
        if canSort(A):
            print("YES")
        else:
            print("NO")