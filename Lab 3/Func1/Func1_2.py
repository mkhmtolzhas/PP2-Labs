def fahrenheit_to_centigrade(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def main():
    fahrenheit = int(input("Введи значения в фаренгейте: "))
    print(f"Ваш ответ: {fahrenheit_to_centigrade(fahrenheit)}")
if __name__ == "__main__":
    main()
