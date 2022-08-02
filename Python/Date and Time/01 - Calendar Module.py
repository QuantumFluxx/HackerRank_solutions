# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/calendar-module/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

import calendar

MM, DD, YYYY = map(int,raw_input().split())
print calendar.day_name[calendar.weekday(YYYY,MM,DD)].upper()