numSticks = int(input())
s = [int(i) for i in input().split()]                                                                                 
# s = [5, 4, 4, 2, 2, 8]
s.sort(reverse=True)
while s:
    print(len(s))
    min = s.pop()
    while s and min == s[-1]:
        s.pop()