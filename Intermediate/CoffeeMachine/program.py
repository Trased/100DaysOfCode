import menu

if __name__ == "__main__":
    wrong = True
    while wrong:
        pick = input("What would you like? (espresso/latte/cappuccino): ")
        if pick in menu.MENU:
            if menu.resources["money"] < menu.MENU[pick]["cost"]:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            if (menu.resources["water"] > menu.MENU[pick]["ingredients"]["water"] and
                    menu.resources["milk"] > menu.MENU[pick]["ingredients"]["milk"] and
                    menu.resources["coffee"] > menu.MENU[pick]["ingredients"]["coffee"]):
                total -= menu.MENU[pick]["cost"]
                if total > 0:
                    menu.resources["money"] = round(total, 1)
                print(f"Here is your {pick}. Enjoy!")
                menu.resources["water"] -= menu.MENU[pick]["ingredients"]["water"]
                menu.resources["milk"] -= menu.MENU[pick]["ingredients"]["milk"]
                menu.resources["coffee"] -= menu.MENU[pick]["ingredients"]["coffee"]
            else:
                print("Sorry, there are not enough resources. You've got your money back!")
        elif pick == "report":
            print(menu.resources["water"])
            print(menu.resources["milk"])
            print(menu.resources["coffee"])
            print(menu.resources["money"])
        else:
            print("Incorrect input, retry!")

        pick = input("Retry / redo? 'y' or 'n'")
        if pick == 'n':
            wrong = False


        

