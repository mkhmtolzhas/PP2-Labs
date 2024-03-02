# import math
# import functools
# import operator


# def f(head, tail, acc):
#     if head == None: return acc
#     if len(tail) == 0: return acc * head
#     return f(tail[0], tail[1:], acc * head)

# numbers = [int(i) for i in input().split()]
# print(f(numbers[0], numbers[1:], 1))
# print(math.prod(numbers))
# print(functools.reduce(operator.mul, numbers))
def recursive_sum(arr):
    total_sum = 0
    for element in arr:
        if isinstance(element, list):
            total_sum += recursive_sum(element)
        else:
            total_sum += element
    return total_sum


numbers = [int(i) for i in input().split()]
if len(numbers) == 1:
    print(numbers[0])
else:
    numbers_2 = []
    for i in range(1, len(numbers)):
        if numbers_2 == []:
            numbers_2.append([numbers[0]] * numbers[i])
        else:
            numbers_2.append([numbers_2[i-2]] * numbers[i])

    print(recursive_sum(numbers_2[-1]))

# for i in numbers_2[-1]:
sum_of_this = 1
for i in numbers[1:]:
    sum_of_this *= i
print(sum([numbers[0] * sum_of_this] ))

# for i in sum_number:
#     answer[su]
