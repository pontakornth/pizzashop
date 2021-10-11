from enum import Enum


class PizzaSize(Enum):
    small = 120
    medium = 200
    large = 280

    def __str__(self):
        return self.name

    @property
    def price(self):
        return self.value


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size: PizzaSize):
        if not isinstance(size, PizzaSize):
            raise TypeError("size must be PizzaSize")
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        return self.size.price + 20 * len(self.toppings)

    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self):
        description = self.size.name
        if self.toppings:
            description += " pizza with " + ", ".join(self.toppings)
        else:
            description += " plain cheeze pizza"
        return description


if __name__ == '__main__':
    for size in PizzaSize:
        print(size.name, "pizza has price", size.value)
