first = sorted(list(input("")))
firstList = sorted(list(first))
second = sorted(list(input("")))
secondList = sorted(list(second))
last_first = 0
last_second = 0
deletion = 0

for i in range(0, len(first)):
    if(first[i] not in secondList):
        deletion += 1
    else:
        for x in range(last_second, len(second)):
            if(secondList[x] == first[i]):
                secondList[x] = ""
                last_second = x
                break
        
for j in range(0, len(second)):
    if(second[j] not in firstList):
        deletion += 1
    else:
        for y in range(last_first, len(first)):
            print
            if(firstList[y] == second[j]):
                firstList[y] = ""
                last_first = y
                break
                
print(deletion)