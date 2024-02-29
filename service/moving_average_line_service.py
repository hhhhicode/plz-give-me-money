def get_moving_average_line(df, window):
    return df['trade_price'].rolling(window=window, min_periods=1).mean()


def add_mv(df, windows):
    sorted_df = df.sort_values(by='candle_date_time_kst', ascending=True, inplace=False)
    for window in windows:
        df['MA' + str(window)] = get_moving_average_line(sorted_df, window)
    return df
