# Задача- 1: У вас есть массив целых чисел, в котором каждое число, кроме одного,
# повторяется дважды. Вам нужно найти это одиночное число.

def find_number(numbers):
    num_len = len(numbers)
    num = None
    for j in range(0, num_len - 1):
        for i in range(0, num_len - 1 - j):
            if numbers[i] < numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
    for k in range(0, num_len - 1, 2):
        if numbers[k] != numbers[k + 1]:
            num = numbers[k]
            break
    return num


my_list = [1, 4, 6, 32, 43, 5, 2, 3, 4, 1, 6, 43, 5, 2, 3]
print(find_number(my_list))
