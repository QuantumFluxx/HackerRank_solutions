def getJumps(ar):
    jumps = []
    for i in range(len(ar)-1):
        if ar[i] > ar[i+1]:
            jumps.append(i)
    return jumps

def isSortedWithSwap(ar, i, j):
    ar[i], ar[j] = ar[j], ar[i]
    jumps = getJumps(ar)
    ar[i], ar[j] = ar[j], ar[i] # repair list
    return len(jumps) == 0

def isSortedWithReverse(ar, i, j):
    ar[i:j] = ar[j-1:i+1:-1]
    jumps = getJumps(ar)
    ar[i:j] = ar[j-1:i+1:-1] # repair list
    return len(jumps) == 0

def magic(ar):
    jumps = getJumps(ar)
    if len(jumps) == 0:
        print('yes')
    elif len(jumps) == 1:
        i = jumps[0]
        j = i+1
        while j+1 < len(ar) and ar[i+1] == ar[j+1]: #move point to last same element
            j+=1
        if isSortedWithSwap(ar, i, j):
            print('yes')
            print('swap', i+1, j+1)
        else:
            print('no')
    elif len(jumps) == 2:
        i = jumps[0]
        j = jumps[1] + 1
        if isSortedWithSwap(ar, i, j):
            print('yes')
            print('swap', i+1, j+1)
        else:
            print('no')
    else:
        i = jumps[0]
        j = jumps[-1] + 2
        if isSortedWithReverse(ar,i,j):
            print('yes')
            print('reverse', i+1, j)
        else:
            print('no')

n = int(input())
ar = list(map(int, input().split()))
magic(ar)