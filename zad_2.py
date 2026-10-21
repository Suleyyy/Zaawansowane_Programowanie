from zad_1 import Student


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka | Adres: {self.zip_code} {self.city}, ul. {self.street} | "
            f"Godziny otwarcia: {self.open_hours} | Tel: {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name} (Tel: {self.phone})"


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: str,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka: '{self.author_name} {self.author_surname}' - "
            f"Stron: {self.number_of_pages} (Wydana: {self.publication_date}) | "
            f"Lokalizacja: {self.library.city}"
        )


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


biblio1 = Library("Warszawa", "Koszykowa 26", "00-950", "08:00 - 20:00", "22 537 41 00")
biblio2 = Library("Kraków", "Rajska 1", "31-124", "09:00 - 19:00", "12 375 22 00")

ks1 = Book(biblio1, "1954", "Witold", "Gombrowicz", "280")
ks2 = Book(biblio1, "1961", "Stanisław", "Lem", "210")
ks3 = Book(biblio2, "1896", "Henryk", "Sienkiewicz", "550")
ks4 = Book(biblio2, "1937", "Bruno", "Schulz", "180")
ks5 = Book(biblio1, "1924", "Władysław", "Reymont", "620")

emp1 = Employee(
    "Jan",
    "Kowalski",
    "2020-01-15",
    "1985-04-12",
    "Warszawa",
    "Prosta 5",
    "00-001",
    "501 111 222",
)
emp2 = Employee(
    "Anna",
    "Nowak",
    "2018-06-01",
    "1990-11-23",
    "Kraków",
    "Długa 12",
    "30-002",
    "502 333 444",
)
emp3 = Employee(
    "Piotr",
    "Wiśniewski",
    "2022-09-10",
    "1995-02-28",
    "Warszawa",
    "Polna 8",
    "00-002",
    "503 555 666",
)

std1 = Student("Michał", [])
std2 = Student("Katarzyna", [])
std3 = Student("Tomasz", [])


zam1 = Order(employee=emp1, student=std1, books=[ks1, ks2], order_date="2026-10-21")

zam2 = Order(
    employee=emp2, student=std2, books=[ks3, ks4, ks5], order_date="2026-10-22"
)


print("=== ZAMÓWIENIE 1 ===")
print(zam1)

print("\n=== ZAMÓWIENIE 2 ===")
print(zam2)
