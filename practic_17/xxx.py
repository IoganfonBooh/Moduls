# 001
# your_chain = [int(x) for x in input('Введите последовательность чисел через пробел: ').split()]
# element = int(input('Введите число: '))
#
#
# def merge_sort(L):
#     if len(L) < 2:
#         return L[:]
#     else:
#         middle = len(L) // 2
#         left = merge_sort(L[:middle])
#         right = merge_sort(L[middle:])
#         return merge(left, right)
#
# def merge(left, right):
#     result = []
#     i, j = 0, 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
#
# your_chain = merge_sort(your_chain)
#
# print(merge_sort(your_chain))
#
# def binary_search(array, element, left, right):
#     if left > right:
#         return False
#
#     middle = (right+left) // 2
#     if array[middle] == element:
#         return middle
#     elif element < array[middle]:
#         return binary_search(array, element, left, middle - 1)
#     else:
#         return binary_search(array, element, middle + 1, right)
#
# print(binary_search(your_chain, element, 0, len(your_chain)))


# # 002
#
# error = 'ПЕРЕЗАПУСТИТЕ ПРОГРАММУ'
# sum_result = input('Введите несколько целых чисел через пробел: ')
# rand_digit = int(input('И ещё одно целое число: '))
#
# # Проверяем на цифры в строке
#
# def is_int(str):
#     str = str.replace(' ', '')
#     try:
#         int(str)
#         return True
#     except ValueError:
#         return False
#
# # Проверяем на соответствие указанному в условии ввода данных.
#
# if " " not in sum_result:
#     print("\nНЕ ЗАБУДЬТЕ ПРО ПРОБЕЛЫ! (введите ЧИСЛА, согласно условиям ввода.)")
#     sum_result = input('Введите ЦЕЛЫЕ числа через пробел: ')
# if not is_int(sum_result):
#     print('\nВ ВВОДЕ СОДЕРЖАТСЯ НЕ ЦИФРЫ ЛИБО НЕ ЦЕЛЫЕ ЧИСЛА (введите ЧИСЛА, согласно условиям ввода.)\n')
#     print(error)
# else:
#     sum_result = sum_result.split()
#
# list_sum_result = [int(item) for item in sum_result]
#
# # Сортируем список
#
# def merge_sort(L):
#     if len(L) < 2:
#         return L[:]
#     else:
#         middle = len(L) // 2
#         left = merge_sort(L[:middle])
#         right = merge_sort(L[middle:])
#         return merge(left, right)
#
# def merge(left, right):
#     result = []
#     i, j = 0, 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
#
# list_sum_result = merge_sort(list_sum_result)
#
# # Установливаем позицию элемента
#
# def binary_search(array, element, left, right):
#     try:
#         if left > right:
#             return False
#         middle = (right + left) // 2
#         if array[middle] == element:
#             return middle
#         elif element < array[middle]:
#             return binary_search(array, element, left, middle - 1)
#         else:
#             return binary_search(array, element, middle + 1, right)
#     except IndexError:
#         return 'Число превышает диапазон списка, введите меньшее число.'
#
# print(f'Упорядоченный по возрастанию список: {list_sum_result}')
#
# if not binary_search(list_sum_result, rand_digit, 0, len(list_sum_result)):
#     rI = min(list_sum_result, key=lambda x: (abs(x - rand_digit), x))
#     ind = list_sum_result.index(rI)
#     max_ind = ind + 1
#     min_ind = ind - 1
#     if rI < rand_digit:
#         print(f'''В списке нет введенного элемента
# Ближайший меньший элемент: {rI}, его индекс: {ind}
# Ближайший больший элемент: {list_sum_result[max_ind]} его индекс: {max_ind}''')
#     elif min_ind < 0:
#         print(f'''В списке нет введенного элемента
# Ближайший больший элемент: {rI}, его индекс: {list_sum_result.index(rI)}
# В списке нет меньшего элемента''')
#     elif rI > rand_digit:
#         print(f'''В списке нет введенного элемента
# Ближайший больший элемент: {rI}, его индекс: {list_sum_result.index(rI)}
# Ближайший меньший элемент: {list_sum_result[min_ind]} его индекс: {min_ind}''')
#     elif list_sum_result.index(rI) == 0:
#         print(f'Индекс введенного элемента: {list_sum_result.index(rI)}')
# else:
#     print(f'Индекс введенного элемента: {binary_search(list_sum_result, rand_digit, 0, len(list_sum_result))}')

