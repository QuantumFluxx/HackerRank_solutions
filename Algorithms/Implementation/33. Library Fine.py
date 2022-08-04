res = list(reversed([int(x) for x in input().split()]))
due = list(reversed([int(x) for x in input().split()]))

def calc(res, due):
    if res[0] < due[0]:
        return 0
    if res[0] > due[0]:
        return 10000
    if res[1] < due[1]:
        return 0
    if res[1] > due[1]:
        return 500 * (res[1] - due[1])
    if res[2] < due[2]:
        return 0
    if res[2] > due[2]:
        return 15 * (res[2] - due[2])
    return 0
print(calc(res, due))