#!/usr/bin/env python3


def has_double(password):
    current = password[0]
    count = 0

    for digit in password:
        if digit == current:
            count += 1
        elif count == 2:
            return True
        else:
            count = 1

        current = digit

    return count == 2


def is_increasing(password):
    for i, digit in enumerate(password[:-1]):
        if int(digit) > int(password[i+1]):
            return False

    return True


def password_count():
    count = 0

    for password in (str(p) for p in range(248345, 746315)):
        if not has_double(password):
            continue
        elif not is_increasing(password):
            continue
        else:
            count += 1

    return count


print(password_count())
