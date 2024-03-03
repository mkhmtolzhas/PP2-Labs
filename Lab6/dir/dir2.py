import os

path = input()


if not os.path.exists(path):
    print("Путь не существует")

if not os.access(path, os.R_OK):
    print("Нет доступа для чтения")
else:
    print("Доступ для чтения")

if not os.access(path, os.W_OK):
    print("Нет доступа для записи")
else:
    print("Доступ для записи")

if not os.access(path, os.X_OK):
    print("Нет доступа для исполнения")
else:
    print("Доступ для исполнения")