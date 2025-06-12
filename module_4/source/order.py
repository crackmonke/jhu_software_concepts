class Order:

    def __init__(self):
        # Initializes a customer order
        self.pizzas = []
        self.cost = 0.0
        self.paid = False

    def __str__(self):
        # Prints a customer's order
        order_details = f"Customer Requested:\n"
        for pizza in self.pizzas:
            order_details += str(pizza) + "\n"
        order_details += f"Total Cost: ${self.cost:.2f}\n"
        return order_details

    def input_pizza(self, crust, sauce, cheese, toppings):
        from source.pizza import Pizza

        ordering = "yes"
        while ordering == "yes":
            # Crust input
            while True:
                crust = input("Enter crust type (Thin, Thick, Gluten Free): ").strip().title()
                if crust in Pizza.crusts:
                    break
                print("Invalid crust type. Please try again.")

            # Sauce input
            while True:
                sauce = input("Enter sauce type (Marinara, Pesto, Liv Sauce): ").strip().title()
                if sauce in Pizza.sauces:
                    break
                print("Invalid sauce type. Please try again.")

            # Cheese input
            while True:
                cheese = input("Enter cheese type (Mozzarella): ").strip().title()
                if cheese in Pizza.cheeses:
                    break
                print("Invalid cheese type. Please try again.")

            # Toppings input (no duplicates)
            while True:
                toppings_input = input("Enter toppings (Pineapple, Pepperoni, Mushrooms), separated by commas: ")
                toppings_list = [t.strip().title() for t in toppings_input.split(",")]
                # Remove duplicates and filter valid toppings
                toppings = []
                seen = set()
                for t in toppings_list:
                    if t in Pizza.toppings and t not in seen:
                        toppings.append(t)
                        seen.add(t)
                if toppings:
                    break
                print("Invalid toppings. Please try again.")

            pizza = Pizza(crust, sauce, cheese, toppings)
            self.pizzas.append(pizza)
            self.cost += pizza.cost()

            while True:
                ordering = input("Would you like to add another pizza? (yes/no): ").strip().lower()
                if ordering in ["yes", "no"]:
                    break
                print("Invalid input. Please enter 'yes' or 'no'.")
            if ordering == "no":
                break

        return self.pizzas

    def order_paid(self):
        # Set order as paid once payment has been collected
        payment_type = ""
        while payment_type not in ["cash", "card", "online"]:
            payment_type = input("Enter payment type (cash, card, online): ").strip().lower()
            if payment_type not in ["cash", "card", "online"]:
                print("Invalid payment type. Please enter 'cash', 'card', or 'online'.")
        self.paid = True
        print(f"Thank you for your payment by {payment_type}!")
