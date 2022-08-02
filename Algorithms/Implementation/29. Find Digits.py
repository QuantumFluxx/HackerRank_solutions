T = int(input())


for t in range(T):
    i_value = int(input())
    c_value = [float(i) for i in str(i_value)]
    
    total = 0
    for c in c_value:
        if c == 0:
            continue
        if (i_value/c)%1 == 0:
            total += 1
    print(total)