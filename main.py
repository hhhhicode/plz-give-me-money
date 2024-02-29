import streamlit as st
import socket
import requests


candlesMinutes = 15
candlesMarket = "KRW-BTC"
candlesCount = 200

getCandlesUrl = ("https://api.upbit.com/v1/candles/minutes/"
                 + str(candlesMinutes)
                 + "?market="
                 + candlesMarket
                 + "&count="
                 + str(candlesCount))
getCandlesHeaders = {"accept": "application/json"}
# response = requests.get(getCandlesUrl, headers=getCandlesHeaders)
#
# print(response)

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Google DNS 서버를 이용
    return s.getsockname()[0]

print(get_ip_address())

# st.title('plz give me money')