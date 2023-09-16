#Задача-2: У вас есть массив, содержащий числа от 1 до N, где N - длина массива. Одно из чисел в массиве повторяется дважды,
#а одно число пропущено. Найдите повторяющееся число и пропущенное число.

def find_numbers(numbers):
    num_len = len(numbers)
    num_pair = None
    num_fail = None
    for j in range(0, num_len - 1):
        for i in range(0, num_len - 1 - j):
            if numbers[i] < numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
    for k in range(0, num_len - 1):
        if numbers[k] == numbers[k + 1]:
            num_pair = numbers[k]
        if (numbers[k] - numbers[k+1]) > 1:
            num_fail = numbers[k] - 1
    return [num_pair, num_fail]


my_list = [2, 3, 1, 5, 3]
f_numbers = find_numbers(my_list)
print(f'Повторяющееся число: {f_numbers[0]}')
print(f'Пропущенное число: {f_numbers[1]}')