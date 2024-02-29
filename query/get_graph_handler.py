import plotly.graph_objects as go


def plot_candlestick(df):
    fig = go.Figure(data=[go.Candlestick(x=df['candle_date_time_kst'],
                                         open=df['opening_price'],
                                         high=df['high_price'],
                                         low=df['low_price'],
                                         close=df['trade_price'])])

    fig.update_layout(
        xaxis=dict(
            tickformat='%Y-%m-%d'
        ),
        xaxis_rangeslider_visible=False,  # 레인지 슬라이더 비활성화
        xaxis_title="시간 (KST)",
        yaxis_title="가격 (KRW)",
        yaxis_tickformat=','  # 천 단위 구분자를 사용하여 포맷 설정
    )
    return fig
