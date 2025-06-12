import pytest
from source.pizza import Pizza

@pytest.mark.pizza
def test_pizza_init():
    pizza = Pizza("Thin", "Marinara", "Mozzarella", ["Pepperoni", "Mushrooms"])
    assert pizza.crust == "Thin"
    assert pizza.sauce == "Marinara"
    assert pizza.cheese == "Mozzarella"
    assert pizza.toppings == ["Pepperoni", "Mushrooms"]

@pytest.mark.pizza
def test_pizza_cost_nonzero():
    pizza = Pizza("Thick", "Pesto", "Mozzarella", ["Pineapple"])
    assert pizza.cost() > 0

@pytest.mark.pizza
def test_pizza_str():
    pizza = Pizza("Thin", "Marinara", "Mozzarella", ["Pepperoni"])
    result = str(pizza)
    assert "Thin" in result
    assert "Pepperoni" in result
    assert "Cost" in result

@pytest.mark.pizza
def test_pizza_cost_correct():
    pizza = Pizza("Thin", "Marinara", "Mozzarella", ["Pepperoni"])
    expected = 5 + 2 + 0 + 2  # Thin + Marinara + Mozzarella + Pepperoni
    assert pizza.cost() == expected