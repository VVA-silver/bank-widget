# Bank Widget

Виджет банковских операций клиента. Предоставляет инструменты для фильтрации и сортировки списка банковских транзакций.

## Структура проекта

```
bank-widget/
├── src/
│   ├── __init__.py
│   └── processing/
│       ├── __init__.py
│       └── processing.py
├── .gitignore
└── README.md
```

## Установка

1. Клонируйте репозиторий:

```bash
git clone <url-репозитория>
cd bank-widget
```

2. Убедитесь, что используется Python 3.8+:

```bash
python --version
```

Сторонних зависимостей нет — проект использует только стандартную библиотеку Python.

## Модуль `processing`

### `filter_by_state`

Фильтрует список операций по значению ключа `state`.

**Параметры:**
- `data` — список словарей с банковскими операциями
- `state` — статус для фильтрации (по умолчанию `'EXECUTED'`)

**Пример:**

```python
from src.processing.processing import filter_by_state

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]

# Фильтрация по умолчанию — только EXECUTED
filter_by_state(operations)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Фильтрация по статусу CANCELED
filter_by_state(operations, state='CANCELED')
# [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

---

### `sort_by_date`

Сортирует список операций по дате (`date`).

**Параметры:**
- `data` — список словарей с банковскими операциями
- `reverse` — порядок сортировки: `True` — убывание (новые первыми), `False` — возрастание (старые первыми); по умолчанию `True`

**Пример:**

```python
from src.processing.processing import sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]

# Сортировка по убыванию (новые первыми) — по умолчанию
sort_by_date(operations)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Сортировка по возрастанию (старые первыми)
sort_by_date(operations, reverse=False)
# [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```
