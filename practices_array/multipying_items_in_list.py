def list_multiplication(nums):
    temp = 0
    for i in nums:
        temp *= i
    return temp


n = [2, 3, 4]

print(list_multiplication(n))
