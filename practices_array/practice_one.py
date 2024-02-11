import array

balance = array.array('i', [400, 5000, 60, 2000, 567])
balance.insert(2, 666)
balance[1] = 45
# print(balance[2])
# print(balance[2:4])
print(balance)

foot_warehouse = array.array('i', [20, 34, 43, 45, 30])
foot_warehouse.reverse()
print(foot_warehouse)
