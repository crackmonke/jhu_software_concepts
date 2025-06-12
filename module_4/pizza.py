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
        self.cost = 0.0

    def __str__(self):
        #Prints a pizza order and its cost
        return f"Pizza with {self.crust} crust, {self.sauce} sauce, {self.cheese} cheese, and toppings: {', '.join(self.toppings)}. Cost: ${self.cost:.2f}"
        

    def cost(self):
        #determines the cost of the pizza
        self.cost = (self.crusts[self.crust] + 
                     self.sauces[self.sauce] + 
                     self.cheeses[self.cheese] + 
                     sum(self.toppings[topping] for topping in self.toppings))
        
        return self.cost