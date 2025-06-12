class pizza

#Pizza objects and assoicated cost
def __init__(self, crust, sauce, cheese, toppings):
    # Initializes a pizza
    pizza = None  # Placeholder for pizza object
    #set pizza variables
    self.crust = crust
    self.sauce = sauce
    self.cheese = cheese
    self.toppings = toppings
    self.cost = 0  # Initialize cost to zero

    # Calculate cost based on ingredients
    if crust == "thin":
        self.cost += 5
    elif crust == "thick":
        self.cost += 6
    elif crust == "Gluten Free":
        self.cost += 8

    if sauce == "Marinara":
        self.cost += 2
    elif sauce == "Pesto":
        self.cost += 3
    elif sauce == "LivSauce":
        self.cost += 5
    #set cost to create

def __str__(self):
    #Prints a pizza order
    #Prints the cost of the pizza

def cost(self):
    #determines the cost of the pizza