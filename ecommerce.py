import logging
logging.basicConfig(
    filename="orders.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Order:

    tax_percentage = 5   

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = {}  
        self.order_status = "Not Placed"
        self.total_amount = 0

    def place_order(self, item_name, price):
        self.items[item_name] = price
        self.order_status = "Placed"
        logging.info("%s added to order",item_name)

    def cancel_order(self):
        if self.order_status == "Placed":
            self.order_status = "Cancelled"
            logging.info("Order cancelled successfully")
        else:
            logging.info("Order cannot be cancelled")

    def calculate_total_price(self):
        subtotal = sum(self.items.values())
        tax = (subtotal * Order.tax_percentage) / 100
        self.total_amount = subtotal + tax

        logging.info("Subtotal is %d", subtotal)
        logging.info("Tax is %d", tax)
        logging.info("Total Amount is %d", self.total_amount)

    @classmethod
    def update_tax_percentage(cls, new_tax):
        cls.tax_percentage = new_tax
        print("Tax percentage updated to:", cls.tax_percentage)

o1 = Order("Harshini")

o1.place_order("Laptop", 50000)
o1.place_order("Mouse", 1000)

o1.calculate_total_price()

Order.update_tax_percentage(10)

