#!/usr/bin/env python3


def calc_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel(fuel)
 

data = (int(x) for x in open("input"))
print(sum(calc_fuel(mass) for mass in data))
