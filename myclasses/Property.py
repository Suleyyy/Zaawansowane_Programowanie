class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Powierzchnia (m^2): {self.area}\nLiczba pokoi: {self.rooms}\nCena (zł): {self.price}\nAdres: {self.address}"
