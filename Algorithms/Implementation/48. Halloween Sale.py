import sys

def howManyGames(p, d, m, s):
    ans = 0
    while s >= p:
        s -= p
        ans += 1
        p = max(m, p - d)
    return ans

if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)