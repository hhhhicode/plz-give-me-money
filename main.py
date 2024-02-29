from query import get_candles_handler
from utils import ip_utils
import streamlit as st


st.title('plz give me money')

st.write(ip_utils.get_internal_ip_address())

st.write(ip_utils.get_external_ip())

st.write(get_candles_handler.get_candles(15, "KRW-BTC", 200))