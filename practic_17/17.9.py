#
#
set_of_numbers = input('Введите несколько целых чисел через пробел: ')
# number = int(input('Введите одно целое число: '))


def isint(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False


if " " not in set_of_numbers:
    print("\nБудьте внимательны, вводите числа через пробел)")
    set_of_numbers = input('Введите несколько целых чисел: ')
if not isint(set_of_numbers):
    print('\nВ ВВОДЕ СОДЕРЖАТСЯ НЕ ЦИФРЫ ЛИБО НЕ ЦЕЛЫЕ ЧИСЛА (введите ЧИСЛА, согласно условиям ввода.)\n')
    # set_of_numbers = input('Введите ЦЕЛЫЕ числа через пробел: ')
else:
    set_of_numbers = set_of_numbers.split()
    number = int(input('Введите одно целое число: '))
sum_result = [int(item) for item in set_of_numbers]

# Сортируем список

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

sum_result = merge_sort(sum_result)

# Установливаем позицию элемента

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число превышает диапазон списка, введите меньшее число.'

print(f'Упорядоченный по возрастанию список: {sum_result}')

if not binary_search(sum_result, number, 0, len(sum_result)):
    rI = min(sum_result, key=lambda x: (abs(x - number), x))
    ind = sum_result.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < number:
        print(f'''В списке нет number
Ближайший < элемент: {rI}, его индекс: {ind}
Ближайший > элемент: {sum_result[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет number
Ближайший > элемент: {rI}, его индекс: {sum_result.index(rI)}
В списке нет < элемента''')
    elif rI > number:
        print(f'''В списке нет number
Ближайший > элемент: {rI}, его индекс: {sum_result.index(rI)}
Ближайший < элемент: {sum_result[min_ind]} его индекс: {min_ind}''')
    elif sum_result.index(rI) == 0:
        print(f'Индекс number: {sum_result.index(rI)}')
else:
    print(f'Индекс number: {binary_search(sum_result, number, 0, len(sum_result))}')

