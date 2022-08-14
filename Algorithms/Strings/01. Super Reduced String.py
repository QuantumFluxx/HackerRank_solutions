s = input()

changed = True
while changed and s != "":
    changed = False
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            changed = True
            s = s[:(i)] + s[(i+2):]
            break

if s == "":
    print('Empty String')
else:
    print(s)