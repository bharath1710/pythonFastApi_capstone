
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import LoanCreate
from app.models.loan import LoanAccount
import math

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/")
def create_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    l = LoanAccount(**loan.dict(), user_id=1)
    db.add(l); db.commit()
    return l

@router.get("/{loan_id}/emi")
def calculate_emi(loan_id: int, db: Session = Depends(get_db)):
    loan = db.query(LoanAccount).get(loan_id)
    r = loan.interest_rate / (12 * 100)
    n = loan.tenure_months
    emi = loan.principal * r * ((1+r)**n) / (((1+r)**n) - 1)
    return {"emi": round(emi, 2)}
