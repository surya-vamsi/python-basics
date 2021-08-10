student_name = input("Enter your name:")
marks = {"surya":40,"pavan":50,"key":25}
for student in marks:
    if student_name == student:
        print("Name of student:",student_name)
        print("Scored marks:",marks[student])
        break
else:
    print("Sorry your entry was not registerd")
