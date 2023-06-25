# import sys

# программу не менять, только добавить два метода
lst_in = ["1 Сергей 35 120000", "2 Федор 23 12000", "3 Иван 13 1200"]  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for i in data:
            dct = {}
            item_ls = i.split()
            for idx, key in enumerate(DataBase.FIELDS):
                dct[key] = item_ls[idx]
            self.lst_data.append(dct)
# вариант автора
#    def insert(self, data):
#         for x in data:
#             self.lst_data.append(dict(zip(self.FIELDS, x.split())))

    def select(self, a, b):
        if len(self.lst_data) > b:
            b = len(self.lst_data)




db = DataBase()
db.insert(lst_in)
print(db.lst_data)

# FIELDS = ('id', 'name', 'old', 'salary')
# ls = ["1 Сергей 35 120000", "2 Федор 23 12000", "3 Иван 13 1200"]
# new_ls = []
#
# for i in ls:
#     dct = {}
#     item_ls = i.split()
#     for idx, key in enumerate(FIELDS):
#         dct[key] = item_ls[idx]
#     new_ls.append(dct)
#
# print(new_ls)


