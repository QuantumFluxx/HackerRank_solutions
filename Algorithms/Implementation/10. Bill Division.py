n, k = map(int, input().split())
c = list(map(int, input().split()))
b_charged = int(input())

b = (sum(c) - c[k]) / 2
if b_charged == b:
    print("Bon Appetit")
else:
    print(int(b_charged-b))