#
# # 003
# nums = input("Введите последовательность чисел через пробел: ").split()
# num = int(input("Введите любое число: "))
# try:
#     numlist = list(map(int, nums))
# except ValueError:
#     print("Ошибка ввода. Выход из программы.")
#     exit()
# else:
#     pass
#
# for i in range(1, len(numlist)):
#     x = numlist[i]
#     idx = i
#     while idx > 0 and numlist[idx-1] > x:
#         numlist[idx] = numlist[idx-1]
#         idx -= 1
#     numlist[idx] = x
# print(numlist)
#
#
# def binary_search(array, element, left, right):
#     if left > right:
#         print("Введенное вами число отсутствует в списке.")
#
#     middle = (right + left) // 2
#     if array[middle] == element:
#         return middle - 1
#     elif element < array[middle]:
#         return binary_search(array, element, left, middle - 1)
#     else:
#         return binary_search(array, element, middle + 1, right)
#
#
#
#
#
# array = numlist
# element = num
# print(binary_search(array, element, 0, numlist[-1]))



# # 004
# array = input("введите числа через пробел: ")
# array_valid = []
# for elem in array.split():
#     if elem.isdigit():
#         array_valid.append(int(elem))
#
# def sort_func(num_list):
#     """Сортировка списка пузырьком"""
#     for i in range(len(num_list)):
#         for j in range(len(num_list) - i - 1):
#             if num_list[j] > num_list[j + 1]:
#                 num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
#     return num_list
#
#
# a = sort_func(array_valid)
# print(a)  # отсортированный список
# b = int(input("введите число для поиска:"))
#
#
# def poisk(a, b):
#     for i in range(0, len(a) - 1):
#         if a[i] < b and b <= a[i + 1]:
#             return i
#
#
# if poisk(a, b) == None:
#     print(f"число {b}  за пределами списка")
#
# print(poisk(a, b))
#
#
# # 005
# #
# def input_():  ## Функция ввода чисел и проверки на одинаковые элементы
#     numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
#     for i in range((len(numbers) - 1)):
#         for j in range(i + 1, (len(numbers))):
#             if numbers[i] == numbers[j]:
#                 print("Вы ввели одинаковые числа")
#                 numbers = list(map(int, input("Введите целые числа через пробел: ").split()))
#     return numbers
#
#
# def Sort_bubble(array): ## Функция сортировки
#     length = len(array)
#     for i in range(length):
#         for j in range(0, length-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return numbers
#
# def binary_search(array, number, left, right):  ## Функция бинарного поиска индекса элемента в массиве
#     if left > right:
#         return False
#
#     middle = (right + left) // 2
#     if array[middle] == number:
#         return middle
#     elif number < array[middle]:
#         return binary_search(array, number, left, middle - 1)
#     else:
#         return binary_search(array, number, middle + 1, right)
#
# def num_(numbers, number):  ## Функция элемента, меньшего чем введенный пользователем
#     for i in (Sort_bubble(numbers)): #а следующий за ним больший или равный ему
#         if i < number:
#             num = i
#     return num
#
# numbers = input_()
# number = int(input("Введите любое число: "))
# print("Массив введенных чисел: ", numbers)
# print("Целое число: ", number)
# left = 0
# right = len(numbers) - 1
#
# index = binary_search(numbers, num_(numbers,number), left, right)
# element = numbers[index]
# print("Отсортированный список целых чисел: ", Sort_bubble(numbers))
# print("Индекс и элемент, меньший введенного пользователем а следующий за ним "
#       "больший или равный ему: ", "[", index, "]", element )
#

# 006
#
# def sorting(l):
#     for i in range(len(l)):
#         x = l[i]
#         idx = i
#         while idx > 0 and l[idx - 1] > x:
#             l[idx] = l[idx - 1]
#             idx -= 1
#         l[idx] = x
#     return l
#
#
# def binary_search(array, num, left, right):
#     if left > right:
#         return False
#
#     middle = (right + left) // 2
#     if num > array[middle] and num <= array[middle + 1]:
#         return middle, middle + 1
#     elif array[middle] == num:
#         return middle - 1, middle
#     elif num < array[middle]:
#         return binary_search(array, num, left, middle - 1)
#     else:
#         return binary_search(array, num, middle + 1, right)
#
# l = (list(map(int, input('Введите числа от 1 до 999 через пробел: ').split())))
# array = sorting(l)
#
# while True:
#     try:
#         num = int(input("Введите число от 1 до 999: "))
#         if num <= 0 or num > 999 or num > max(l):
#             raise Exception
#         break
#
#     except ValueError:
#         print("Нужно ввести число!")
#     except Exception:
#         print("Неправильный диапазон!")
# print(array)
# print(binary_search(array,num,0,len(array)-1))
#

f = [2, 4, 1, 3, 6, 4, 9, 0]
f.sort()
print(f)