class Shape:
    def __init__(self) -> None:
        pass
    def area(self):
        print(self.__length ** 2)
"""Я решил эту задачу такой логикой, 
что если по умолчанию длина квадрата будет 0, 
то его площадь тоже будет по умолчанию 0"""
class Square(Shape):
    def __init__(self, length = 0) -> None:
        self.__length = length
    def area(self):
        print(self.__length ** 2)

def main():
    a = Square()
    a.area()

if __name__ == "__main__":
    main()
