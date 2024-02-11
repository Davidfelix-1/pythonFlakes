total_seconds=int(input("Enter the digit for seconds:  "))
hours=total_seconds//3600
minute=(total_seconds%3600)//60
seconds=(total_seconds%3600)%60

print("Hours = {}".format(hours))
print("Minutes = {}".format(minute))
print("Seconds = {}".format(seconds))