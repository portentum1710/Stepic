month, number = map(int, input().split())

previous_day = 0
previous_month = 0

next_day = 0
next_month = 0

months_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if number == 1:
    print("Pos 1")
    previous_day = months_list[month - 2]
    previous_month = month - 1
    next_day = number + 1
    next_month = month
elif number in (28, 30, 31):
    print("Pos 2")
    previous_day = number - 1
    previous_month = month
    next_day = 1
    next_month = month + 1
else:
    print("Pos 3")
    previous_day = number - 1
    previous_month = month
    next_day = number + 1
    next_month = month

print(f"Предыдущий день: {previous_day}.{previous_month}")
print(f"Следующий день: {next_day}.{next_month}")
