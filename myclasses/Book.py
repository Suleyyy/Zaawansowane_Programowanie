from myclasses.Library import Library


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
