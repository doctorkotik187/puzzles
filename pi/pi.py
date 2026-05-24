#!/usr/bin/env python3

import random


def monte_carlo(n):
    inside = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # inside
        if x**2 + y**2 <= 1:
            inside += 1

    return 4 * inside / n


print(monte_carlo(10000000))
