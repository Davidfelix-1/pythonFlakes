padlocks = [2, 3, 4, 5, 6]


def sum_list(items):
    sum_numbers = 0
    for item in items: sum_numbers += item
    return sum_numbers


print(sum_list(padlocks))
