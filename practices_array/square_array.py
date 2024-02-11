import array

array_num = array.array('i', [2, 3, 4, 5, 6, 7, 8])

array_len = str(len(array_num))
print(array_len)

array_square = [n**3 for n in array_num]
print(array_square)
