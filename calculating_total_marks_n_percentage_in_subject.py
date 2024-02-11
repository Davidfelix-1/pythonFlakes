e=int(input('English '))
m=int(input('Maths '))
h=int(input('History '))
g=int(input('Geography '))
c=int(input('Computer '))
total=e+m+h+g+c
per=(total/500.0)*100
print('total marks={}'.format(total))
print("percentages of marks= {:.2f}".format(per))



english=int(input("enter score for English: "))
mathematics=int(input(" enter score for Maths: "))
history=int(input(" enter score for History: "))
geography=int(input(" enter score for Geography:  "))
computer=int(input(" enter score for Computer:  "))

total=english+mathematics+history+geography+computer
perc=(total/500.0)*100

print("Total Marks= {}".format(total))
print("Percentage of Marks= {}".format(perc))