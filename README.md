# DiplomSkyPro
Diplom
## Задача
Автоматизировать UI- и API-тесты из моей финальной работы по ручному тестированию.
## Финальный проект по ручному тестированию: Авиасейлс https://www.aviasales.ru/
## Описание тестируемой системы:
Авиасейлс ру - это популярный российский сайт, созданный для удобного поиска дешёвых авиабилетов в любые направления мира.  В качестве метапоиска Aviasales не продает авиабилеты, но перенаправляет пользователей на сайты авиакомпаний и онлайн-турагентов.  
## Шаги работы:
Были подключены зависимости:
selenium,
requests,
pytest,
allure
В проекте созданы файлы 
test\test_ui.py
 с UI-тестами.
test\test_api.py
 с API-тестами.
## Запуск тестов:
pytest --alluredir=allure-results tests/test_api.py - запуск тестов api
pytest --alluredir=allure-results tests/test_ui.py - запуск тестов ui
allure serve allure-result - формирование отчета
pytest --alluredir=allure-results - запуск всех тестов
