
from pizza import *
import pizza

# This function shows a limitation on tool-assisted
# refactoring in a dynamic language like Python.
#
# When you rename the Pizza getPrice method to get_price,
# does it rename the method here?
# - if no type annotation on the pizza parameter, maybe not
# - if use type annotation ':Pizza' on the parameter, it should

def order_pizza(pizza):
    """Print a description of a pizza, along with its price."""

    # create printable description of the pizza such as
    # "small pizza with muschroom" or "small plain pizza"
    description = pizza.size
    if pizza.toppings:
        description += " pizza with "+ ", ".join(pizza.toppings)
    else:
        description += " plain cheeze pizza"
    print(f"A {description}")
    print("Price:", pizza.get_price())


if __name__ == "__main__":
    pizza1 = Pizza(pizza.SMALL)
    pizza1.add_topping("mushroom")
    pizza1.add_topping("tomato")
    pizza1.add_topping("pinapple")
    order_pizza(pizza1)

    # a plain pizza
    pizza2 = Pizza(pizza.MEDIUM)
    order_pizza(pizza2)

    # pizza with only one topping
    pizza3 = Pizza(pizza.LARGE)
    pizza3.add_topping("seafood")
    order_pizza(pizza3)
