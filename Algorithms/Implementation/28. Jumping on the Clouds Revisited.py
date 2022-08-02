n,k = map(int,input().strip().split())
c = [int(s) for s in input().strip().split()]
print(100-n//k-2*sum([c[i] for i in range(0,n,k)]))