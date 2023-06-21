lst = [5, 3, 0, -6, 8, 10, 1]


def get_filter(a, filtr=None):
    if filter is None:
        return a

    res = []
    for x in a:
        if filtr(x):
            res.append(x)

    return res


r = get_filter(lst, lambda p: p % 2 == 0)
print(r)