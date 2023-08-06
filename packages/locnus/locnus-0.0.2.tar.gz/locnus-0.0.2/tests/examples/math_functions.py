import math


def pizza_volume(z, a, num_pizzas=1, cut_in_half=False):
    volume = math.pi * z * z * a * num_pizzas
    if cut_in_half:
        volume /= 2
    return volume
