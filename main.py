from service import moving_average_line_service, graph_handler_service, candles_handler_service
from utils import ip_utils
import json
import schedule
import time
import streamlit as st
import service.my_upbit as my_upbit
import service.my_gpt as my_gpt


def make_decision_and_execute():
    print("Making decision and executing...")

    data_json = my_upbit.fetch_and_prepare_data()
    advice = my_gpt.analyze_data_with_gpt4(data_json)

    try:
        decision = json.loads(advice)
        print(decision)
        # if decision.get('decision') == "buy":
        #     my_upbit.buy_coin("KRW-BTC", 100000, 100000*0.9995)
        # elif decision.get('decision') == "sell":
        #     my_upbit.sell_all_coin("BTC", "KRW-BTC")
    except Exception as e:
        print(f"Failed to parse the advice as JSON: {e}")

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

    st.plotly_chart(fig, config=plotly_config)


if __name__ == "__main__":
    make_decision_and_execute()
    schedule.every().hour.at(":01").do(make_decision_and_execute)

    while True:
        schedule.run_pending()
        time.sleep(1)
