from database import db, Base
from models.customer import Customer
from models.order import Orders
from models.product import Products
from datetime import date, timedelta

def add_sample_data():
    # Add sample customers
    customer1 = Customer(customer_name="John Doe", email="john.doe@example.com", phone="1234567890")
    customer2 = Customer(customer_name="Jane Smith", email="jane.smith@example.com", phone="0987654321")
    
    db.session.add(customer1)
    db.session.add(customer2)
    db.session.commit()

    # Add sample products
    product1 = Products(product_name="Product 1", price=10.0)
    product2 = Products(product_name="Product 2", price=20.0)
    
    db.session.add(product1)
    db.session.add(product2)
    db.session.commit()

    # Add sample orders
    order1 = Orders(order_date=date.today(), customer_id=customer1.id, expected_delivery_date=date.today() + timedelta(days=3))
    order1.products.append(product1)
    order1.products.append(product2)
    
    db.session.add(order1)
    db.session.commit()
