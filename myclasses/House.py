from myclasses import Property


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return super().__str__() + f"\nRozmiar działki (m^2): {self.plot}\n"
