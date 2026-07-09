# make a grade calculator
grade = float(input())
if grade >= 90:
    print("A+")
elif 90 > grade >= 80:
    print("A")
elif 80 > grade >= 70:
    print("A-")
elif 70 > grade >= 60:
    print("B")
elif 60 > grade >= 50:
    print("B-")
elif 50 > grade:
    print("F")