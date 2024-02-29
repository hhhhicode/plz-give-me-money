from query import get_candles_handler
from query import get_graph_handler
from utils import ip_utils
import streamlit as st

st.title('plz give me money')

st.write(ip_utils.get_internal_ip_address())

st.write(ip_utils.get_external_ip())

# Plotly 그래프의 config 설정을 분리하여 정의
plotly_config = {
    "scrollZoom": True,
    "dragMode": False
}

if st.button('그래프 보기'):
    df = get_candles_handler.fetch_candle_data()
    st.plotly_chart(get_graph_handler.plot_candlestick(df), config=plotly_config)
