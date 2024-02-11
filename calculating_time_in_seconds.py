hours=int(input("Enter digits for hours:  "))
minutes=int(input("Enter digits for minutes:  "))
seconds=int(input("Enter digit for seconds:  "))
total_seconds=(hours*3600)+(minutes*60)+seconds

print("The total seconds is = {}".format(total_seconds),"seconds")
