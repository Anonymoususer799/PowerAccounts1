from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Transaction(BaseModel):
    amount: float
    category: str
    timestamp: str

@router.get("/")
def get_transactions():
    return {"transactions": []}

@router.post("/")
def add_transaction(transaction: Transaction):
    return {"message": "Transaction added", "transaction": transaction}