class Upstring:
    def __init__(self,string: str) -> None:
        self.__string = string
    
    def getString(self):
        return self.__string
    
    def printString(self):
        print(self.__string.upper())

#Проверка работает ли корректно наш класс Апстринг
        
def main():
    string =  Upstring(string = input())
    string.printString()

if __name__ == "__main__":
    main()

#Все корректно работает