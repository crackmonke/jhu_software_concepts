import pytest
from source.order import Order
from source.pizza import Pizza

@pytest.mark.integration
def test_order_multiple_pizzas():
    order = Order()
    pizza1 = Pizza("Thin", "Marinara", "Mozzarella", ["Pepperoni"])
    pizza2 = Pizza("Thick", "Pesto", "Mozzarella", ["Mushrooms"])
    order.pizzas.append(pizza1)
    order.pizzas.append(pizza2)
    assert len(order.pizzas) == 2
    assert pizza1 in order.pizzas
    assert pizza2 in order.pizzas