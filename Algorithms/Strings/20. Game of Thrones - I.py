def can_be_palindrome(string):
    string = sorted(string)
    current_letter_count = 1
    middle = False
    for index, char in enumerate(list(string[1:])):
        if string[index] != char:
            if current_letter_count % 2:
                if not middle:
                    middle = True
                else:
                    return False
        current_letter_count += 1
    return True

print('YES' if can_be_palindrome(input()) else 'NO')