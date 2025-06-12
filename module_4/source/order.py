class Order:
    """
    Represents a customer's pizza order, which may include multiple pizzas.

    Attributes
    ----------
    pizzas : list
        List of Pizza objects in the order.
    cost : float
        Total cost of the order.
    paid : bool
        Whether the order has been paid for.
    """

    def __init__(self):
        """
        Initialize a new Order with no pizzas, zero cost, and unpaid status.
        """
        self.pizzas = []
        self.cost = 0.0
        self.paid = False

    def __str__(self):
        """
        Return a string summary of the order, listing all pizzas and the total cost.

        Returns
        -------
        str
            A formatted string describing the order.
        """
        order_details = f"Customer Requested:\n"
        for pizza in self.pizzas:
            order_details += str(pizza) + "\n"
        order_details += f"Total Cost: ${self.cost:.2f}\n"
        return order_details

    def input_pizza(self, crust, sauces, cheese, toppings):
        """
        Interactively prompt the user to build one or more pizzas for the order.

        Parameters
        ----------
        crust : str
            Not used (kept for compatibility).
        sauce : list[str]
            Not used (kept for compatibility).
        cheese : str
            Not used (kept for compatibility).
        toppings : list[str]
            Not used (kept for compatibility).

        Returns
        -------
        list
            The list of Pizza objects added to the order.
        """
        from source.pizza import Pizza

        ordering = "yes"
        while ordering == "yes":
            # Prompt for crust type
            while True:
                crust = input("Enter crust type (Thin, Thick, Gluten Free): ").strip().title()
                if crust in Pizza.crusts:
                    break
                print("Invalid crust type. Please try again.")

            # Prompt for sauces (multiple allowed, no duplicates)
            while True:
                sauces_input = input("Enter sauces (Marinara, Pesto, Liv Sauce), separated by commas: ")
                sauces_list = [s.strip().title() for s in sauces_input.split(",")]
                sauces = []
                seen_sauces = set()
                for s in sauces_list:
                    if s in Pizza.sauces and s not in seen_sauces:
                        sauces.append(s)
                        seen_sauces.add(s)
                if sauces:
                    break
                print("Invalid sauces. Please try again.")

            # Prompt for cheese type
            while True:
                cheese = input("Enter cheese type (Mozzarella): ").strip().title()
                if cheese in Pizza.cheeses:
                    break
                print("Invalid cheese type. Please try again.")

            # Prompt for toppings (multiple allowed, no duplicates)
            while True:
                toppings_input = input("Enter toppings (Pineapple, Pepperoni, Mushrooms), separated by commas: ")
                toppings_list = [t.strip().title() for t in toppings_input.split(",")]
                toppings = []
                seen = set()
                for t in toppings_list:
                    if t in Pizza.toppings and t not in seen:
                        toppings.append(t)
                        seen.add(t)
                if toppings:
                    break
                print("Invalid toppings. Please try again.")

            # Create and add the pizza to the order
            pizza = Pizza(crust, sauces, cheese, toppings)
            self.pizzas.append(pizza)
            self.cost += pizza.cost()

            # Ask if the user wants to add another pizza
            while True:
                ordering = input("Would you like to add another pizza? (yes/no): ").strip().lower()
                if ordering in ["yes", "no"]:
                    break
                print("Invalid input. Please enter 'yes' or 'no'.")
            if ordering == "no":
                break

        return self.pizzas

    def order_paid(self):
        """
        Prompt for payment type and mark the order as paid if a valid type is entered.
        """
        payment_type = ""
        while payment_type not in ["cash", "card", "online"]:
            payment_type = input("Enter payment type (cash, card, online): ").strip().lower()
            if payment_type not in ["cash", "card", "online"]:
                print("Invalid payment type. Please enter 'cash', 'card', or 'online'.")
        self.paid = True
        print(f"Thank you for your payment by {payment_type}!")
