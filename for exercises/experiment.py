# numbers = [float(i) for i in input("введите U and I :").split()]
# # print(f"Voltimetr :{(numbers[0] / numbers[1]) * (1 - (numbers[1] * ) / number[0])}")
# print(f"Voltimetr :{numbers[0] / numbers[1]}")



# while True:
#     numbers = [float(i) for i in input("введите U and I :").split()]
#     # print(f"Voltimetr :{(numbers[0] / numbers[1]) * (1 - (numbers[1] * ) / number[0])}")
#     # print(f"Voltimetr :{numbers[0] / numbers[1]}")

# import re

# def square_generator(number):
#     for i in range(1, number + 1):
#         yield i ** 2

# for i in square_generator(5):
#     print(i)


# square = (i ** 2 for i in range(5))

# for i in square:
#     print(i)



# class SquareGenerator:
#     def __init__(self, n):
#         self.n = n
#         self.current = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current <= self.n:
#             square = self.current ** 2
#             self.current += 1
#             return square
#         else:
#             raise StopIteration

# gen = SquareGenerator(5)


# for i in gen:
#     print(square)




# pattern = r"(\d+) (\d+)"

# string = input()

# idk = re.match(pattern, string)

# if idk:
#     print("Первая группа:", idk.group(1))
#     print("Вторая группа:", idk.group(2))
#     print("Все группы:", idk.groups())
# else:
#     print("Совпадение не найдено")


# import os
from colorama import Fore, Back, Style

# path = os.getcwd()

# for entry in os.listdir(path):
#     full_path = os.path.join(path, entry)

#     if os.path.isdir(full_path):
#         print(Back.GREEN + entry)

print(Style.RESET_ALL)
string = input().replace(".", "")
print(string)