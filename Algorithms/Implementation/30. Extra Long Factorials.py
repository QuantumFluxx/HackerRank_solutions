def factorial(x):
    if x == 0: return 0
    answer = 1
    while x > 0:
        answer *= x
        x = x - 1
    return answer

if __name__ == '__main__':
    num = int(input())
    print(factorial(num))