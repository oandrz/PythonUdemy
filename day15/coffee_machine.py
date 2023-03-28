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
    "money": 0
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

class CoffeeMenu(Enum):
    ESPRESSO = "espresso"
    LATTE = "latte"
    CAPPUCCINO = "cappuccino"
    REPORT = "report"
    OFF = "off"


def handle_drink(menu):
    print("handle_drink")


def handle_report():
    print(f'''
Water: "{resources[KEY_WATER]}ml"
Milk: "{resources[KEY_MILK]}ml"
Coffee: "{resources[KEY_COFFEE]}ml"
Money: "${resources[KEY_MONEY]}"
    ''')


def handle_action(action):
    if action.lower() == CoffeeMenu.ESPRESSO.value:
        print("espresso")
    elif action.lower() == CoffeeMenu.LATTE.value:
        print("latte")
    elif action.lower() == CoffeeMenu.CAPPUCCINO.value:
        print("latte")
    elif action.lower() == CoffeeMenu.REPORT.value:
        handle_report()
    else:
        print("The machine doesn't has that functionality")


if __name__ == "__main__":
    while True:
        menu = input("What would you like? ")
        if menu.lower() == CoffeeMenu.OFF.value:
            print("Thank you for using this machine")
            break
        handle_action(menu)
