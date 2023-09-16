# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    for j in range(0, len(numbers) - 1):
        for i in range(0, len(numbers) - 1 - j):
            if numbers[i] < numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
    return numbers


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers


my_list = [1, 4, 6, 32, 43, 5, 2, 3, 4]
print(sort_list_imperative(my_list))
print(sort_list_declarative(my_list))
