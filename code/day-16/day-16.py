# # import module

# # print(module.i)

# import turtle


# mike = turtle.Turtle()
# mike.shape("turtle")
# mike.color("red")
# mike.forward(200)



# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.exitonclick()


# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon name", ["Pikachu","Squirtle","Charmander"])
# table.add_column( "Type", ["Electric", "Water","Fire"] )
# table.align = "l"
# print(table)


#Coffee maker machine

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
