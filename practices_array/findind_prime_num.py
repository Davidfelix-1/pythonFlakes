from array import array

array_book = array('i', [25, 67, 89, 45])
array_book2 = array('i', [25, 67, 89, 45])
array_book.extend(array_book2)
print(array_book)
