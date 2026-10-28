class Chair:
    def __init__(self, name, color, price, material):
        self.name = name
        self.color = color
        self.price = price
        self.material = material

    def set_price(self, new_price):
        self.price = new_price

    def show(self):
        print(self.name, "|", self.color, "|", self.price, "грн |", self.material)


chairs = [
    Chair("Офісний", "чорний", 1500, "тканина"),
    Chair("Кухонний", "білий", 800, "пластик"),
    Chair("Барний", "сірий", 1200, "метал"),
    Chair("Класичний", "коричневий", 2100, "дерево"),
]

print("Список стільців:")
for chair in chairs:
    chair.show()

chairs[1].set_price(950)
chairs[3].set_price(1900)

print()
print("Після зміни ціни:")
for chair in chairs:
    chair.show()
