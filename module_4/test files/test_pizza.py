import pytest
from source.pizza import Pizza

@pytest.mark.unit
def test_pizza_initialization():
    pizza = Pizza("Thin", "Marinara", "Mozzarella", ["Pepperoni", "Mushrooms"])
    assert pizza.crust == "Thin"
    assert pizza.sauce == "Marinara"
    assert pizza.cheese == "Mozzarella"
    assert pizza.toppings == ["Pepperoni", "Mushrooms"]

@pytest.mark.unit
def test_pizza_cost_returns_float():
    pizza = Pizza("Thick", "Pesto", "Mozzarella", ["Pineapple"])
    assert isinstance(pizza.cost(), float)