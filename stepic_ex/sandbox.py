k = int(input())

week_days = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
name_of_day = week_days[k % 7 - 1]
print(name_of_day)


