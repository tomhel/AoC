#!/usr/bin/env python3


def decode_image(image, width, height):
    layers = len(image) // (width * height)

    for i in range(width * height):
        for pix in (image[i+l*width*height] for l in range(layers)):
            if pix != 2:
                yield pix
                break


def render_image(image, width):
    for i, pix in enumerate(image):
        print(" " if pix == 0 else "@", end="\n" if (i + 1) % width == 0 else "")


data = [int(i) for i in list(open("input").read().strip())]
decoded = decode_image(data, 25, 6)
render_image(decoded, 25)
