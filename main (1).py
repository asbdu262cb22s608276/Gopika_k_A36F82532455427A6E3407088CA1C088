#get the year input from the user

year=int(input("enter a year:"))

#check if its a leap year
if(year%4==0 and year%100!=0)or(year%400==0):
  print(f"{year} is a leaf year:")
else:
  print(f"{year} is not a leaf year:")