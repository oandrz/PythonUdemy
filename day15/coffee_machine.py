from enum import Enum

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

"""
Functional
- show menu -> what would you like? input (string) : espresso, latte, cappuccino, report, off else wrong menu 

- report -> 
show:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
-Q what is the initial value for the resources ?

- Insert coin -> asking the money inserted based on the type
quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
-- Validation insert money, if not enough print “Sorry that's not enough money. Money refunded.”.
-- Change when money > price print “Here is $2.45 dollars in change.” 2 decimal places
-- transaction done print “Here is your latte. Enjoy!”


Non Functional
- infinite loop menu
- resource validation, if less than requirement print : “Sorry there is not enough %resources%.”
- Save profit and resource deduction after buy (state saving)
"""

KEY_WATER = "water"
KEY_MILK = "milk"
KEY_COFFEE = "coffee"
KEY_MONEY = "money"
KEY_INGREDIENTS = "ingredients"
KEY_COST = "cost"

class CoffeeMenu(Enum):
    ESPRESSO = "espresso"
    LATTE = "latte"
    CAPPUCCINO = "cappuccino"
    REPORT = "report"
    OFF = "off"


def handle_report():
    print(f'''
Water: "{resources[KEY_WATER]} ml"
Milk: "{resources[KEY_MILK]} ml"
Coffee: "{resources[KEY_COFFEE]} ml"
Money: "${resources[KEY_MONEY]}"
    ''')


def handle_action(action):
    if action.lower() == CoffeeMenu.ESPRESSO.value:
        handle_order(CoffeeMenu.ESPRESSO.value)
    elif action.lower() == CoffeeMenu.LATTE.value:
        handle_order(CoffeeMenu.LATTE.value)
    elif action.lower() == CoffeeMenu.CAPPUCCINO.value:
        handle_order(CoffeeMenu.CAPPUCCINO.value)
    elif action.lower() == CoffeeMenu.REPORT.value:
        print("Thank you for using our services!")
        handle_report()
    elif action.lower() == "exit":
        exit()
    else:
        print("The machine doesn't has that functionality")

def validate_payment(type, quarters, dimes, nickles, pennies):
    total_money = 0.0
    total_money += float(quarters) * 0.25
    total_money += float(dimes) * 0.10
    total_money += float(nickles) * 0.05
    total_money += float(pennies) * 0.01

    required_balance = MENU[type][KEY_COST]

    return total_money - required_balance

def process_order(type):
    print(f"Here is your {type} ☕️. Enjoy!")
    resources[KEY_MILK] -= MENU[type][KEY_INGREDIENTS].get(KEY_MILK, 0)
    resources[KEY_WATER] -= MENU[type][KEY_INGREDIENTS].get(KEY_WATER, 0)
    resources[KEY_COFFEE] -= MENU[type][KEY_INGREDIENTS].get(KEY_COFFEE, 0)

    resources[KEY_MONEY] += MENU[type][KEY_COST]

def handle_order(type):
    print("Please insert coins.")
    quarters = input("how many quarters?: ")
    dimes = input("how many dimes?: ")
    nickles = input("how many nickles?: ")
    pennies = input("how many pennies?: ")

    change = validate_payment(type, quarters, dimes, nickles, pennies)
    if change >= 0:
        process_order(type)
        print(f"Here is ${round(change, 2)} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")


if __name__ == "__main__":
    while True:
        menu = input("What would you like? ")
        if menu.lower() == CoffeeMenu.OFF.value:
            print("Thank you for using this machine")
            break
        handle_action(menu)
