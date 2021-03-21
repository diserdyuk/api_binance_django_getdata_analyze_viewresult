from datetime import datetime
import time

from binance.client import Client

'''
import models StatusOrder from django project tradeonbinance
'''
import sys
import os
import django

sys.path.append('tradeonbinance')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tradeonbinance.settings'
django.setup()

from statusorders.models import StatusOrder, Config


TICKER = 'BTCUSDT'
# side
SHORT_POSITION = 'Short'
LONG_POSITION = 'Long'
WAITING_CONDITION = 'Waiting condition'
# status
NOT_POSITION ='Not opened position'
OPENED_LONG_POSITION = 'Opened long position'
OPENED_SHORT_POSITION = 'Opened short position'
CLOSED_LONG_POSITION = 'Closed long position'
CLOSED_SHORT_POSITION = 'Closed short position'
NOT_CLOSED_POSITION = 'Not closed position'

TIMEOUT = 300    # 5 min 
INTERVAL = Client.KLINE_INTERVAL_5MINUTE
QUANTITY_DATA_ROWS = 10
NUMBER_MOVING_AVERAGE = 9


API_KEY = 'ABCDabcd123456!@#$%'
API_SECRET = 'ABCDabcd123456!@#$%'


client = Client(API_KEY, API_SECRET)
print('logged in')


def get_percent_deviation():    
    return int(Config.objects.get(name='percent_deviation').value)


def get_size_position():
    return int(Config.objects.get(name='size_position').value)


def write_to_file(data):
    with open('status_and_orders_btcusdt.txt', 'a+') as file:
        file.write(f'{data}\n')


def get_online_data_binance():
    cnt = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    sum_prices = 0
    
    candles = client.get_klines(symbol=TICKER, interval=INTERVAL, limit=QUANTITY_DATA_ROWS)
    for i in candles:
        cnt += 1
        close = i[4]
        sum_prices += float(close)

        if cnt == NUMBER_MOVING_AVERAGE:
            mov_avg = (sum_prices/NUMBER_MOVING_AVERAGE)
            close_price = i[4]
        if cnt % QUANTITY_DATA_ROWS == 0:
            cnt = 0
            sum_prices = 0

            return (close_price, mov_avg)


def open_position(price, ma):
    price = float(price)
    ma = float(ma)
    percent = price / get_percent_deviation()

    if price > ma + percent:    
        return SHORT_POSITION 
    elif price < ma - percent:
        return LONG_POSITION
        

def close_position(side, open_posit):
    '''
    Returns true iff closed a position
    '''
    close, mov_avg = get_online_data_binance()
    open_posit = float(open_posit)
    price = float(close)
    mov_avg = float(mov_avg)

    if side == SHORT_POSITION and price <= mov_avg:    # closed short
        result_short = open_posit - price
        status_closed_short = f'closed short position: {result_short}, price: {price}'
        write_to_file(status_closed_short)
        StatusOrder.objects.create(ticker=TICKER, price=close, side=SHORT_POSITION, size=get_size_position(), time=f'{datetime.now()}', status=CLOSED_SHORT_POSITION)
        print(status_closed_short)
        return True
    elif side == LONG_POSITION and price >= mov_avg:    # closed long  
        result_long = price - open_posit
        status_closed_long = f'closed buy position: {result_long}, price: {price}'
        write_to_file(status_closed_long)
        StatusOrder.objects.create(ticker=TICKER, price=close, side=LONG_POSITION, size=get_size_position(), time=f'{datetime.now()}', status=CLOSED_LONG_POSITION)
        print(status_closed_long)
        return True
    else:
        status_closed_position = f'not closed position, date-time: {str(datetime.now())}, close price: {price}, moving average {mov_avg}'
        write_to_file(status_closed_position)
        StatusOrder.objects.create(ticker=TICKER, price=close, side=WAITING_CONDITION, size=get_size_position(), time=f'{datetime.now()}', status=NOT_CLOSED_POSITION)
        print(status_closed_position)
        time.sleep(TIMEOUT)
        return False


def trade():
    while True:
        close, mov_avg = get_online_data_binance() 
        write_to_file(str(datetime.now()))
        print(str(datetime.now()))

        price_mov_avg = f'close price: {close}, moving average: {mov_avg}'
        write_to_file(price_mov_avg)
        print(price_mov_avg)

        if open_position(close, mov_avg) == LONG_POSITION:    # opened long 
            check_price, side = close, LONG_POSITION 
            
            status_opened_long = f'buy market on: {close}, size pozition: {get_size_position()}'
            write_to_file(status_opened_long)
            StatusOrder.objects.create(ticker=TICKER, price=close, side=LONG_POSITION, size=get_size_position(), time=f'{datetime.now()}', status=OPENED_LONG_POSITION)
            print(status_opened_long)
            while True: 
                if close_position(side, check_price):
                    break

        elif open_position(close, mov_avg) == SHORT_POSITION:    # opened short
            check_price, side = close, SHORT_POSITION
 
            status_opened_short = f'short sell market on: {close}, size pozition: {get_size_position()}'
            write_to_file(status_opened_short)
            StatusOrder.objects.create(ticker=TICKER, price=close, side=SHORT_POSITION, size=get_size_position(), time=f'{datetime.now()}', status=OPENED_SHORT_POSITION)
            print(status_opened_short)
            while True:
                if close_position(side, check_price):
                    break
        else:
            status_no_position = 'no conditions for opening position'
            write_to_file(status_no_position)
            StatusOrder.objects.create(ticker=TICKER, price=close, side=WAITING_CONDITION, size=get_size_position(), time=f'{datetime.now()}', status=NOT_POSITION)
            print(status_no_position)

            time.sleep(TIMEOUT)


if __name__ == '__main__':
    trade()

