"""Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randrange

initial_list = [randrange(1,1000) for el in range(1,15)]
print(f'initial list is: {initial_list}')

new_list = [el for el in initial_list if el > initial_list[initial_list.index(el)-1]]
print(f'new list is: {new_list}')