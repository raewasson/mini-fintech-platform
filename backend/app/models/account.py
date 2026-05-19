from pydantic import BaseModel
from models.transaction import Transaction
from typing import List

class Account(BaseModel):
    account_id: int
    account_owner: str
    balance: float
    transactions: List[Transaction] = []