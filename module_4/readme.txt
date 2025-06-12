# Pizza Ordering App

This is a simple Python application for creating and managing pizza orders.  
It supports multiple pizzas per order, customizable crusts, multiple sauces, cheeses, and toppings (no duplicates), and calculates the total cost.

## Features

- Interactive command-line interface for building pizza orders
- Supports multiple pizzas per order
- Customizable crust, multiple sauces, cheese, and toppings (no duplicates)
- Calculates total cost for the order
- Marks orders as paid with payment type
- Fully unit and integration tested with pytest
- Sphinx-style code documentation

## Project Structure

```
module_4/
│
├── source/
│   ├── order.py        # Order class and logic
│   ├── pizza.py        # Pizza class and logic
│   └── __init__.py
│
├── test files/
│   ├── test_order.py         # Unit tests for Order
│   ├── test_pizza.py         # Unit tests for Pizza
│   └── test_integration.py   # Integration tests
│
├── pytest.ini        # Pytest configuration for custom markers
├── requirements.txt  # Python dependencies for this project
├── README.md         # Project documentation
```

## Usage

1. **Install Python 3.10+** (recommended).
2. **Install dependencies** using the requirements file:

   ```
   pip install -r requirements.txt
   ```

3. **Run the tests:**

   ```
   pytest
   ```

   To run only order or pizza tests:

   ```
   pytest -m order
   pytest -m pizza
   ```

## Documentation

- Code is documented with Sphinx-style docstrings.
- To build HTML docs with Sphinx (if configured):

   ```
   sphinx-build -b html source docs
   ```


**README written by:**  
GitHub Copilot

