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
from src.processing.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED", "amount": 1000},
    {"id": 2, "state": "CANCELED", "amount": 500},
]

result = filter_by_state(operations)
# [{"id": 1, "state": "EXECUTED", "amount": 1000}]
```
