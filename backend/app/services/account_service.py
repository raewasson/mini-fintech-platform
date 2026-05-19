from models.account import Account
from models.transaction import Transaction
from datetime import datetime as Time

transaction_id_counter = 4

accounts_db = {
    12345: Account(account_id=12345,account_owner="Luke Skywalker", balance=1000.0, transactions=[
            Transaction(transaction_id="1", amount=200.0, timestamp="2026-05-04T10:00:00Z"),
            Transaction(transaction_id="3", amount=-50.0, timestamp="2026-05-05T12:00:00Z")
        ]),
    67890: Account(account_id=67890, account_owner="Darth Vader", balance=500.0, transactions=[
            Transaction(transaction_id="2", amount=300.0, timestamp="2026-05-04T11:00:00Z"),
            Transaction(transaction_id="4", amount=-100.0, timestamp="2026-05-06T12:00:00Z")
        ])
}

def get_account(account_id: int) -> Account | None:
    return accounts_db.get(account_id)

def update_account_balance(account_id: int, amount: float) -> bool:
    account = get_account(account_id)
    if account:
        account.balance += amount
        global transaction_id_counter
        account.transactions.append(Transaction(transaction_id=str(transaction_id_counter), amount=amount, timestamp=Time.now().isoformat()))
        transaction_id_counter += 1
        return True
    return False