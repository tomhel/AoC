def load():
    with open("input") as f:
        for line in map(lambda x: x.strip(), f):
            yield line if line == "" else int(line)


def find_max_calories():
    calorie_list, calories = [], 0
    for food in load():
        if food == "":
            calorie_list.append(calories)
            calories = 0
            continue
        calories += food
    return sum(sorted(calorie_list)[-3:])


print(find_max_calories())
