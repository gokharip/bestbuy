class Product:

    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("The name field cannot be blank")
        self.name = name
        if price <= 0:
            raise ValueError("The price field cannot be less than 0")
        self.price = price
        if quantity <= 0:
            raise ValueError("The quantity field cannot be less than 0")
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity < 1:
            self.active = False

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(self.name + ", " + "Price: " + str(self.price) + ",  " + "Quantity: " + str(self.quantity))

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError("Not enough quantity")
        self.quantity -= quantity
        return float(quantity * self.price)

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()
