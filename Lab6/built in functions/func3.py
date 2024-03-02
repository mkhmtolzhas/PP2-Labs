string = input()

string2 = ''
for i in reversed(string):
    string2+=i

print(string == string2)
print(string == string[::-1])