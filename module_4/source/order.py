class Order:

    def __init__(self):
        #Initalizes a customer order
        #initalizes order cost
        self.pizzas = []
        self.cost = 0.0
        self.paid = False
        self.order_id = self.generate_order_id()

    def __str__(self):
        #Prints a customers order
        order_details = f"Order ID: {self.order_id}, Customer: {self.customer_name}, Total Cost: ${self.cost:.2f}\n"
        order_details += "Pizzas:\n"

        #Iterates through the pizzas in the order and adds them to the order details
        for pizza in self.pizzas:
            order_details += str(pizza) + "\n"  

        return order_details
    

    def input_pizza(self, crust, sauce, cheese, toppings):
        #Inputs the customers order for a given pizza
        #Initalize the pizza object and attach to the order
        #Update the cost
        from source.pizza import Pizza

        ordering = "yes"

        while ordering == "yes":
            crust = input("Enter crust type (Thin, Thick, Gluten Free): ")
            if crust not in Pizza.crusts:
                print("Invalid crust type. Please try again.")
                continue
            sauce = input("Enter sauce type (Marinara, Pesto, Liv Sauce): ")
            if sauce not in Pizza.sauces:
                print("Invalid sauce type. Please try again.")
                continue
            cheese = input("Enter cheese type (Mozzarella): ")
            if cheese not in Pizza.cheeses:
                print("Invalid cheese type. Please try again.")
                continue
            toppings = input("Enter toppings (Pineapple, Pepperoni, Mushrooms), separated by commas: ").split(", ")
            toppings = [topping.strip() for topping in toppings if topping.strip() in Pizza.toppings]
            if not toppings:
                print("Invalid toppings. Please try again.")
                continue

            pizza = Pizza(crust, sauce, cheese, toppings)
            self.pizzas.append(pizza)
            self.cost += pizza.cost()

            ordering = input("Would you like to add another pizza? (yes/no): ").strip().lower()
            if ordering not in ["yes", "no"]:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue

        return self.pizzas
    

    def order_paid(self):
        #Set order as paid once payment has been collected
        paying = input("Have you paid for the order? (yes/no): ").strip().lower()
        if paying == "yes":
            self.paid = True
            print("Thank you for your payment!")
        else:
            print("Please complete the payment to finalize your order.")
        