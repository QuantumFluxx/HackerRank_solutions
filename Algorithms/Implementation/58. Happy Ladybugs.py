games = int(input())
for g in range(games):
    n = int(input())
    b = input()
    bugs = {}
    underscore = False
    for bi in b:
        if bi == '_':
            underscore = True
        else:
            if bi in bugs:
                bugs[bi] += 1
            else:
                bugs[bi] = 1
    if underscore:
        for bi in bugs:
            if bugs[bi] == 1:
                print('NO')
                break
        else:
            print('YES')
    else:
        if n == 1:
            print('NO')
        else:
            if b[0] != b[1]:
                print('NO')
            else:
                for i in range(1, n - 1):
                    if b[i - 1] != b[i] and b[i + 1] != b[i]:
                        print('NO')
                        break
                else:
                    if b[-1] != b[-2]:
                        print('NO')
                    else:
                        print('YES')