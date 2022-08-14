def solve(N,K):
    if K == 0: return range(1,1+N)
    if N%(2*K): return [-1]
    base = range(K+1,2*K+1) + range(1,1+K)
    ans = []
    Q = N/(2*K)
    for q in xrange( Q ):
        for i in base:
            ans.append( q*2*K + i )
    return ans
rr = raw_input
rrI = lambda: int(rr())
rrM = lambda: map(int,rr().split())
for _ in xrange(rrI()):
    print " ".join(map(str, solve(*rrM())))