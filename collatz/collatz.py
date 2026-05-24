#!/usr/bin/env python3


def collatz(n: int, counter: int = 1):
    if n < 1:
        return "Please provide a positive integer N."
    print(f"step {counter}: {n}")
    if n == 1:
        return
    if n % 2 == 0:
        return collatz(int(n / 2), counter + 1)
    else:
        return collatz(n * 3 + 1, counter + 1)


collatz(27)
