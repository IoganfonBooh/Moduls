from datetime import datetime

from decorators import debug

# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper
#
# #Эту функцию мы будем декорировать
# def my_first_decorator():
# 	print("Это мой первый декоратор!")
#
# my_first_decorator = my_decorator(my_first_decorator)
#
#
# my_first_decorator()


# def working_hours(func):
#     def wrapper():
#         if 9 <= datetime.now().hour < 20:
#             func()
#         else:
#             pass  # Нерабочее время, выходим
#     return wrapper
#
# @working_hours
# def writing_tests():
#     print("Я пишу тесты на python!")
#
# writing_tests()

# from decorators import do_twice

# @do_twice
# def test_twice():
#     print("Это вызов функции test_twice!")
# test_twice()



# @do_twice
# def test_twice_without_params():
#     print("Этот вызов без параметров")
#
# @do_twice
# def test_twice_2_params(str1, str2):
#     print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))
#
# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#
# test_twice_without_params()
# test_twice_2_params("1", "2")
# test_twice("single")


# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#     return "Done"
#
# print(test_twice.__name__)

@debug
def age_passed(name, age=None):
  if age is None:
    return "Необходимо передать значение age"
  else:
    return "Аргументы по умолчанию заданы!"

age_passed("Роман")
age_passed("Роман", age=21)