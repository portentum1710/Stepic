#                ПОДВИГ 3
# s = set(map(float, input().split()))
# s = list(s)
# print(*sorted(s))
#                ПОДВИГ 4
# text = map(str, input().lower().split())
# text = set(text)
# print(len(text))
#                ПОДВИГ 5
# s = input()
# digits = []
# for syb in s:
#     if syb.isdigit():
#         digits.append(int(syb))
#
# if digits:
#     digits = sorted(list(set(digits)))
#     print(*digits)
# else:
#     print("НЕТ")
#                ПОДВИГ 6
# lst_in = ["Мария", "Елена", "Екатерина", "Александр", "Елена", "Мария"]
#
# lst_in = len(set(lst_in))
# print(lst_in)
#                ПОДВИГ 7

# lst_in = list(map(str.strip, sys.stdin.readlines()))
# users = []
# for comment in lst_in:
#     start_idx = 0
#     end_idx = comment.index(":")
#     users.append(comment[start_idx:end_idx])
#
# print(len(set(users)))
#                ПОДВИГ 8
flag = True
cities = set()
while flag:
    city = input().lower()
    if city != "q":
        cities.add(city)
    else:
        flag = False

print(len(cities))
