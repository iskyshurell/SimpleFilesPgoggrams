import random
import os


def first_func(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def sec_func(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


def main_func():

    with open("coordinates.txt", "r") as file:
        with open("result.txt", "w") as result:
            for line in file:
                nums_list = line.split()
                try:
                    res1 = first_func(int(nums_list[0]), int(nums_list[1]))
                except Exception:
                    print("Error! Ошибка в 1 функции")
                try:
                    res2 = sec_func(int(nums_list[0]), int(nums_list[1]))
                except Exception:
                    print("Error! Ошибка в 2 функции")
                number = random.randint(0, 100)

                my_list = sorted([round(res1, 3), round(res2, 3), round(number, 3)])
                result.write(f"{' '.join(str(my_list))} \n")


main_func()


# try:
#     file = open('coordinates.txt', 'r')
#     for line in file:
#         nums_list = line.split()
#         res1 = first_func(int(nums_list[0]), int(nums_list[1]))
#         try:
#             res2 = sec_func(int(nums_list[0]), int(nums_list[1]))
#             try:
#                 number = random.randint(0, 100)
#                 file_2 = open('result.txt', 'w')
#                 my_list = sorted([res1, res2, number])
#                 file_2.write(' '.join(my_list))
#             except Exception:
#                 print("Что-то пошло не так")
#         except Exception:
#             print("Что-то пошло не так со второй функцией")
#         finally:
#             file.close()
#             file_2.close()
# except Exception:
#     print("Что-то пошло не так с первой функцией")


# TODO отредактировать и исправить программу
