# API обменник валют

### Что делает:
Запрашивает данные с любого api-обменника,
на котором есть ручка для получения всех валют и цен на них относительно доллара, а также 
аутентификация по api-ключу через URL PARAMS.\
Я использую https://freecurrencyapi.com/

### Перед запуском
Необходимо заполнить .env-template файл и переименовать в .env (или создать .env файл по шаблону)

Переменные .env:
```commandline
FREE_CURRENCY_API_KEY - api-ключ
EXCHANGE_URL - ссылка с ценами валют относительно доллара
API_KEY_PARAM_NAME - название параметра апи ключа на сайте

Дефолтные значения:
EXCHANGE_URL=https://api.freecurrencyapi.com/v1/latest
API_KEY_PARAM_NAME=apikey
```

### Запуск:
#### Предполагая, что есть докер

```
docker compose up --build
```

#### Без докера

Зависимости:
```commandline
pip install -r requirements.txt
```

Запуск:
```bash
cd server && uvicorn --port 8080 --host 0.0.0.0 app:app
```

### Работающий сервер:
Всего одна доступная ручка (эндпойнт):
```commandline
http://127.0.0.1:8080/api/rates
```
Принимает url-параметры:
```commandline
from_ - нижнее подчеркивание обязательно. Валюта, которую меняем
to - валюта, которую получаем
value - количество меняемой валюты
```
Ответ:
```json
{
  "result": float - количество получаемой валюты
}
```
Пример запрос-ответ:
```json
Запрос:
http://127.0.0.1:8080/api/rates?from_=USD&to=RUB&value=1

Ответ:
{
  "result": 96.09
}
```

### Документация:
SwaggerUI (интерактивная документация доступна по url 127.0.0.1:8080/docs)

