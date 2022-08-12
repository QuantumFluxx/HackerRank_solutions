tests = int(input())
n = 0
n2 = 0
for i in range(0, tests):
    inp = input()
    inp = inp.split(' ')
    n = int(inp[0])
    thegrid = []
    for i in range(0, n):
        s = input()
        thegrid.append(s)
    inp2 = input()
    inp2 = inp2.split(' ')
    n2 = int(inp2[0])
    subgrid = []
    for i in range(0, n2):
        s = input()
        subgrid.append(s)
    found = False
    for i in range(0, len(thegrid)):
        for j in range(0, len(subgrid)):
            if(subgrid[j] in thegrid[i + j]):
                if (j == len(subgrid)-1):
                    found = True
                    print ("YES")
                    break
                continue
            else:
                break
            break
    if not found:
        print ("NO")