# api_binance_django_getdata_analyze_viewresult

Для реализации нужно зарегистрироваться на сайте https://www.binance.com/ и создать апи для тестов 

Нужно реализовать следующий алгоритм торгового робота:

1. Отслеживаем значения Moving average(для 5 минутных свечей, расчитывать на закрытии 9-ти свечей) по валютной паре BTC-USDT.
2. Если значение цены выше МА на заданное число мы продаем заданный обьем ВТС.
3. Если цена ниже МА на заданное число мы покупаем заданный объём ВТС.
4. После того как мы имеем открытую позицию производим закрытие позиции (обратная сделка), когда цена=МА


Реализовать простейший веб интерфейс для 

1) отслеживания открытых и закрытых ордеров
2) также в интерфейсе должна быть возможность настраивать отклонение от MA для покупки и продажи и объем создаваемого ордера



Результат

![alt tag](https://i.imgur.com/qzk2Tgv.png)


Для запуска проекта


1) зарегистрироваться на binance и создать api

binance.com


1.2) в файле trade_btcusdt_on_binance.py заменить набор символов своими ключами

API_KEY = 'ABCDabcd123456!@#$%'

API_SECRET = 'ABCDabcd123456!@#$%'


2) установить виртуальное окружение

$ virtualenv venv


3) запустить venv

$ source venv/bin/activate


4) установить django

$ pip install django


5) сделать миграции

$ python manage.py makemigrations

$ python manage.py migrate


6) создать суперюзера

$ python manage.py createsuperuser


7) запусить локальный сервер

$ python manage.py runserver


8) перейти в админку 

http://127.0.0.1:8000/admin


9) в админке создать два значения в поле Config

size_position

percent_deviation


10) запустить торговый скрипт

trade_btcusdt_on_binance.py


11) перейти в браузер

http://127.0.0.1:8000/
