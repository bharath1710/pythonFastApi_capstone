
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoanCreate(BaseModel):
    principal: float
    interest_rate: float
    tenure_months: int
