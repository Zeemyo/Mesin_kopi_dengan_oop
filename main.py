from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

mesin_nyala = True

while mesin_nyala:
    options = menu.get_items()

    pilihan = input(f"Berikut jenis Kopi yang tersedia: ({options}): ").lower()
    if pilihan == "off":
        mesin_nyala = False
    elif pilihan == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        minuman = menu.find_drink(pilihan)

        if coffee_maker.is_resource_sufficient(minuman) and money_machine.make_payment(minuman.cost):
            coffee_maker.make_coffee(minuman)




