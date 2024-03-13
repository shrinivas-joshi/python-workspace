class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(
            f"Water : {self.resources['water']}ml\n"
            f"Milk: {self.resources['milk']}ml\n"
            f"Coffee: {self.resources['coffee']}gm"
        )

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if self.resources[item] < drink.ingredients[item]:
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy")
