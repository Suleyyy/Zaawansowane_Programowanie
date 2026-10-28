class Student:

    def __init__(self, name: str, marks: list[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return True if sum(self.marks) / len(self.marks) > 50 else False

    def __str__(self):
        return f"Imie : {self.name}"
