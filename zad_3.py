class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Powierzchnia (m^2): {self.area}\nLiczba pokoi: {self.rooms}\nCena (zł): {self.price}\nAdres: {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f"\nRozmiar działki (m^2): {self.plot}\n"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return super().__str__() + f"\nPiętro: {self.floor}\n"

dom = House(100, 5, 100000, "Katowice ul. Wolności", 1600)
miesz = Flat(100, 5, 100000, "Katowice ul. Wolności", 7)

print(dom)
print(miesz)