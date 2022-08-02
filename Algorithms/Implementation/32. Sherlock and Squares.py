t = int(input())

for i in range (0,t):
    count = 0
    a,b = [int(j) for j in input().strip().split()]
    square1 = a ** (.5)
    if (square1 != int(square1)):
        a1 = int(square1) + 1
    else:
        a1 = int(square1)
    square2 = b ** (.5)
    b1 = int(square2)
    count = b1 - a1 +1
    print(count)