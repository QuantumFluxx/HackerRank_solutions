import fileinput

stones = []
gems = []

for line in fileinput.input():
    if fileinput.lineno() == 1:
        lengths = int(line)
    else:
        stones.append(line.strip())

#print(stones)
for x in range(0, len(stones[0])):
    if stones[0][x] not in gems:
        gems.append(stones[0][x])
        for y in range(0, lengths):
            if stones[0][x] not in stones[y]:
                #print(x)
                try :
                    gems.remove(stones[0][x])
                except ValueError:
                    continue

print(len(gems))