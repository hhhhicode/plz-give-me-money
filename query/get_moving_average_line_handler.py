def get_moving_average_line(df, window):
    return df['trade_price'].rolling(window=window, min_periods=1).mean()