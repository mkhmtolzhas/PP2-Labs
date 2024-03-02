bakha = []
for i in input().split():
    bakha.append(True) if i == "y" else bakha.append(False)
print(all(tuple(bakha)))