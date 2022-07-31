# Problem: https://www.hackerrank.com/challenges/time-conversion/problem
# Score: 15


def timeConversion(s):
    if s.find('PM') > 0:
        hour, minute, second = s.replace('PM', '').split(':')

        if int(hour) < 12:
            hour = str(int(hour) + 12).rjust(2, '0')
        else:
            hour = str(int(hour)).rjust(2, '0')
    else:
        hour, minute, second = s.replace('AM', '').split(':')

        if int(hour) == 12:
            hour = str(0).rjust(2, '0')
        else:
            hour = str(int(hour)).rjust(2, '0')

    return '{}:{}:{}'.format(hour, minute, second)