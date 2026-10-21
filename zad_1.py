class Student:

    def __init__(self, name: str, marks: list[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return True if sum(self.marks)/len(self.marks) > 50 else False

    def __str__(self):
        return f"Imie : {self.name}"
if __name__ == "__main__":

    student = Student("Jan", [55,70,100,40,90])
    student2 = Student("Ambroży", [55,10,10,40,30])

    def check(student):
        if student.is_passed():
            print("Zdał")
        else:
            print("Nie zdał")

    check(student)
    check(student2)