n, k = map(int, input().split())
rq, cq = map(int, input().split())

moves = {'n': n - rq, 'nw': min(n - rq, cq-1), 'ne': min(n - rq, n - cq),
         's': rq-1, 'sw': min(rq-1, cq-1), 'se': min(rq-1, n - cq), 'w': cq-1, 'e': n - cq}
for _ in range(k):
    r, c = map(int, input().split())
    if c == cq:
        if r > rq:
            moves['n'] = min(r-rq-1, moves['n'])
        else:
            moves['s'] = min(rq-r-1, moves['s'])
    elif r == rq:
        if c > cq:
            moves['e'] = min(c-cq-1, moves['e'])
        else:
            moves['w'] = min(cq-c-1, moves['w'])
    elif c - r == cq - rq:
        if c < cq and r < rq:
            moves['sw'] = min(min(cq-c-1, rq-r-1), moves['sw'])
        elif c > cq and r > rq:
            moves['ne'] = min(min(c-cq-1, r-rq-1), moves['ne'])
    elif c + r == cq + rq:
        if c < cq and r > rq:
            moves['nw'] = min(min(r-rq-1, cq-c-1), moves['nw'])
        elif c > cq and r < rq:
            moves['se'] = min(min(rq-r-1, c-cq-1), moves['se'])
            
print(sum(moves.values()))