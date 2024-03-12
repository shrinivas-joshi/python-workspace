class MenuItem:
    def __init__(self, water, milk, coffee, name, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=25.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=15.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=55.0)
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            print(item.name)
            print(order_name)
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")