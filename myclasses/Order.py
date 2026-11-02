from myclasses import Book, Employee, Student


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: list[Book], order_date: str
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n  - ".join(
            [
                f"{book.author_name} {book.author_surname} (Liczba stron: {book.number_of_pages})"
                for book in self.books
            ]
        )
        return (
            f"Zamówienie z dnia: {self.order_date}\n"
            f"Student: {self.student}\n"
            f"Obsługujący pracownik: {self.employee.first_name} {self.employee.last_name}\n"
            f"Zamówione książki:\n  - {book_list if self.books else 'Brak książek'}"
        )
