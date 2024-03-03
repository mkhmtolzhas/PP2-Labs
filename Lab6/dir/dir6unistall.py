import os

path = "."

for i in range(ord('A'), ord('Z') + 1):
    os.remove(f"{path}/{chr(i)}.txt")
    print(f"{chr(i)}.txt was deleted")