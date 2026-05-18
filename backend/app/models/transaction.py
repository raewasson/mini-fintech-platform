from pydantic import BaseModel

class Transaction(BaseModel):
    transaction_id: str
    amount: float
    timestamp: str