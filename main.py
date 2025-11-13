import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings
import yfinance as yf
warnings.filterwarnings('ignore')

@st.cache_data
def load(tck):
    ticker_data = yf.Ticker(ticker)
    tickerDf = ticker_data.history( start='2012-01-01', end='2025-11-01')
    st.write('**Цены на закрытии торгов**')
    st.line_chart(tickerDf.Close)
    st.write('**Обьем продаж**')
    st.line_chart(tickerDf.Volume)
    pass



st.title('Катировки компании Apple')
st.write('Показаны цены на **закрытие** и **обьем**')

ticker = 'AAPL'
load(ticker)






