# print if the given year is a lead year or not
year = int(input())

# leap year logic:
# year divisiable by 4 and not divisiable by 100 or divisiable by 400 is a leap yeaer

print("Leap Year" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "Not a leap year")