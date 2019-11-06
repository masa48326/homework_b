'''
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
'''


def sum(numbers):
    sum_number = 0
    for num in numbers:
        sum_number += num

    return sum_number


def maximum(numbers):
    max_number = numbers[0]
    for i in range(1, len(numbers)):
        if max_number < numbers[i]:
            max_number = numbers[i]

    return max_number


def minimum(numbers):
    min_number = numbers[0]
    for i in range(1, len(numbers)):
        if min_number > numbers[i]:
            min_number = numbers[i]

    return min_number


def average(numbers):
    sum_number = sum(numbers)
    return sum_number / len(numbers)


input_str = input('データを入力してください(スペース区切り) > ')
number_list = []
for s in input_str.split(' '):
    number_list.append(int(s))

print(f'合計値: {sum(number_list)}')
print(f'最大値: {maximum(number_list)}')
print(f'最小値: {minimum(number_list)}')
print(f'平均値: {average(number_list)}')
