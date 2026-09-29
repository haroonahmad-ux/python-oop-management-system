
# 📦 Python OOP Management System
# Product Management + Customer Management
# Demonstrates:
# Classes, Objects, Constructors, Attributes,
# Methods, Inheritance, and Child-Class Methods


print("=" * 45)
print("      PYTHON OOP MANAGEMENT SYSTEM")
print("=" * 45)
print()


# =========================================================
# 📦 PRODUCT MANAGEMENT SYSTEM
# =========================================================

print("===== PRODUCT MANAGEMENT SYSTEM =====")
print()


class Product:
    """Manage basic product information and operations."""

    def __init__(self, brand, price, stock):
        self.brand = brand
        self.price = price
        self.stock = stock

    def sell(self):
        """Sell one item and decrease stock by one."""
        if self.stock > 0:
            self.stock -= 1
            print(f"{self.brand} sold successfully.")
            print("Stock:", self.stock)
        else:
            print(f"{self.brand} is out of stock.")

    def price_update(self):
        """Increase product price by 400."""
        self.price += 400
        print(f"Updated Price: {self.price}")

    def show_details(self):
        """Display product information."""
        print("------------------------------")
        print("Product Details")
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Stock:", self.stock)
        print("------------------------------")
        print()


# Product Objects
mobile1 = Product("Oppo A38", 33000, 20)
charger2 = Product("Soul C12", 9000, 12)
earphones3 = Product("HKT Tango A-4", 8000, 5)
adapter4 = Product("USA", 1000, 65)
cable5 = Product("Reno 12 Pro", 1800, 56)


# Display Product Details
earphones3.show_details()
mobile1.show_details()


# Sell Products
charger2.sell()
cable5.sell()
adapter4.sell()

print()


# Sell the Same Product Multiple Times
print("===== REPEATED PRODUCT SALES =====")

charger2.sell()
charger2.sell()
charger2.sell()
charger2.sell()

cable5.sell()
cable5.sell()

print()


# Update Product Price
print("===== PRICE UPDATE =====")

cable5.price_update()

print()


# =========================================================
# 📱 INHERITANCE — MOBILE CLASS
# =========================================================

class Mobile(Product):
    """Child class inheriting from Product."""

    def smart_feature(self):
        print(f"{self.brand}: Mobile features available.")


# Mobile Objects
item1 = Mobile("Glass: Y60", 650, 40)
item2 = Mobile("Glass: Hot 9", 700, 40)
item3 = Mobile("Glass: F19", 200, 35)


# Display Child-Class Product Details
print("===== MOBILE PRODUCTS =====")

item1.show_details()
item2.show_details()
item3.show_details()


# Sell Child-Class Products
print("===== MOBILE SALES =====")

item3.sell()
item1.sell()

print()


# Update Child-Class Product Prices
print("===== MOBILE PRICE UPDATES =====")

item1.price_update()
item3.price_update()
item2.price_update()

print()


# Use Child-Class Method
print("===== MOBILE FEATURES =====")

item1.smart_feature()
item2.smart_feature()
item3.smart_feature()

print()


# =========================================================
# 👤 CUSTOMER MANAGEMENT SYSTEM
# =========================================================

print("=" * 45)
print("      CUSTOMER MANAGEMENT SYSTEM")
print("=" * 45)
print()


class Customer:
    """Manage customer purchase and billing information."""

    def __init__(self, name, contact, item, price, quantity):
        self.name = name
        self.contact = contact
        self.item = item
        self.price = price
        self.quantity = quantity

    def show_data(self):
        """Display customer purchase report."""
        total_amount = self.price * self.quantity

        print("------------------------------")
        print("Customer Report")
        print("------------------------------")
        print("Customer Name:", self.name)
        print("Contact:", self.contact)
        print("Item:", self.item)
        print("Item Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Amount:", total_amount)
        print("------------------------------")

        print("Customer Support")
        print("Support: Store Management")
        print("Contact: 0300-0000000")
        print("------------------------------")
        print()


# Customer Objects
customer1 = Customer(
    "Kamran",
    "0300-1111111",
    "Oppo A38",
    43000,
    1
)

customer2 = Customer(
    "Haroon",
    "0300-2222222",
    "Oppo A76",
    84000,
    1
)

customer3 = Customer(
    "Majeed",
    "0300-3333333",
    "Reno F12",
    112000,
    1
)

customer4 = Customer(
    "Ahmad",
    "0300-4444444",
    "Fast Android Cable",
    650,
    3
)

customer5 = Customer(
    "Sharfat",
    "0300-5555555",
    "Samsung Quick Charger",
    3200,
    2
)

customer6 = Customer(
    "M. Khalid",
    "None",
    "We5 30GB Bundle",
    1700,
    3
)


# Display Selected Customer Reports
customer1.show_data()
customer3.show_data()
customer6.show_data()


# =========================================================
# 🧬 INHERITANCE — CUSTOMER REPORT CLASS
# =========================================================

class CustomerReport(Customer):
    """Child class demonstrating inheritance and an additional method."""

    def customer_report(self):
        """Generate a detailed customer report."""
        total_amount = self.price * self.quantity

        print("------------------------------")
        print("Detailed Customer Report")
        print("------------------------------")
        print("Customer Name:", self.name)
        print("Contact:", self.contact)
        print("Item:", self.item)
        print("Item Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Amount:", total_amount)
        print("------------------------------")

        print("Customer Support")
        print("Support: Store Management")
        print("Contact: 0300-0000000")
        print("------------------------------")
        print()


# Customer Report Objects
report1 = CustomerReport(
    "Kashif",
    "0300-6666666",
    "Sufee Oil 5kg",
    1400,
    2
)

report2 = CustomerReport(
    "Aftab",
    "0300-7777777",
    "Men's Face Wash",
    800,
    3
)

report3 = CustomerReport(
    "Ali Aftab",
    "0300-8888888",
    "Apple Maza Candies Pack",
    350,
    8
)

report4 = CustomerReport(
    "Kashif Ali",
    "None",
    "Bonus Soap 3kg",
    850,
    3
)


# Display Customer Reports
print("===== DETAILED CUSTOMER REPORTS =====")

report1.customer_report()
report2.customer_report()
report3.customer_report()
report4.customer_report()


print("=" * 45)
print("       PROGRAM FINISHED")
print("=" * 45)
