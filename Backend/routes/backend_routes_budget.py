from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Budget(BaseModel):
    category: str
    limit: float

budgets = []

@router.get("/")
def get_budgets():
    return {"budgets": budgets}

@router.post("/")
def add_budget(budget: Budget):
    for b in budgets:
        if b.category == budget.category:
            raise HTTPException(status_code=400, detail="Category already exists")
    budgets.append(budget)
    return {"message": "Budget added", "budget": budget}