from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    menu = Menu()
    coffeeMaker = CoffeeMaker()
    moneyMachine = MoneyMachine()
    repeat = True
    while repeat:
        pick = input(f"What would you like? ({menu.get_items()}): ")
        if pick == "report":
            moneyMachine.report()
            coffeeMaker.report()
        elif menu.find_drink(pick):
            if coffeeMaker.is_resource_sufficient(menu.find_drink(pick)):
                if moneyMachine.make_payment(menu.find_drink(pick).cost):
                    coffeeMaker.make_coffee(menu.find_drink(pick))

        pick = input("Do you want something else? 'y' or 'n'")
        if pick == "n":
            repeat = False








