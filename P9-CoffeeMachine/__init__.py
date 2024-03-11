MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def printReport(current_resources):
    print(
        f"Water : {current_resources['water']}ml\n"
        f"Milk: {current_resources['milk']}ml\n"
        f"Coffee: {current_resources['coffee']}gm\n"
        f"Money: Rs.{current_resources['money']}")


def checkResources(name_of_drink):
    drink_ingredients = MENU[name_of_drink]['ingredients']
    if resources['water'] >= drink_ingredients['water']:
        if resources['milk'] >= drink_ingredients['milk']:
            if resources['coffee'] >= drink_ingredients['coffee']:
                return "True"
            else:
                return 'coffee'
        else:
            return "milk"
    else:
        return "water"


def calculate_payment(one_rup, two_rup, five_rup, ten_rup):
    return (one_rup * 1.0) + (two_rup * 2.0) + (five_rup * 5.0) + (ten_rup * 10.0)


def payment_Result(cost_of_drink):
    print("Please insert the coins.")
    ones = float(input("How many one rupees? "))
    twos = float(input("How many two rupees? "))
    fives = float(input("How many five rupees? "))
    tens = float(input("How many ten rupees? "))
    total_payment = calculate_payment(ones, twos, fives, tens)
    print(total_payment)
    if total_payment < cost_of_drink:
        return "Fail"
    else:
        resources['money'] += cost_of_drink
        return total_payment - cost_of_drink


def makeDrink(name_of_drink):
    drink = MENU[name_of_drink]['ingredients']
    resources['water'] = resources['water'] - drink['water']
    resources['milk'] = resources['milk'] - drink['milk']
    resources['coffee'] = resources['coffee'] - drink['coffee']


def startDrinkPrep(name_of_drink):
    resource_available = checkResources(name_of_drink)
    if resource_available == "True":
        payment = payment_Result(MENU[name_of_drink]['cost'])
        if payment != "Fail":
            print(f"Here is the Rs.{payment} in change")
            makeDrink(name_of_drink)
        else:
            print("Sorry that's not enough money. Money Refunded")
    else:
        print(f"Sorry there is not enough {resource_available}")


machine_running = True
resources["money"] = 0
while machine_running:
    user_choice = input("What would you like to have ? (espresso/latte/cappuccino):").lower()
    if user_choice == "report":
        printReport(resources)
    elif user_choice == "off":
        machine_running = False
    else:
        startDrinkPrep(user_choice)
