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


зарегистрироваться на binance и создать api
binance.com


установить виртуальное окружение
$ virtualenv venv


запустить venv
$ source venv/bin/activate


установить django
pip install django


сделать миграции
$ python manage.py makemigrations
$ python manage.py migrate


создать суперюзера
$ python manage.py createsuperuser


запусить локальный сервер
$ python manage.py runserver


перейти в админку 
http://127.0.0.1:8000/admin


в админке создать два значения в поле Config
size_pozition
percent_deviation


запустить торговый скрипт


перейти в браузер
http://127.0.0.1:8000/
