import numpy as np
import plotly.graph_objects as go


def get_cross_down(df):
    return (df['MA10'] < df['MA20']) & (df['MA10'].shift(-1) >= df['MA20'].shift(-1))


def set_cross_down_color(df):
    df['color'] = np.where(get_cross_down(df), 'red')


def add_cross_down_color(df, fig):
    set_cross_down_color(df)
    for i in range(len(df) - 1):
        if df['color'].iloc[i] == 'red':
            fig.add_trace(go.Scatter(x=[df['candle_date_time_kst'].iloc[i], df['candle_date_time_kst'].iloc[i + 1]],
                                     y=[df['MA10'].iloc[i], df['MA10'].iloc[i + 1]],
                                     mode='lines',
                                     line=dict(color=df['color'].iloc[i], width=2),
                                     showlegend=False))
    fig.update_layout(title='Value with MA10 and MA20', xaxis_rangeslider_visible=False)
