from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from app.database import get_db
from app.models import Sale, Product
from app.schemas import SaleCreate, SaleResponse

router = APIRouter()

@router.post("/", response_model=SaleResponse)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    if not db.query(Product).filter(Product.id == sale.product_id).first():
        raise HTTPException(status_code=400, detail="Product not found")
    new_sale = Sale(**sale.dict())
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale

@router.get("/", response_model=list[SaleResponse])
def list_sales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Sale).offset(skip).limit(limit).all()

@router.get("/revenue")
def revenue(start_date: date, end_date: date, db: Session = Depends(get_db)):
    revenue = db.query(func.sum(Sale.quantity * Sale.price_per_unit)).filter(Sale.sale_date.between(start_date, end_date)).scalar()
    return {"revenue": revenue or 0}

@router.get("/compare")
def compare(start1: date, end1: date, start2: date, end2: date, db: Session = Depends(get_db)):
    rev1 = db.query(func.sum(Sale.quantity * Sale.price_per_unit)).filter(Sale.sale_date.between(start1, end1)).scalar() or 0
    rev2 = db.query(func.sum(Sale.quantity * Sale.price_per_unit)).filter(Sale.sale_date.between(start2, end2)).scalar() or 0
    return {"period1": rev1, "period2": rev2}
