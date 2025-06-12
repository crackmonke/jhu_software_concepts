class pizza:
    
    crusts = {"Thin": 5, "Thick": 6, "Gluten Free": 8}
    sauces = {"Marinara": 2, "Pesto": 3, "Liv Sauce": 5}
    toppings = {"Pineapple": 1, "Pepperoni": 2, "Mushrooms": 3}
    cheeses = {"Mozzarella": 0}

    #Pizza objects and assoicated cost
    def __init__(self, crust, sauce, cheese, toppings):
        # Initalizes a pizza and sets its variables
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

        # Set cost to create
        self.cost = self.crusts[crust] + self.sauces[sauce] + self.cheeses[cheese] + sum(self.toppings[topping] for topping in toppings)


    def __str__(self):
        #Prints a pizza order
        #Prints the cost of the pizza

    def cost(self):
        #determines the cost of the pizza