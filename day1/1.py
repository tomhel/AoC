#!/usr/bin/env python3


def calc_fuel(mass):
    return mass // 3 - 2
 

data = (int(x) for x in open("input"))
fuel = sum(calc_fuel(mass) for mass in data)

print(fuel)

