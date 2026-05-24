#!/usr/bin/env python3

def fibonacci_print(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b

def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-2) + fibonacci_rec(n-1)

def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

N = 10
fibonacci_print(N)
print("-------------")
print(str(fibonacci_rec(N)) + " | " + str(fibonacci_iter(N)))
