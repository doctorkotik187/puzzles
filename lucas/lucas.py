def lucas_rec(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        temp = lucas_rec(n - 1) + lucas_rec(n - 2)
        return temp


def lucas_iter(n):
    a, b = 2, 1

    for _ in range(n - 1):
        a, b = b, a + b

    return b


N = 100
# print(lucas_rec(N))
print(lucas_iter(N))
