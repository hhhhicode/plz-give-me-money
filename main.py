from service import moving_average_line_service, graph_handler_service, candles_handler_service
from utils import ip_utils
import numpy as np
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
    df = candles_handler_service.fetch_candle_data()
    moving_average_line_service.add_mv(df, [10, 20, 60])

    df['fill_color'] = np.where((df['MA10'] - df['MA20']) < 0, 'rgba(255, 0, 0, 0.3)', 'rgba(0, 0, 0, 0)')

    fig = graph_handler_service.plot_candlestick(df)

    st.plotly_chart(fig, config=plotly_config)
