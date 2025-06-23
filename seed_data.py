from sqlalchemy.orm import sessionmaker
from sqldp import engine, MenuItem, Table

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add the demo table
table = Table(id=1, qr_code_url='/static/qrcodes/1.png')
session.merge(table)  # Use merge to avoid duplication

# Add menu items
menu_items = [
    MenuItem(id=1, name='Margherita Pizza', price=9.99, category='Main Course', is_available=True),
    MenuItem(id=2, name='Orange Juice', price=2.50, category='Drinks', is_available=True),
    MenuItem(id=3, name='French Fries', price=3.00, category='Sides', is_available=True),
    MenuItem(id=4, name='Chicken Shawarma Wrap', price=7.50, category='Main Course', is_available=True),
    MenuItem(id=5, name='Cola', price=1.50, category='Drinks', is_available=True),
    MenuItem(id=6, name='Green Salad', price=3.75, category='Sides', is_available=True),
    MenuItem(id=7, name='Mineral Water', price=1.00, category='Drinks', is_available=True),
    MenuItem(id=8, name='Beef Burger', price=8.99, category='Main Course', is_available=True),
    MenuItem(id=9, name='Cheesecake', price=4.50, category='Dessert', is_available=True),
    MenuItem(id=10, name='Turkish Coffee', price=2.00, category='Drinks', is_available=True),
    MenuItem(id=11, name='Grilled Chicken', price=10.50, category='Main Course', is_available=True),
    MenuItem(id=12, name='Chocolate Cake', price=4.75, category='Dessert', is_available=True),
    MenuItem(id=13, name='Iced Tea', price=2.25, category='Drinks', is_available=True),
    MenuItem(id=14, name='Spaghetti Bolognese', price=9.50, category='Main Course', is_available=True),
    MenuItem(id=15, name='Garlic Bread', price=2.25, category='Sides', is_available=True),
    MenuItem(id=16, name='Tiramisu', price=5.00, category='Dessert', is_available=True),
    MenuItem(id=17, name='Lemonade', price=2.75, category='Drinks', is_available=True),
    MenuItem(id=18, name='Club Sandwich', price=7.25, category='Main Course', is_available=True),
    MenuItem(id=19, name='Mashed Potatoes', price=3.50, category='Sides', is_available=True),
    MenuItem(id=20, name='Apple Pie', price=4.00, category='Dessert', is_available=True),
]

# Insert data
session.add_all(menu_items)
session.commit()

print("✅ Seed data inserted successfully.")
