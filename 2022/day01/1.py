def load():
    with open("input") as f:
        for line in map(lambda x: x.strip(), f):
            yield line if line == "" else int(line)


def find_max_calories():
    max_calories, calories = 0, 0
    for food in load():
        if food == "":
            max_calories = max(max_calories, calories)
            calories = 0
            continue
        calories += food
    return max_calories


print(find_max_calories())
