from fastapi import FastAPI
from routes import auth, transactions, reports

app = FastAPI()

# Include routes
app.include_router(auth.router, prefix="/auth")
app.include_router(transactions.router, prefix="/transactions")
app.include_router(reports.router, prefix="/reports")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Accounting System API"}