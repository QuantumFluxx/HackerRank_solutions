import sys

def surfaceArea(A):
    H = len(A)
    W = len(A[0])
    ans = 2*H*W
    for i in range(H):
        for j in range(W):
            # top
            if i == 0:
                ans += A[i][j]
            
            # left
            if j == 0:
                ans += A[i][j]
            
            # right
            if j == W-1:
                ans += A[i][j]
            else:
                ans += abs(A[i][j]-A[i][j+1])
            
            # bottom
            if i == H-1:
                ans += A[i][j]
            else:
                ans += abs(A[i][j]-A[i+1][j])
    return ans

if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
        A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
        A.append(A_t)
    result = surfaceArea(A)
    print(result)