print('enter digits')
num=int(input())
fd=num//10
ld=num%10
product=fd*ld
print("first digit of input is ={}".format(fd))
print("last digit of input is={}".format(ld))
print("the product of inputs first n last digit is={}".format(product))