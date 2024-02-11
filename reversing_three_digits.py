print("enter three digits: ")
nums=int(input())
first_d=nums//100
middle_d=(nums//10)%10
last_d=nums%10
rev=last_d*100+middle_d*10+first_d
print("Reversed output of input is={}".format(rev))
