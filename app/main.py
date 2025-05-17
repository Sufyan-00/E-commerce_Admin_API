from fastapi import FastAPI
from app.database import Base, engine
from app.routers import products, inventory, sales

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce Admin API")

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])
app.include_router(sales.router, prefix="/sales", tags=["Sales"])
