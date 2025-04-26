cash=0
menu={
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24
        },
        'cost':150
    },
    
    'espresso': {
            'ingredients': {
                'water': 50,
                'coffee': 18
            },
            'cost': 100
        },

        'cappuccino': {
            'ingredients': {
                'water': 250,
                'milk': 100,
                'coffee': 24
            },
            'cost': 200
        }   
    }
def collect_coins():
    print("Please insert coins ")
    five= int(input("How many 5 coins? "))
    ten= int(input("How many 10 coins? "))
    twenty= int(input("How many 20 coins? "))
    sum= (five*5)+(ten*10)+(twenty*20)
    return sum

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def payment_process(money,drink_cost):
    if money>=drink_cost:
        change=money-drink_cost
        print(f"Here is your change {change}.")
        global cash
        cash+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

resources= {
    'water': 300,
    'milk': 500,
    'coffee': 350
}

flag=False
while not flag:
    choice=input("What would you like? (latte/espresso/cappuccino): ")
    if choice=='off':
        flag=True
    elif choice=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${cash}")
    else:
        drink=menu[choice]
        if check_resources(drink['ingredients']):
            payment=collect_coins()
            if payment_process(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])
        else:
            print("Sorry, we don't have enough resources to make that drink.")
    print("Thank you for using the coffee machine!")