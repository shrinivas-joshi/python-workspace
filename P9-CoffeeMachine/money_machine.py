class MoneyMachine:
    CURRENCY = "Rs."

    COIN_VALUES = {
        "ones": 1,
        "twos": 2,
        "fives": 5,
        "tens": 10
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("Please insert the coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded")
            self.money_received = 0
            return False
