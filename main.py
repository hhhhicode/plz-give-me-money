from query import get_candles_handler
from query import get_graph_handler
from query import get_moving_average_line_handler
from utils import ip_utils
import streamlit as st

st.title('plz give me money')

st.write(ip_utils.get_internal_ip_address())

st.write(ip_utils.get_external_ip())

# Plotly 그래프의 config 설정을 분리하여 정의
plotly_config = {
    "scrollZoom": True,
    "dragMode": "pan",
    "editable": False,    # 그래프의 편집 비활성화
}

if st.button('그래프 보기'):
    df = get_candles_handler.fetch_candle_data()
    df['MA10'] = get_moving_average_line_handler.get_moving_average_line(df, 10)
    df['MA20'] = get_moving_average_line_handler.get_moving_average_line(df, 20)
    df['MA60'] = get_moving_average_line_handler.get_moving_average_line(df, 60)

    fig = get_graph_handler.plot_candlestick(df)


    st.plotly_chart(fig, config=plotly_config)
