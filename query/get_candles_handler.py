import requests


def get_candles(market, minutes, count):
    get_candles_url = ("https://api.upbit.com/v1/candles/minutes/" + str(minutes)
                       + "?market=" + market
                       + "&count=" + str(count))
    get_candles_headers = {"accept": "application/json"}
    return requests.get(get_candles_url, headers=get_candles_headers).text
