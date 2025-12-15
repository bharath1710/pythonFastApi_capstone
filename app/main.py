
from fastapi import FastAPI
from app.routers import auth, loans
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Banking Loan Payment System")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(loans.router, prefix="/loans", tags=["Loans"])

@app.get("/")
def root():
    return {"status": "Loan Payment System Running"}
