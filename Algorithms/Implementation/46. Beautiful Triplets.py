n, d = [int(r) for r in input().split()]
a = [int(r) for r in input().split()]

triplets = 0
for i in range(n-2):
    for j in range(i + 1, n-1):
        if a[j] - a[i] == d:
            foundTrip = False
            for k in range(j + 1, n):
                if a[k] - a[j] == d:
                    triplets += 1
                    foundTrip = True
                    break
            if foundTrip == True:
                break
            
print(triplets)