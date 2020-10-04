# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

list = ["яблоко","банан","киви","арбуз"]
index = 1
for item in list:
    print(index, ' ', '{:>6}'. format(item))
    index += 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
lst1 = [9, 8, 8, 4, 5, 1, 3]
lst2 = [1, 8, 5]
res = []
for i in lst1:
    if i not in lst2:
        res.append(i)
lst1 = res
print(lst1)
print()


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
