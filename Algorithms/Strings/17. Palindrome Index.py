def palindromeIndex(s):
    l = len(s)
    i = 0
    j = l-1
    while i<l:
        if s[i]!=s[j]:
            break
        i+=1
        j-=1
    if i>j: return -1
    a = i+1
    b = j
    while a<j and b>i+1:
        if s[a]!=s[b]:
            return j
        a+=1
        b-=1
    return i

for _ in range(int(input())):
    print(palindromeIndex(input()))