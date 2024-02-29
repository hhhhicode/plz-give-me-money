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
response = requests.get(getCandlesUrl, headers=getCandlesHeaders)

st.write(response)

st.title('plz give me money')

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Google DNS 서버를 이용
    return s.getsockname()[0]

st.write(get_ip_address())

def get_external_ip():
    response = requests.get('https://httpbin.org/ip')
    return response.json()['origin']

st.write(get_external_ip())