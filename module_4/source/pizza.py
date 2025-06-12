class Pizza:
    """A class representing a pizza order."""

    crusts = {"Thin": 5, "Thick": 6, "Gluten Free": 8}
    sauces = {"Marinara": 2, "Pesto": 3, "Liv Sauce": 5}
    toppings = {"Pineapple": 1, "Pepperoni": 2, "Mushrooms": 3}
    cheeses = {"Mozzarella": 0}

    def __init__(self, crust: str, sauce: str, cheese: str, toppings: list[str]):
        """Initialize a pizza with crust, sauce, cheese, and toppings."""
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings  # list of topping names

    def __str__(self) -> str:
        """Return a string representation of the pizza."""
        toppings_str = ', '.join(self.toppings) if self.toppings else "no toppings"
        return (
            f"Pizza with {self.crust} crust, {self.sauce} sauce, {self.cheese} cheese, "
            f"and toppings: {toppings_str}. Cost: ${self.cost():.2f}"
        )

    def cost(self) -> float:
        """Calculate the total cost of the pizza."""
        try:
            total = (
                Pizza.crusts[self.crust]
                + Pizza.sauces[self.sauce]
                + Pizza.cheeses[self.cheese]
                + sum(Pizza.toppings[topping] for topping in self.toppings if topping in Pizza.toppings)
            )
        except KeyError as e:
            raise ValueError(f"Invalid pizza component: {e}")
        return float(total)