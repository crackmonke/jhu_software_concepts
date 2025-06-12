class Pizza:
    """
    A class representing a pizza order.

    Attributes
    ----------
    crusts : dict
        Available crust types and their prices.
    sauces : dict
        Available sauces and their prices.
    toppings : dict
        Available toppings and their prices.
    cheeses : dict
        Available cheeses and their prices.
    crust : str
        The crust type for this pizza.
    sauce : list[str]
        The sauces for this pizza.
    cheese : str
        The cheese for this pizza.
    toppings : list[str]
        The toppings for this pizza.
    """

    crusts = {"Thin": 5, "Thick": 6, "Gluten Free": 8}
    sauces = {"Marinara": 2, "Pesto": 3, "Liv Sauce": 5}
    toppings = {"Pineapple": 1, "Pepperoni": 2, "Mushrooms": 3}
    cheeses = {"Mozzarella": 0}

    def __init__(self, crust: str, sauce: list[str], cheese: str, toppings: list[str]):
        """
        Initialize a pizza with crust, sauces, cheese, and toppings.

        Parameters
        ----------
        crust : str
            The crust type.
        sauce : list[str]
            List of sauces.
        cheese : str
            The cheese type.
        toppings : list[str]
            List of toppings.
        """
        self.crust = crust
        self.sauce = sauce  # list of sauce names
        self.cheese = cheese
        self.toppings = toppings  # list of topping names

    def __str__(self) -> str:
        """
        Return a string representation of the pizza.

        Returns
        -------
        str
            A formatted string describing the pizza and its cost.
        """
        sauces_str = ', '.join(self.sauce) if self.sauce else "no sauces"
        toppings_str = ', '.join(self.toppings) if self.toppings else "no toppings"
        return (
            f"Pizza with {self.crust} crust, {sauces_str} sauce(s), {self.cheese} cheese, "
            f"and toppings: {toppings_str}. Cost: ${self.cost():.2f}"
        )

    def cost(self) -> float:
        """
        Calculate the total cost of the pizza.

        Returns
        -------
        float
            The total price of the pizza.

        Raises
        ------
        ValueError
            If an invalid pizza component is provided.
        """
        try:
            total = (
                Pizza.crusts[self.crust]
                + sum(Pizza.sauces[s] for s in self.sauce if s in Pizza.sauces)
                + Pizza.cheeses[self.cheese]
                + sum(Pizza.toppings[topping] for topping in self.toppings if topping in Pizza.toppings)
            )
        except KeyError as e:
            raise ValueError(f"Invalid pizza component: {e}")
        return float(total)