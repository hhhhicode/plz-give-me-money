import streamlit as st
import requests

st.title('plz give me money')

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
response = requests.get(getCandlesUrl, headers = getCandlesHeaders)

print(response)

