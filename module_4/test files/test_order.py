import pytest
from source.order import Order
from source.pizza import Pizza

@pytest.mark.order
def test_order_init():
    order = Order()
    assert order.pizzas == []
    assert order.cost == 0.0
    assert order.paid is False

@pytest.mark.order
def test_order_str():
    order = Order()
    pizza = Pizza("Thin", ["Marinara"], "Mozzarella", ["Pepperoni"])
    order.pizzas.append(pizza)
    order.cost += pizza.cost()
    result = str(order)
    assert result.startswith("Customer Requested:")
    assert "Total Cost" in result
    assert "Pepperoni" in result

@pytest.mark.order
def test_order_input_pizza_updates_cost(monkeypatch):
    order = Order()
    # Simulate user input for one pizza, then 'no' to stop
    inputs = iter([
        "Thin", "Marinara", "Mozzarella", "Pepperoni", "no"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    order.input_pizza(None, None, None, None)
    assert order.cost > 0

@pytest.mark.order
def test_order_paid(monkeypatch):
    order = Order()
    # Simulate payment type input
    inputs = iter(["card"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    order.order_paid()
    assert order.paid is True