month, number = map(int, input().split())

previous_day = 0
next_day = 0
previous_month = 0
next_month = 0


if number == 28 and month == 2:
    next_day = 1
    next_month += month



if month in [1, 3, 5, 7, 8, 10, 12] :
    if 2 <= number <= 30:
        print("in month 31")
        previous_day = number -1
        next_day = number + 1
    elif number == 1:
        previous_day = 31


elif month == 2 :
    if 2 <= number <= 27:
        print("in month 28")
        previous_day = number - 1
        next_day = number + 1

else:

    if 2 <= number <= 29:
        print("in month 30")
        previous_day = number - 1
        next_day = number + 1



previous_day = str(previous_day)
next_day = str(next_day)
month = str(month)
next_month = str(next_month)
print(f"{previous_day.rjust(2, '0')}.{month.rjust(2, '0')} {next_day.rjust(2, '0')}.{next_month.rjust(2, '0')}")

