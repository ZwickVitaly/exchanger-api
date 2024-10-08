from fastapi import FastAPI

from routers import currency_exchange_router


app = FastAPI()

app.include_router(currency_exchange_router, prefix="/api")