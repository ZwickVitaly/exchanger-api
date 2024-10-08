from aiohttp import ClientSession

from settings import API_KEY_PARAM_NAME, FREE_CURRENCY_API_KEY, EXCHANGE_URL


async def get_currencies_data():
    async with ClientSession() as session:
        async with session.get(
            EXCHANGE_URL, params={API_KEY_PARAM_NAME: FREE_CURRENCY_API_KEY}
        ) as response:
            if response.ok:
                return (await response.json()).get("data")
