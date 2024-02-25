import re

snake_case_words = re.split(r"[_]", input())
print(snake_case_words[0], end='')
for i in range(1, len(snake_case_words)):
    words = snake_case_words[i][0].upper() + snake_case_words[i][1:]
    print(words, end="")