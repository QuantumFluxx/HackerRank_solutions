import sys

def score(word):
        if len(word) & 1:
                return -1
        mid = int(len(word)/2)
        a = word[0:mid]
        b = list(word[mid:])
        num = 0
        for i in range(len(a)):
                try:   
                        b.remove(a[i])
                except ValueError:
                        num += 1
        return num

num = int(sys.stdin.readline())

for i in range(num):
        s = sys.stdin.readline().strip()
        print(score(s))