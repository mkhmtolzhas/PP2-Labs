import os

def check_path_existence(path):
    if os.path.exists(path):
        print("Путь существует")
        if os.path.isfile(path):
            print("Имя файла:", os.path.basename(path))
        if os.path.isdir(path):
            print("Часть каталога:", os.path.dirname(path))
    else:
        print("Путь не существует")

path = os.getcwd()
check_path_existence(path)
