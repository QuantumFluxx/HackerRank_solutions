import sys

s = input().strip()

count = 1
for letter in s:
    if ord(letter) <= ord('Z'):
        count += 1
print(count)