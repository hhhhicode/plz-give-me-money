from service import moving_average_line_service, graph_handler_service, candles_handler_service, cross_down_service
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
    df = candles_handler_service.fetch_candle_data()
    moving_average_line_service.add_mv(df, [10, 20, 60])

    fig = graph_handler_service.plot_candlestick(df)

    cross_down_service.add_cross_down_color(df, fig)

    st.plotly_chart(fig, config=plotly_config)
