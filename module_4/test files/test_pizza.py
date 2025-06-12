import pytest
from source.pizza import Pizza

@pytest.mark.pizza
def test_pizza_init():
    """
    Test that a Pizza object is initialized correctly.

    Asserts
    -------
    - The crust, sauce, cheese, and toppings are set as expected.
    """
    pizza = Pizza("Thin", ["Marinara"], "Mozzarella", ["Pepperoni", "Mushrooms"])
    assert pizza.crust == "Thin"
    assert pizza.sauce == ["Marinara"]
    assert pizza.cheese == "Mozzarella"
    assert pizza.toppings == ["Pepperoni", "Mushrooms"]

@pytest.mark.pizza
def test_pizza_cost_nonzero():
    """
    Test that the cost method returns a non-zero value for a valid pizza.

    Asserts
    -------
    - The cost is greater than zero.
    """
    pizza = Pizza("Thick", ["Pesto"], "Mozzarella", ["Pineapple"])
    assert pizza.cost() > 0

@pytest.mark.pizza
def test_pizza_str():
    """
    Test that the string representation of a pizza contains all details.

    Asserts
    -------
    - The string contains the crust, a topping, and the word "Cost".
    """
    pizza = Pizza("Thin", ["Marinara"], "Mozzarella", ["Pepperoni"])
    result = str(pizza)
    assert "Thin" in result
    assert "Pepperoni" in result
    assert "Cost" in result

@pytest.mark.pizza
def test_pizza_cost_correct():
    """
    Test that the cost method returns the correct value for a known pizza.

    Asserts
    -------
    - The cost matches the expected calculation.
    """
    pizza = Pizza("Thin", ["Marinara"], "Mozzarella", ["Pepperoni"])
    expected = 5 + 2 + 0 + 2  # Thin + Marinara + Mozzarella + Pepperoni
    assert pizza.cost() == expected