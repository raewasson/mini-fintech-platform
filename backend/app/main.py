from fastapi import FastAPI
from routes import accounts, transactions

app = FastAPI()

app.include_router(accounts.router)
app.include_router(transactions.router)

@app.get("/")
async def root():
    return {"message": "I'm a bank. No really, I'm a bank! Plz believe me!!! Don't go!!!!!"}