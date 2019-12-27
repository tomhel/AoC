#!/usr/bin/env python3


import re


def deal_with_increment(deck, n):
    shuffled = [None] * len(deck)

    for i, card in enumerate(deck):
        shuffled[i * n % len(shuffled)] = card

    return shuffled


def deal_into_new_stack(deck, n):
    return list(reversed(deck))


def cut(deck, n):
    return deck[n:] + deck[:n]


def load_input():
    with open("input") as f:
        for row in f:
            technique, n = re.findall("[a-z ]*[a-z]|-?\d+", row.strip() + " 0")[:2]
            yield technique, int(n)


def shuffle():
    techniques = {
        "deal with increment": deal_with_increment,
        "deal into new stack": deal_into_new_stack,
        "cut": cut
    }

    deck = list(range(10007))

    for t, n in load_input():
        deck = techniques[t](deck, n)

    return deck


print(shuffle().index(2019))
