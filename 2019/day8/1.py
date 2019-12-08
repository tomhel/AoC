#!/usr/bin/env python3


def calc_histogram(image, width, height):
    histogram = [0, 0, 0]

    for i, pix in enumerate(image):
        if (i + 1) % (width * height) == 0:
            yield histogram
            histogram = [0, 0, 0]

        histogram[pix] += 1


data = [int(i) for i in list(open("input").read().strip())]
result = min(calc_histogram(data, 25, 6))
print(result[1] * result[2])
