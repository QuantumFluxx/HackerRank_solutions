tcs = int(input())
for i in range(tcs):
    b, w = map(int, input().split(' '))
    x, y, z = map(int, input().split(' '))
    if x + z < y:
        print(b*x+w*(x+z))
    elif y + z < x:
        print(w*y+b*(y+z))
    else:
        print(b*x+w*y)