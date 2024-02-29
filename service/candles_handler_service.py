import requests
import pandas as pd


def get_candles_data(market, minutes, count):
    get_candles_url = ("https://api.upbit.com/v1/candles/minutes/" + str(minutes)
                       + "?market=" + market
                       + "&count=" + str(count))
    get_candles_headers = {"accept": "application/json"}
    return requests.get(get_candles_url, headers=get_candles_headers).json()


def fetch_candle_data():
    data = get_candles_data("KRW-BTC", 15, 200)
    # API 응답에서 데이터 프레임 생성
    df = pd.DataFrame(data, columns=['candle_date_time_kst', 'opening_price', 'high_price', 'low_price', 'trade_price',
                                     'candle_acc_trade_volume'])
    df['candle_date_time_kst'] = pd.to_datetime(df['candle_date_time_kst'])
    return df
