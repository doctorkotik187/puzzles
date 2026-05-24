#!/usr/bin/env python3

import math


def euclid(a, b):
    d = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    print(d)


euclid((1, 1), (2, 2))
