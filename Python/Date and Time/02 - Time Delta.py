# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/python-time-delta/problem
# Difficulty: Medium
# Max Score: 30
# Language: Python

# ========================
#         Solution
# ========================

import datetime

format_string = "%a %d %b %Y %H:%M:%S %z"
T = int(input())

for test in range(T):
    t1 = str(input())
    t2 = str(input())

    parsed_t1 = datetime.datetime.strptime(t1, format_string)
    parsed_t2 = datetime.datetime.strptime(t2, format_string)

    diff = parsed_t2 - parsed_t1

    print (int(abs(diff.total_seconds())))