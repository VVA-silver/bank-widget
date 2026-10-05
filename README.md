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
 

В проект добавлены генераторы для работы с банковскими транзакциями и номерами карт.

filter_by_currency

Функция фильтрует транзакции по коду валюты.

filter_by_currency(transactions, currency)

Параметры:
• transactions — список словарей с информацией о транзакциях;
• currency — код валюты, например USD или EUR.

Функция возвращает итератор, содержащий только транзакции с указанной валютой.
Пример:
transactions = [
    {
        "id": 1,
        "operationAmount": {
            "currency": {
                "code": "USD"
            }
        }
    }
]

result = filter_by_currency(transactions, "USD")
transaction_descriptions
Генератор последовательно возвращает описания транзакций.
transaction_descriptions(transactions)
Параметр:
• transactions — список словарей с информацией о транзакциях.
Пример:
descriptions = transaction_descriptions(transactions)

for description in descriptions:
    print(description)
card_number_generator
Генератор создает номера банковских карт в формате:
XXXX XXXX XXXX XXXX
card_number_generator(start, stop)
Параметры:
• start — начальное значение диапазона;
• stop — конечное значение диапазона.
Пример:
for card_number in card_number_generator(1, 5):
    print(card_number)
Результат:
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005
Тестирование
Для тестирования генераторов используется pytest.
В тестах применяются:
• фикстуры pytest.fixture;
• параметризация pytest.mark.parametrize;
• проверки пустых списков;
• проверки отсутствующих данных;
• проверки формата номеров карт;
• проверки поведения генераторов и StopIteration.
Запуск тестов:
pytest
Проверка кода с помощью Flake8:
flake8 src tests

Покрытие тестами
Для проверки покрытия используется pytest-cov.
Запуск тестов и создание HTML-отчёта:
pytest --cov=src --cov-report=html --cov-fail-under=80