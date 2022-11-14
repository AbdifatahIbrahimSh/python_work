def make_pizza(size, *toppings):
    """Make pizza"""
    print(f"\nMaking {size}-inch pizza for the following toppings:")
    for topping in toppings:
        print(f" - {topping.title()}")


