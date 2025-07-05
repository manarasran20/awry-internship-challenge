from datetime import datetime, timedelta

class Product:
    def __init__(self, name, price, quantity, weight=0, expiry=None, need_shipping=False):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.weight = weight
        self.expiry = expiry
        self.need_shipping = need_shipping

    def is_expired(self):
        return datetime.now() > self.expiry if self.expiry else False

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class CartItem:
    def __init__(self, prod, qty):
        self.prod = prod
        self.qty = qty

class Cart:
    def __init__(self):
        self.things = []

    def add(self, prod, qty):
        if prod.quantity < qty:
            raise Exception(f"Sorry, only {prod.quantity} {prod.name} left.")
        self.things.append(CartItem(prod, qty))

class ShippingService:
    @staticmethod
    def send(items):
        print("** Shipment notice **")
        total_weight = 0.0
        for i in items:
            name = i['prod'].getName()
            weight = i['prod'].getWeight() * i['qty']
            print(f"{i['qty']}x {name}\t{int(weight * 1000)}g")
            total_weight += weight
        print("Total package weight", round(total_weight, 1), "kg\n")
        return total_weight

def checkout(person, cart):
    if not cart.things:
        raise Exception("Cart is still empty!")

    total = 0
    shipList = []

    for thing in cart.things:
        p = thing.prod
        if p.is_expired():
            raise Exception(f"{p.name} is expired already.")
        if p.quantity < thing.qty:
            raise Exception(f"Not enough {p.name} in stock.")
        total += p.price * thing.qty
        if p.need_shipping:
            shipList.append({'prod': p, 'qty': thing.qty})

    shipCost = 0
    if shipList:
        weight = ShippingService.send(shipList)
        shipCost = int(weight * 30)

    grand = total + shipCost

    if person.balance < grand:
        raise Exception("Not enough balance to complete order.")

    person.balance -= grand

    print("** Checkout receipt **")
    for thing in cart.things:
        print(f"{thing.qty}x {thing.prod.name} \t{thing.qty * thing.prod.price}")

    print("Subtotal \t", total)
    print("Shipping \t", shipCost)
    print("Amount \t\t", grand)
    print("Remaining Balance: ", person.balance)

# Testing it
cheese = Product("Cheese", 100, 10, 0.2, datetime.now() + timedelta(days=2), True)
biscuit = Product("Biscuits", 150, 5, 0.7, datetime.now() + timedelta(days=5), True)
tv = Product("TV", 3000, 3, 10.0, None, True)
card = Product("Scratch Card", 50, 100, 0, None, False)

user = Customer("Manar", 1000)
basket = Cart()
basket.add(cheese, 2)
basket.add(biscuit, 1)

checkout(user, basket)
