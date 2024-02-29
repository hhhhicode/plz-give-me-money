def get_moving_average_line(df, window):
    return df['trade_price'].rolling(window=window, min_periods=1).mean()


def add_mv(df, window):
    df['MA' + str(window)] = get_moving_average_line(df, window)
    return df
