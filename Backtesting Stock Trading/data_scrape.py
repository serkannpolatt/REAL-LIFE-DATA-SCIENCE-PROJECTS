import datetime as dt 
import yfinance as yf

start = dt.datetime(2020,1,1)
end = dt.datetime.now()

data = yf.download("TSLA", start=start, end=end)

data.to_csv("stock_data.csv")
