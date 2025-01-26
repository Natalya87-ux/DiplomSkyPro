# DiplomSkyPro
Diplom
## Задача
Автоматизировать UI- и API-тесты из моей финальной работы по ручному тестированию.
## Финальный проект по ручному тестированию: Авиасейлс https://www.aviasales.ru/
## Описание тестируемой системы:
Авиасейлс ру - это популярный российский сайт, созданный для удобного поиска дешёвых авиабилетов в любые направления мира.  В качестве метапоиска Aviasales не продает авиабилеты, но перенаправляет пользователей на сайты авиакомпаний и онлайн-турагентов.  

## Структура проекта
```plaintext
DiplomSkyPro/
├── locators/                     # Локаторы элементов страниц
│   ├── __init__.py               # Инициализация пакета locators
│   └── main_page_locators.py     # Локаторы элементов главной страницы
├── pages/                        # Реализация Page Object Model
│   ├── __init__.py               # Инициализация пакета pages
│   ├── aviasales_api.py          # Методы взаимодействия с API Aviasales
│   ├── base_page.py              # Базовый класс для страниц
│   └── main_page.py              # Класс главной страницы
├── tests/                        # Тестовые файлы
│   ├── __init__.py               # Инициализация пакета tests
│   ├── test_api.py               # Тесты для проверки API
│   └── test_ui.py                # Тесты для проверки UI
├── config.py                     # Конфигурация проекта
├── conftest.py                   # Фикстуры для Pytest
├── .gitignore                    # Игнорируемые файлы и папки Git
├── README.md                     # Описание проекта
├── requirements.txt              # Список зависимостей Python
└── External Libraries/           # Внешние библиотеки (менеджер зависимостей)
```
### Описание папок и файлов

- **`locators/`**: Содержит файлы с локаторами элементов страниц. 
  - `main_page_locators.py`: Локаторы для главной страницы.

- **`pages/`**: Реализация подхода Page Object Model (POM).
  - `base_page.py`: Базовый класс для страниц, содержащий общие методы.
  - `main_page.py`: Класс, реализующий функциональность главной страницы.
  - `aviasales_api.py`: Методы для работы с API Aviasales.

- **`tests/`**: Тестовые файлы.
  - `test_api.py`: Тесты для проверки API.
  - `test_ui.py`: Тесты для проверки UI.

- **`config.py`**: Файл конфигурации проекта.
- **`conftest.py`**: Фикстуры для Pytest (например, инициализация WebDriver).
- **`.gitignore`**: Файлы и папки, игнорируемые системой контроля версий Git.
- **`requirements.txt`**: Зависимости проекта для установки через `pip`.

---

## Команды для запуска тестов

### Установка зависимостей
Перед запуском тестов установите зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
````

### Запуск всех тестов:
```bash
pytest --alluredir=allure-results
```

### Запуск тестов API
```bash
pytest --alluredir=allure-results tests/test_api.py
```

### Запуск тестов UI
```bash
pytest --alluredir=allure-results tests/test_ui.py
```

### Генерация отчётов Allure
```bash
allure serve allure-results
```
