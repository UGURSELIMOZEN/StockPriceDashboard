import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# STOCK Price Dashboard

""")

Tickers = pd.read_csv(r'C:\Users\Ugur\Desktop\Streamlit\Tickers.csv')

column_count_plot = st.sidebar.multiselect("STOCK TICKER  ",Tickers)

norm = st.sidebar.checkbox('Normalize')
start_date = st.sidebar.date_input('Start Date' , value = pd.to_datetime('2010-01-01'))
end_date = st.sidebar.date_input('End Date' , value = pd.to_datetime('today'))


def normalize(Price) :
    r = Price.pct_change()
    cumr = (1+r).cumprod()-1
    cumr = cumr.fillna(0)
    return cumr

if  len(column_count_plot) > 0 :
    Pricedata = yf.download(column_count_plot , start_date , end_date)['Adj Close']
    if norm :
        st.subheader('Normalized  Price Dashboard')
        pdata =normalize(Pricedata)
        st.line_chart(pdata)
    else :
        st.subheader('Close Price Dashboard')
        st.line_chart(Pricedata)

st.sidebar.text("Built with  ❤️  Streamlit")
