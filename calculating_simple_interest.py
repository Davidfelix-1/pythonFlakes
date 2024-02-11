rate=int(input("enter digit for rate:  "))
time=int(input("enter digit for time:  "))
principal=int(input("enter digit for principal:  "))
simple_interest=(principal*rate*time)/100
print("Rate is =", rate)
print("time is =", time)
print("principal is =", principal)
print("Simple interest is ={:.2f}".format(simple_interest))

