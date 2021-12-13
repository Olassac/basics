print("Good morning")
print("student name")
studentname = input()
print("What did you score?")
studentscore = int(input())
if studentscore >= 70 or studentscore <= 100:
    print("A")
elif studentscore >= 60 or studentscore <= 69:
    print("B")
elif studentscore >= 50 or studentscore <= 59:
    print("C")
elif studentscore >= 45 or studentscore <= 49:
    print("D")
elif studentscore >= 40 or studentscore <= 44:
    print("E")
else:
    print("Fail")

