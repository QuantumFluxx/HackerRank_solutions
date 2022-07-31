# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Score: 10


def diagonalDifference(arr):
    first_diagonal = 0
    second_diagonal = 0
    
    for i in range(len(arr)):
        first_diagonal += arr[i][i]
        second_diagonal += arr[i][len(arr)-1 - i]

    return abs(first_diagonal - second_diagonal)