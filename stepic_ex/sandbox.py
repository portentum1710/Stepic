#var_1, var_2 = map(str, input().split())
# string_01 = input()
# string_02 = input()

msg = "abrakadabra"
print(msg.isalpha())

d = "abc"
print(d.ljust(10, "*"))

print("Иванов Иван Иванович".split(" "))
digs = "1, 2,3, 4,5,6"
print(digs.replace(" ", '').split(","))
', '.join(digs)
print(digs)

fio = "Иванов Иван Иванович"
fio_2 = ','.join(fio.split())
print(fio_2)
