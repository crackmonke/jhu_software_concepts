class Order:

    def __init__(self):
        # Initializes a customer order
        self.pizzas = []
        self.cost = 0.0
        self.paid = False
        self.customer_name = "Customer"  # Placeholder, or set via input

    def __str__(self):
        # Prints a customer's order
        order_details = f"Customer: {self.customer_name}, Total Cost: ${self.cost:.2f}\n"
        order_details += "Pizzas:\n"
        for pizza in self.pizzas:
            order_details += str(pizza) + "\n"
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

            # Toppings input
            while True:
                toppings_input = input("Enter toppings (Pineapple, Pepperoni, Mushrooms), separated by commas: ")
                toppings = [t.strip().title() for t in toppings_input.split(",") if t.strip().title() in Pizza.toppings]
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
        paying = input("Have you paid for the order? (yes/no): ").strip().lower()
        if paying == "yes":
            self.paid = True
            print("Thank you for your payment!")
        else:
            print("Please complete the payment to finalize your order.")
