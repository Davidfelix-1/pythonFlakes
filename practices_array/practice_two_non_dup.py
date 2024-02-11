# numbers = [2, 3, 3, 5, 6, 7, 6, 9]
#
# duplicate_digit = []
# non_duplicate_digit = []
#
# for number in numbers:
#     if number == number:
#         duplicate_digit += number
#     if number != number:
#         non_duplicate_digit += number
#
# print(duplicate_digit)

numbers = [1, 2, 2, 4, 5, 6, 6, 8]
unique_elements = set(numbers)
for num in numbers:
    if numbers.count(num) == 1:
        unique_elements.add(num)

print(unique_elements)

numberz = [1, 2, 2, 4, 5, 6, 6, 8, 8]
non_duplicates = [num for num in numberz if numberz.count(num) == 1]
print(non_duplicates)
