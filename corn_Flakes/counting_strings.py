def count_strings_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# input_string = "semicolon"
# print(count_strings_frequency(input_string))
