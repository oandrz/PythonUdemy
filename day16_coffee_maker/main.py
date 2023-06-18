from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def handle_action(action):
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    if action.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    elif action.lower() == "exit":
        print("Thank you for using our services!")
        exit(code=1)
    elif menu.find_drink(order_name=action) is not None:
        menu_item = menu.find_drink(order_name=action)
        is_resource_enough = coffee_maker.is_resource_sufficient(drink=menu_item)
        is_money_enough = money_machine.make_payment(cost=menu_item.cost)
        if  is_resource_enough and is_money_enough:
            coffee_maker.make_coffee(order=menu_item)
    else:
        print("The machine doesn't has that functionality")


if __name__ == "__main__":
    while True:
        menu = input("What would you like? ")
        handle_action(menu)
