n=int(input())
fDict=dict()
fInvDict=dict()

L=input().split()
for i in range(n):
    fDict[i+1] = int(L[i])
    fInvDict[int(L[i])] = i+1
for x in range(1,n+1):
    print(fInvDict[fInvDict[x]])