
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.database import Base

class LoanAccount(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    principal = Column(Float)
    interest_rate = Column(Float)
    tenure_months = Column(Integer)
    status = Column(String, default="ACTIVE")
