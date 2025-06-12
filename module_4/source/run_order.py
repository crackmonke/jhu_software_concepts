from source.order import Order

def main():
    order = Order()
    print("Welcome to the Pizza Order System!")
    order.input_pizza(None, None, None, None)
    print("\nYour order summary:")
    print(order)
    order.order_paid()

if __name__ == "__main__":
    main()