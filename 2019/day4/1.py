#!/usr/bin/env python3


def has_double(password):
    for i, digit in enumerate(password[:-1]):
        if digit == password[i+1]:
            return True

    return False


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
