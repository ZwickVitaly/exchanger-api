from pydantic import BaseModel, Field, field_validator

from settings import AVAILABLE_CURRENCIES


class ExchangeInSchema(BaseModel):
    from_: str = Field(
        description=f"Валюта, которую меняем. Доступные валюты: {AVAILABLE_CURRENCIES}",
        examples=AVAILABLE_CURRENCIES,
    )
    to: str = Field(
        description=f"Валюта, которую получаем. Доступные валюты: {AVAILABLE_CURRENCIES}",
        examples=AVAILABLE_CURRENCIES,
    )

    value: float = Field(
        description="Количество обмениваемой валюты",
        examples=[1324.35, 241.82313],
        ge=0,
    )

    @field_validator("from_", "to", mode="before")
    @classmethod
    def validate_sorting(cls, value):
        if isinstance(value, str):
            value = value.upper()
        else:
            raise ValueError("Ожидается строка")
        if value not in AVAILABLE_CURRENCIES:
            raise ValueError(
                f"Валюта не найдена. Список доступных валют:\n{'\n'.join(AVAILABLE_CURRENCIES)}"
            )
        return value

class ExchangeOutSchema(BaseModel):
    result: float = Field(
        description=f"Результат",
    )
