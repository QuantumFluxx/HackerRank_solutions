t = int(input())
for _ in range(t):
    parts = list(map(int, input().split(' ')))
    # print('parts', parts)
    print((parts[1] + parts[2] - 2) % parts[0] + 1)