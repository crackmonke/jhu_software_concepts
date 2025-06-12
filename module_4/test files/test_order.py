import pytest
from source.order import Order
from source.pizza import Pizza

@pytest.mark.unit
def test_order_initialization():
    order = Order()
    assert order.pizzas == []
    assert order.cost == 0.0
    assert order.paid is False

@pytest.mark.unit
def test_order_add_pizza():
    order = Order()
    pizza = Pizza("Thin", "Marinara", "Mozzarella", ["Pepperoni"])
    order.pizzas.append(pizza)
    assert len(order.pizzas) == 1
    assert order.pizzas[0] == pizza