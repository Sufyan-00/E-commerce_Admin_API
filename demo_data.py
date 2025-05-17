from app.database import SessionLocal, Base, engine
from app.models import Category, Product, Inventory, Sale
from datetime import date
import random

Base.metadata.create_all(bind=engine)
db = SessionLocal()

# Clear existing data
db.query(Sale).delete()
db.query(Inventory).delete()
db.query(Product).delete()
db.query(Category).delete()

# Categories
categories = [Category(name="Electronics"), Category(name="Books"), Category(name="Clothing")]
db.add_all(categories)
db.commit()

# Products
products = [
    Product(name="iPhone 14", category_id=1),
    Product(name="MacBook Air", category_id=1),
    Product(name="Harry Potter", category_id=2),
    Product(name="Levi's Jeans", category_id=3),
]
db.add_all(products)
db.commit()

# Inventory
for p in db.query(Product).all():
    db.add(Inventory(product_id=p.id, stock_level=random.randint(0, 100)))
db.commit()

# Sales
for p in db.query(Product).all():
    for _ in range(5):
        db.add(Sale(product_id=p.id, quantity=random.randint(1, 5), price_per_unit=random.uniform(10, 1000), sale_date=date(2024, 5, random.randint(1, 28))))
db.commit()
db.close()
