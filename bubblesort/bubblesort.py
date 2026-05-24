#!/usr/bin/env python3


def bubblesort(list):
    for _ in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    print(list)


bubblesort([2, 7, 1, 3, 9, 8])
