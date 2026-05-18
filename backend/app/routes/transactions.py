from fastapi import APIRouter, HTTPException, Query
from services.account_service import get_account
from services.transfer_service import transfer_funds
from typing import Annotated
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/{account_id}")
async def read_transactions(account_id: int):
    account = get_account(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account.transactions

class TransferParams(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float

# TODO: fix query params
@router.post("/transfer")
async def post_transfer(transfer_query: Annotated[TransferParams, Query()]):
    transfer = transfer_funds(transfer_query.from_account_id, transfer_query.to_account_id, transfer_query.amount)
    if "error" in transfer:
        raise HTTPException(status_code=400, detail="Error transferring funds")
    return transfer