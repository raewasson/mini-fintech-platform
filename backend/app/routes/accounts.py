from fastapi import APIRouter, HTTPException
from services.account_service import get_account

router = APIRouter(
    prefix="/account",
    tags=["account"]
)

@router.get("/{account_id}")
async def read_account(account_id: int):
    account = get_account(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account
