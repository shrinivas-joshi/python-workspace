from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_running = True
while machine_running:
    user_choice = input(f"What would you like to have? ({menu.get_items()}):").lower()
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        machine_running = False
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            amount = money_machine.process_coins()
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)