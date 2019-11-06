'''
サイコロの面の数は?: 8
何回振りますか?: 20
[6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]
'''
import random

dice_list = []
faces = int(input('サイコロの面の数は?: '))
throws = int(input('何回振りますか?: '))

for throw in range(1, 1 + throws):
    dice_list.append(random.randint(1, faces))
print(dice_list)
