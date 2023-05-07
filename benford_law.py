from random import *
import math

distribution = [0 for i in range(9)]


def generate():
    nb = randint(1, 10000) * randint(1, 10000) * randint(1, 10000)
    while nb == 0:
        nb = randint(1, 10000) * randint(1, 10000) * randint(1, 10000)
    return nb


def first_n_digits(num, n):
    return num // 10 ** (int(math.log10(num)) - n + 1)


for i in range(1000000):
    distribution[first_n_digits(generate(), 1) - 1] += 1

distribution_scaled = [(i * 100 / 1000000) for i in distribution]

print(distribution_scaled)
