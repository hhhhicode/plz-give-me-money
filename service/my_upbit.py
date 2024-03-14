import os
import pyupbit
import pandas as pd
import pandas_ta as ta
import json
from dotenv import load_dotenv


load_dotenv()
upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))


def get_current_status():
    orderbook = pyupbit.get_orderbook(ticker="KRW-BTC")
    current_time = orderbook['timestamp']
    btc_balance = 0
    krw_balance = 0
    btc_avg_buy_price = 0
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == "BTC":
            btc_balance = b['balance']
            btc_avg_buy_price = b['avg_buy_price']
        if b['currency'] == "KRW":
            krw_balance = b['balance']

    current_status = {'current_time': current_time, 'orderbook': orderbook, 'btc_balance': btc_balance,
                      'krw_balance': krw_balance, 'btc_avg_buy_price': btc_avg_buy_price}
    return json.dumps(current_status)


def buy_coin(ticker, min_balance, amount):
    print("Attempting to buy BTC...")
    try:
        krw = upbit.get_balance("KRW")
        if krw >= min_balance:
            # result = upbit.buy_market_order("KRW-BTC", krw*0.9995)
            result = upbit.buy_market_order(ticker, amount)
            print("Buy order successful:", result)
    except Exception as e:
        print(f"Failed to execute buy order: {e}")


def sell_all_coin(balance_ticker, order_ticker):
    print("Attempting to sell BTC...")
    try:
        coin = upbit.get_balance(balance_ticker)
        current_price = pyupbit.get_orderbook(ticker=order_ticker)['orderbook_units'][0]["ask_price"]
        if current_price * coin > 5000:
            result = upbit.sell_market_order(order_ticker, coin)
            print("Sell order successful:", result)
    except Exception as e:
        print(f"Failed to execute sell order: {e}")


def get_balance(ticker):
    return upbit.get_balance(ticker)


def buy_market_order(ticker, amount):
    return upbit.buy_market_order(ticker, amount)


def fetch_and_prepare_data():
    # Fetch data
    df_daily = pyupbit.get_ohlcv("KRW-BTC", "day", count=30)
    df_hourly = pyupbit.get_ohlcv("KRW-BTC", interval="minute60", count=24)

    # Define a helper function to add indicators
    def add_indicators(df):
        # Moving Averages
        df['SMA_10'] = ta.sma(df['close'], length=10)
        df['EMA_10'] = ta.ema(df['close'], length=10)

        # RSI
        df['RSI_14'] = ta.rsi(df['close'], length=14)

        # Stochastic Oscillator
        stoch = ta.stoch(df['high'], df['low'], df['close'], k=14, d=3, smooth_k=3)
        df = df.join(stoch)

        # MACD
        ema_fast = df['close'].ewm(span=12, adjust=False).mean()
        ema_slow = df['close'].ewm(span=26, adjust=False).mean()
        df['MACD'] = ema_fast - ema_slow
        df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
        df['MACD_Histogram'] = df['MACD'] - df['Signal_Line']

        # Bollinger Bands
        df['Middle_Band'] = df['close'].rolling(window=20).mean()
        # Calculate the standard deviation of closing prices over the last 20 days
        std_dev = df['close'].rolling(window=20).std()
        # Calculate the upper band (Middle Band + 2 * Standard Deviation)
        df['Upper_Band'] = df['Middle_Band'] + (std_dev * 2)
        # Calculate the lower band (Middle Band - 2 * Standard Deviation)
        df['Lower_Band'] = df['Middle_Band'] - (std_dev * 2)

        return df

    # Add indicators to both dataframes
    # 한달간 일봉과 24시간간 1시간봉 데이터를 가져와서 각각의 데이터에 지표를 추가합니다.
    df_daily = add_indicators(df_daily)
    df_hourly = add_indicators(df_hourly)

    combined_df = pd.concat([df_daily, df_hourly], keys=['daily', 'hourly'])
    combined_data = combined_df.to_json(orient='split')

    # make combined data as string and print length
    print(len(combined_data))

    return json.dumps(combined_data)
