# import re

# # pattern = r"[A-Za-z0-9]+@[a-z]+\.[a-z]+"


# # print(re.findall(pattern, input()))



# pattern = r"[8(+7)][0-9]{10,11}"
# print(re.findall(pattern, input()))

# from datetime import datetime, timedelta

# # weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]


# # print(weekdays[(datetime.now() + timedelta(days=100)).weekday()])
# print((datetime.now() + timedelta(days=100)).strftime("%A"))


AVERAGE = 0.0777

rs = [float(i) ** 2 for i in input().split()]
print(rs)


