# digits = [1, 1, 3, 4, 5, 3, 7, 4, 9]
#
# non_duplicates = [dig for dig in digits if digits.count(dig) == 1]
# print(non_duplicates)

bags = [2, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8]

non_dupplicates = [num for num in bags if bags.count(num) != 1]
print(non_dupplicates)
