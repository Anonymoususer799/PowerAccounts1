from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/predict-expenses")
def predict_expenses(days: int = 30):
    # Mock prediction logic
    future_date = datetime.now() + timedelta(days=days)
    return {
        "prediction": f"Estimated expenses for the next {days} days are $5000",
        "until": future_date.strftime("%Y-%m-%d")
    }