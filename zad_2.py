from myclasses import Book, Employee, Student, Library, Order

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
