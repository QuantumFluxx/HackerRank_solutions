T = int(input())
for _ in range(T):
    N, K = input().split()
    N = int(N)
    K = int(K)
    students = 0
    arrivals = input().split()
    for i in arrivals:
        if int(i) <= 0:
            students += 1
    if students < K:
        print("YES")
    else:
        print("NO")