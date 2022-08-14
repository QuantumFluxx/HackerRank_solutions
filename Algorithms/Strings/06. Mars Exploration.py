import sys

S = input().strip()

num_errors = 0

for i, char in enumerate(S):
    if i%3 == 1:
        if char != 'O':
            num_errors += 1
    else:
        if char != 'S':
            num_errors += 1
  
print(num_errors)