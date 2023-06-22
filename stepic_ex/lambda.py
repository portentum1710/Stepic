#           LAMBDA FUNCTION
# lst = [5, 3, 0, -6, 8, 10, 1]
#
#
# def get_filter(a, filtr=None):
#     if filter is None:
#         return a
#
#     res = []
#     for x in a:
#         if filtr(x):
#             res.append(x)
#
#     return res
#
#
# r = get_filter(lst, lambda p: p % 2 == 0)
# print(r)
# --------------------------------------------------------------------
#                         ПОДВИГ 2

get_sq = lambda n: n ** 2
# print(get_sq(7))
#                         ПОДВИГ 3

get_div = lambda x, y: None if y == 0 else x / y
# print(get_div(6, 0))
#                         ПОДВИГ 4

# abs_num = lambda y: abs(y)
# x = float(input())
# print(abs_num(x))
#                         ПОДВИГ 5
#  5 4 -3 4 5 -24 -6 9 0
is_string = lambda string: "ra" in string
# s = input()
# print(is_string(s))
#                         ПОДВИГ 6

def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


it = list(map(int, input().split()))
lst = filter_lst(it)
print(*lst)
lst = filter_lst(it, lambda x: x < 0)
print(*lst)
lst = filter_lst(it, lambda x: x >= 0)
print(*lst)
lst = filter_lst(it, lambda x: 3 <= x <= 5)
print(*lst)



