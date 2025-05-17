from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Inventory
from app.schemas import InventoryResponse, InventoryUpdate

router = APIRouter()

@router.get("/", response_model=list[InventoryResponse])
def list_inventory(db: Session = Depends(get_db)):
    return db.query(Inventory).all()

@router.get("/low-stock", response_model=list[InventoryResponse])
def low_stock(threshold: int = 10, db: Session = Depends(get_db)):
    return db.query(Inventory).filter(Inventory.stock_level < threshold).all()

@router.put("/{product_id}", response_model=InventoryResponse)
def update_inventory(product_id: int, update: InventoryUpdate, db: Session = Depends(get_db)):
    inventory = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    inventory.stock_level = update.stock_level
    db.commit()
    db.refresh(inventory)
    return inventory
