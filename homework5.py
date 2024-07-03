immutable_tuple = ('food', 1, False)
print(immutable_tuple)
# immutable_tuple[1] = 15
# изменить элементы кортежа нельзя, потому-что кортеж не поддерживает обращение по элементам
mutable_list = ['pineapple', 52, True]
print(mutable_list)
mutable_list[0] = 'strawberry'
mutable_list.extend(['truffle'])
print(mutable_list)
