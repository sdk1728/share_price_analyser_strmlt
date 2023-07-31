import yfinance as yf 
import streamlit as st
import pandas as pd
import datetime 
st.write("""
         # Stock Price Analyser 
         """)

## get data for stocks
#symbol="TSLA"

symbol=st.selectbox("Which Stock do you want to analyse?",
                    ['GOOG','TSLA','MSFT','NFLX'])

col1,col2=st.columns(2)
with col1:
    start_date=st.date_input("Please Enter start date",datetime.date(2019,7,6))
with col2:
    end_date=st.date_input("Please Enter End Date",datetime.date(2023,7,30))

ticker_data=yf.Ticker(symbol)
ticker_df=ticker_data.history(period="id",start=start_date,end=end_date)

st.write(f"""
        ## {symbol}'s Stock Price         
        """)

st.dataframe(ticker_df)

st.write(f""" 
       ## {symbol}'s Closing Price Chart 
""")

st.line_chart(ticker_df['Close'])
