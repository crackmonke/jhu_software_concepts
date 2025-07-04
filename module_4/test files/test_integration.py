import pytest
from source.order import Order
from source.pizza import Pizza

@pytest.mark.order
@pytest.mark.pizza
def test_order_multiple_pizzas_cost_additive():
    """
    Integration test to ensure multiple pizzas in an order result in an additive cost.

    Asserts
    -------
    - The order contains two pizzas.
    - The total cost is the sum of the individual pizza costs.
    """
    order = Order()
    pizza1 = Pizza("Thin", ["Marinara"], "Mozzarella", ["Pepperoni"])
    pizza2 = Pizza("Thick", ["Pesto"], "Mozzarella", ["Mushrooms"])
    order.pizzas.append(pizza1)
    order.pizzas.append(pizza2)
    order.cost = pizza1.cost() + pizza2.cost()
    assert len(order.pizzas) == 2
    assert order.cost == pizza1.cost() + pizza2.cost()