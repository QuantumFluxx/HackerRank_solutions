import sys


s = input().strip()
t = input().strip()
k = int(input().strip())
same = 0
i = 0
while i<len(s) and i<len(t) and s[i]==t[i]:
    i+=1
    
s1 = len(s[i:])
t1 = len(t[i:])
if s1+t1>k:
    print("No")
elif s1+t1==k:
    print("Yes")
elif (len(s)+len(t))-k<=0:
    print("Yes")
elif abs((len(s)+len(t))-k)%2==0:
    print("Yes")
else:
    print("No")