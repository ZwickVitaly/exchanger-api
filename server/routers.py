import asyncio
from json import JSONDecodeError
from fastapi import APIRouter
from fastapi.params import Query
from fastapi.responses import JSONResponse
from decimal import Decimal
from schemas import ExchangeInSchema, ExchangeOutSchema
from api_services import get_currencies_data

currency_exchange_router = APIRouter()


@currency_exchange_router.get("/rates", responses={200: {"model": ExchangeOutSchema}})
async def get_rates(params: ExchangeInSchema = Query()):
    """
    Запрос обменного курса.
    \nfrom: Валюта, которую меняем
    \nto: Валюта, которую получаем
    \nсписок доступных валют в описании модели ExchangeInfoInSchema
    """
    try:
        currencies_data = await get_currencies_data()
        if not currencies_data:
            raise ValueError
    except (asyncio.TimeoutError, JSONDecodeError, ValueError):
        return JSONResponse(content="Сервер с данными о валютах не отвечает", status_code=404)
    price_from = currencies_data.get(params.from_)
    price_to = currencies_data.get(params.to)
    value = params.value
    if params.from_ != "USD":
        value = Decimal(value / price_from)
    result = round(Decimal(value * price_to), 2)
    return JSONResponse(content=ExchangeOutSchema(result=result).model_dump(), status_code=200)
