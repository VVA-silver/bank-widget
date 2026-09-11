# Bank Widget

Виджет банковских операций клиента. Предоставляет инструменты для маскировки номеров карт и счетов, фильтрации и сортировки списка банковских транзакций.

## Структура проекта

```
bank-widget/
├── src/
│   ├── __init__.py
│   ├── masks.py          # маскировка номеров карт и счетов
│   ├── widget.py         # отображение карт/счетов и форматирование дат
│   └── processing/
│       ├── __init__.py
│       └── processing.py # фильтрация и сортировка операций
├── .gitignore
└── README.md
```

## Установка

1. Клонируйте репозиторий:

```bash
git clone <url-репозитория>
cd bank-widget
```

2. Убедитесь, что используется Python 3.10+:

```bash
python --version
```

3. Установите зависимости для разработки:

```bash
pip install pytest pytest-cov flake8 mypy isort
```

---

## Тестирование

Тесты написаны с использованием `pytest` и покрывают все модули проекта.

### Структура тестов

```
tests/
├── conftest.py          # фикстуры для всех тестов
├── test_masks.py        # тесты модуля masks
├── test_widget.py       # тесты модуля widget
└── test_processing.py   # тесты модуля processing
```

### Запуск тестов

```bash
pytest tests/ -v
```

### Запуск тестов с отчётом покрытия

```bash
pytest tests/ --cov=src --cov-report=term-missing --cov-report=html:htmlcov
```

HTML-отчёт покрытия сохраняется в папку `htmlcov/`.

### Текущее покрытие

| Модуль | Покрытие |
|---|---|
| `src/masks.py` | 100% |
| `src/widget.py` | 100% |
| `src/processing/processing.py` | 100% |
| **Итого** | **100%** |

### Линтеры

```bash
flake8 src/ tests/
mypy src/
isort src/ tests/ --check-only
```

---

## Модуль `masks`

### `get_mask_card_number`

Маскирует номер банковской карты.

**Параметры:**
- `card_number` — номер карты (16 цифр, `int` или `str`)

**Пример:**

```python
from src.masks import get_mask_card_number

get_mask_card_number("7000792289606361")
# '7000 79** **** 6361'
```

---

### `get_mask_account`

Маскирует номер банковского счёта.

**Параметры:**
- `account_number` — номер счёта (`int` или `str`)

**Пример:**

```python
from src.masks import get_mask_account

get_mask_account("73654108430135874305")
# '**4305'
```

---

## Модуль `widget`

### `mask_account_card`

Маскирует номер карты или счёта в составе строки с названием.

**Параметры:**
- `card_info` — строка вида `'Visa Platinum 1234567890123456'` или `'Счет 12345678901234567890'`

**Пример:**

```python
from src.widget import mask_account_card

mask_account_card("Visa Platinum 7000792289606361")
# 'Visa Platinum 7000 79** **** 6361'

mask_account_card("Счет 73654108430135874305")
# 'Счет **4305'
```

---

### `get_date`

Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

**Параметры:**
- `date_string` — дата в формате `'2024-03-11T02:26:18.671407'`

**Пример:**

```python
from src.widget import get_date

get_date("2024-03-11T02:26:18.671407")
# '11.03.2024'
```

---

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

filter_by_state(operations)
# [{'id': 41428829, ...}, {'id': 939719570, ...}]

filter_by_state(operations, state='CANCELED')
# [{'id': 594226727, ...}, {'id': 615064591, ...}]
```

---

### `sort_by_date`

Сортирует список операций по дате (`date`).

**Параметры:**
- `data` — список словарей с банковскими операциями
- `reverse` — `True` — новые первыми (по умолчанию), `False` — старые первыми

**Пример:**

```python
from src.processing.processing import sort_by_date

sort_by_date(operations)
# [{'id': 41428829, 'date': '2019-07-03...'}, ...]

sort_by_date(operations, reverse=False)
# [{'id': 939719570, 'date': '2018-06-30...'}, ...]
```
