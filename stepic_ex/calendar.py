def get_prev_and_next_date():
    month, number = map(int, input().split())
    print(f"Текущий День: {number}.{month}")
    previous_day = previous_month = next_day = next_month = 0

    months_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if number != 1:
        days_in_month = months_list[month - 1]
        if number == days_in_month:
            print("Последний день месяца")
            next_day = 1
            next_month = month + 1
        else:
            print("Любой день")
            next_day = number + 1
            next_month = month
        previous_day = number - 1
        previous_month = month
    else:
        print("1 число")
        previous_day = months_list[month - 2]
        previous_month = month - 1
        next_day = number + 1
        next_month = month

    previous_day = str(previous_day).rjust(2, '0')
    previous_month = str(previous_month).rjust(2, '0')
    next_day = str(next_day).rjust(2, '0')
    next_month = str(next_month).rjust(2, '0')

    print(f'{previous_day}.{previous_month} {next_day}.{next_month}')


if __name__ == "__main__":
    get_prev_and_next_date()
