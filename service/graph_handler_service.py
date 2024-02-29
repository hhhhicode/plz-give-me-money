import plotly.graph_objects as go
import numpy as np


def plot_candlestick(df):
    fig = go.Figure(data=[go.Candlestick(x=df['candle_date_time_kst'],
                                         open=df['opening_price'],
                                         high=df['high_price'],
                                         low=df['low_price'],
                                         close=df['trade_price'])])

    # 이동 평균선
    fig.add_trace(go.Scatter(x=df['candle_date_time_kst'], y=df['MA10'], mode='lines', name='MA 10',
                             line=dict(color='white', width=1)))
    fig.add_trace(go.Scatter(x=df['candle_date_time_kst'], y=df['MA20'], mode='lines', name='MA 20',
                             line=dict(color='red', width=1)))
    fig.add_trace(go.Scatter(x=df['candle_date_time_kst'], y=df['MA60'], mode='lines', name='MA 60',
                             line=dict(color='green', width=1)))

    # 레이아웃 설정
    fig.update_layout(
        title='Candles with Moving Averages',
        xaxis=dict(
            showgrid=True,  # x축 격자무늬 표시
            gridcolor='LightGrey',  # 격자무늬 색상 설정
            tickformat='%Y-%m-%d',
            fixedrange=False  # x축에 대해 확대/축소 허용
        ),
        xaxis_rangeslider_visible=False,  # 레인지 슬라이더 비활성화
        xaxis_title="시간 (KST)",
        yaxis=dict(
            showgrid=True,  # y축 격자무늬 표시
            gridcolor='LightGrey',  # 격자무늬 색상 설정
            fixedrange=False  # y축에 대해 확대/축소 허용
        ),
        yaxis_title="가격 (KRW)",
        yaxis_tickformat=','  # 천 단위 구분자를 사용하여 포맷 설정
    )
    return fig
