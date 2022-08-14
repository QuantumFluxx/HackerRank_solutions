import sys

strings = []
for line in sys.stdin:
    strings.append(line.strip())

for i in strings[1:]:
    S = i
    R = i[::-1]
    funny = True
    for j in range(1, len(i)):
        if abs(ord(S[j]) - ord(S[j-1])) != abs(ord(R[j]) - ord(R[j-1])):
            funny = False
            break
            
    if funny:
        print("Funny")
    else:
        print("Not Funny")