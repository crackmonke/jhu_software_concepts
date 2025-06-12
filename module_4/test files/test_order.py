import pytest
from source.order import Order
from source.pizza import Pizza

@pytest.mark.order
def test_order_init():
    """
    Test that a new Order is initialized correctly.

    Asserts
    -------
    - The pizzas list is empty.
    - The cost is zero.
    - The order is not marked as paid.
    """
    order = Order()
    assert order.pizzas == []  # Should start with no pizzas
    assert order.cost == 0.0   # Cost should be zero
    assert order.paid is False # Should not be paid yet

@pytest.mark.order
def test_order_str():
    """
    Test that the order string contains the correct summary and pizza details.

    Asserts
    -------
    - The string starts with "Customer Requested:"
    - The string contains "Total Cost"
    - The string contains the pizza topping "Pepperoni"
    """
    order = Order()
    pizza = Pizza("Thin", ["Marinara"], "Mozzarella", ["Pepperoni"])
    order.pizzas.append(pizza)
    order.cost += pizza.cost()
    result = str(order)
    assert result.startswith("Customer Requested:")  # Should start with this header
    assert "Total Cost" in result                   # Should include total cost
    assert "Pepperoni" in result                    # Should include pizza details

@pytest.mark.order
def test_order_input_pizza_updates_cost(monkeypatch):
    """
    Test that input_pizza updates the order cost.

    Uses monkeypatch to simulate user input for one pizza, then 'no' to stop.

    Asserts
    -------
    - The order cost is greater than zero after adding a pizza.
    """
    order = Order()
    # Simulate user input sequence: crust, sauce, cheese, toppings, then 'no' to stop
    inputs = iter([
        "Thin",        # crust
        "Marinara",    # sauce
        "Mozzarella",  # cheese
        "Pepperoni",   # toppings
        "no"           # finish ordering
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    order.input_pizza(None, None, None, None)
    assert order.cost > 0  # Cost should be updated after adding a pizza

@pytest.mark.order
def test_order_paid(monkeypatch):
    """
    Test that order_paid sets the paid flag to True after valid payment type.

    Uses monkeypatch to simulate payment type input.

    Asserts
    -------
    - The order is marked as paid after payment.
    """
    order = Order()
    # Simulate payment type input
    inputs = iter(["card"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    order.order_paid()
    assert order.paid is True  # Should be marked as paid after payment