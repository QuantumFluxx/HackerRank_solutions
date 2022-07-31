# Problem: https://www.hackerrank.com/challenges/staircase/problem
# Score: 10


def staircase(n):
    for i in range(1, n + 1):
        result = ' '.rjust(i + 1, '#').rstrip()
        print('{:>{width}}'.format(result, width=n))