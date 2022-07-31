# Problem: https://www.hackerrank.com/challenges/plus-minus/problem
# Score: 10


def plusMinus(arr):
    positive_ratio = '{:.6f}'.format(sum([1 for item in arr if item > 0]) / len(arr))
    negative_ratio = '{:.6f}'.format(sum([1 for item in arr if item < 0]) / len(arr))
    zero_ratio = '{:.6f}'.format(sum([1 for item in arr if item == 0]) / len(arr))
    print('\n'.join([positive_ratio, negative_ratio, zero_ratio]))