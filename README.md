# Bank Widget

Виджет банковских операций клиента.

## Структура проекта

```
bank-widget/
├── src/
│   └── processing/
│       ├── __init__.py
│       └── processing.py
├── .gitignore
└── README.md
```

## Модуль processing

### filter_by_state

Фильтрует список операций по статусу.

```python
 
Модуль 
generators
Модуль src/generators.py содержит генераторы для работы с транзакциями и номерами банковских карт.
filter_by_currency
Фильтрует транзакции по коду валюты.
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(transaction)
transaction_descriptions

Последовательно возвращает описания транзакций.

from src.generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)

for description in descriptions:
    print(description)
    
Результат:

Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации
card_number_generator
Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.

from src.generators import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
    
Результат:

0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005


Тестирование

Запуск тестов:

pytest

Проверка покрытия:
pytest --cov=src --cov-report=term-missing
Требуемое покрытие кода — не менее 80%.