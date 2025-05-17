from pydantic import BaseModel
from datetime import date

class CategoryBase(BaseModel):
    name: str

class CategoryResponse(CategoryBase):
    id: int
    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    category_id: int

class ProductResponse(ProductCreate):
    id: int
    class Config:
        orm_mode = True

class InventoryResponse(BaseModel):
    id: int
    product_id: int
    stock_level: int
    class Config:
        orm_mode = True

class InventoryUpdate(BaseModel):
    stock_level: int

class SaleCreate(BaseModel):
    product_id: int
    quantity: int
    price_per_unit: float
    sale_date: date

class SaleResponse(SaleCreate):
    id: int
    class Config:
        orm_mode = True
