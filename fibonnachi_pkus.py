def fibb(num):
    if num <= 3:
        return 1
    else:
        return fibb(num - 1) + fibb(num - 2) + fibb(num - 3)


def fibb_gen(num):
    a = 1
    b = 1
    c = 1

    for i in range(num):
        if i < 2:
            yield 1
        else:
            yield a
            a, b, c = a+b+c, a, b
