class Pizza:

    crusts = {"Thin": 5, "Thick": 6, "Gluten Free": 8}
    sauces = {"Marinara": 2, "Pesto": 3, "Liv Sauce": 5}
    toppings = {"Pineapple": 1, "Pepperoni": 2, "Mushrooms": 3}
    cheeses = {"Mozzarella": 0}

    def __init__(self, crust, sauce, cheese, toppings):
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings  # list of topping names

    def __str__(self):
        return f"Pizza with {self.crust} crust, {self.sauce} sauce, {self.cheese} cheese, and toppings: {', '.join(self.toppings)}. Cost: ${self.cost():.2f}"

    def cost(self):
        total = (
            self.crusts[self.crust]
            + self.sauces[self.sauce]
            + self.cheeses[self.cheese]
            + sum(self.toppings[topping] for topping in self.toppings)
        )
        return float(total)