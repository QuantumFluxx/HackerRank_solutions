t = int(input())
n = 0
count = 0
while n < t:
    n += 3*(2**count)
    count += 1
print(n-t+1)