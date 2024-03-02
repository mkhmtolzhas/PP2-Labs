import os

os.path = "./"

with open("func1.py", "a") as code:
    code.write("print('Hello World!')")