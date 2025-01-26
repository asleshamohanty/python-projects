from menu import MENU
from menu import resources

run_machine = True
money = []

def sufficient(product):
    for item in resources:
        if resources[item] < MENU[product]["ingredients"][item]:
            print(f"Sorry there is not enough {item} available")

def making_coffee(product):
    for item in resources:
        resources[item] -= MENU[product]["ingredients"][item]
    print(f"Here is your {product}, enjoy!!")

def process_coins(product):
    print("Insert coins: ")
    total = (0.25*(float(input("Quarters: "))))+(0.10*(float(input("Dimes: "))))+(0.05*(float(input("Nickles: "))))+(0.01*(float(input("Pennies: "))))
    if total == MENU[product]["cost"]:
        print("Money Received. Your change is $0")
        money.append(total)
        making_coffee(product)
    elif total > MENU[product]["cost"]:
        change = total - (MENU[product]["cost"])
        print(f"Money Received. Your change is ${round(change,2)}")
        money.append(total - change)
        making_coffee(product)
    else:
        print("Sorry that's not enough. Money refunded.")
        run_machine = False
   

while run_machine:
    option = input("What would you like?(espresso/latte/cappuccino): ")
    if option == "off":
        print("The Coffee Machine has been switched off")
        run_machine = False
    elif option == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${sum(money)}")
    elif option == "latte":
        sufficient("latte")
        process_coins("latte")
    elif option == "cappuccino":
        sufficient("cappuccino")
        process_coins("cappuccino")
    elif option == "espresso":
        sufficient("espresso")
        process_coins("espresso")
        