from services.account_service import update_account_balance

def transfer_funds(from_account_id: int, to_account_id: int, amount: float) -> dict[str, str]:
    if to_account_id != from_account_id:
        if update_account_balance(from_account_id, -amount) and update_account_balance(to_account_id, amount):
            return {"message": f"Transferred {amount} from account {from_account_id} to account {to_account_id}"}
        else:
            return {"error": "Transfer failed"}
    else:
        return {"error": "Invalid account IDs"}