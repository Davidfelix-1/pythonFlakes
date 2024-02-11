numbers = [2, 3, 5, 6, 7, 2]

# adding_indexes = [num for num in numbers if numbers.count(num) == 1]
# print('adding_indexes', )

# for num in numbers:
#     for num2 in numbers:
#         if num == num2:
#             print(num + num2)
#
temp = []
for number in range(0, len(numbers), 2):
    numbers.insert(number + 1, number +2)
    print(number)

