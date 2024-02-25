import re

with open("row.txt", 'r') as data:
    check = data.read()


list_of_products = re.findall(r'\d+\.\n(.+?)\n', check)
[print(i) for i in list_of_products]
