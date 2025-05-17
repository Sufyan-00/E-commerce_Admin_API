from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Product, Category
from app.schemas import ProductCreate, ProductResponse

router = APIRouter()

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    if not db.query(Category).filter(Category.id == product.category_id).first():
        raise HTTPException(status_code=400, detail="Category not found")
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=list[ProductResponse])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Product).offset(skip).limit(limit).all()
