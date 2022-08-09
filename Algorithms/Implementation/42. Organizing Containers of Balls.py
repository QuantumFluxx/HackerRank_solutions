import sys


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
        M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
        M.append(M_t)
    # your code goes here

    Rows = []
    Cols = []
    Works = True
    
    for i in range(n):
        Rows.append(sum(M[i]))
       
            
    N = [list(i) for i in zip(*M)]     
    for i in range(n):
        Cols.append(sum(N[i]))
  
    Rows.sort()
    Cols.sort()
    if(Rows == Cols):
        print("Possible")
    else:
        print("Impossible")