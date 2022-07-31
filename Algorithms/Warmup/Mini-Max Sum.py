# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Score: 10


def miniMaxSum(arr):
    arr.sort(reverse=True)
    max_list = [arr[i] for i in range(len(arr)-1)]

    arr.sort()
    min_list = [arr[i] for i in range(len(arr)-1)]
    return print(sum(min_list), sum(max_list))