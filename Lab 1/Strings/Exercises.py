#Exercises
x = "Hello World!"
print(len(x)) #Можно использовать это для всех контейнеров

txt = "Hello World!"
x = txt[0] #Можно использовать это для всех контейнеров

x = txt[2:5:] #Срезы так же для всех контейнеров кроме словаря

txt = " Hello World "
x = txt.strip() #Пробелы удалятся

txt = txt.upper() #Все на заглавной букве

txt = txt.lower() #Теперь на нижнем регистре

txt.replace("h", "j") #Заменяет 

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #Я бы все же предпочел f-строки