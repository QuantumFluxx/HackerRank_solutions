N, K, Q= map(int, input().split())
A= tuple(map(int, input().split()))
for _ in range(Q):
    print(A[(int(input())+N-K)%N])