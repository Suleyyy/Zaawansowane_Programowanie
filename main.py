from myclasses.Student import Student

student = Student("Jan", [55, 70, 100, 40, 90])
student2 = Student("Ambroży", [55, 10, 10, 40, 30])

def check(stud):
    if stud.is_passed():
        print("Zdał")
    else:
        print("Nie zdał")

check(student)
check(student2)