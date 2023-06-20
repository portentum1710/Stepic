import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)



length = len(lst_in)
new_lst = []

i = 0
while i < length:
    if " " not in lst_in[i]:
        new_lst.append(lst_in[i])
    i += 1

print(" ".join(new_lst))






