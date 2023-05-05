import time
import yfinance as yf
from winotify import Notification, audio

tickers = ["AAPL","NVDA", "GS", "WFC"]
upper_limits = [160.4, 130, 240, 280, 70]
lower_limits = [160.2, 90, 140, 120, 60]

while True:
    last_prices = []
    for ticker in tickers:
        try:
            data = yf.download(ticker, period="1d", group_by='ticker')
            last_price = data["Adj Close"].iloc[-1]
            last_prices.append(last_price)
        except:
            print(f"Error retrieving data for {ticker}")
    print(last_prices)
    time.sleep(2)
    for i in range(len(tickers)):
        if last_prices[i] > upper_limits[i]:
            toast = Notification(app_id="Serkan Stock Alarm Bot",
                                  title=f"Price Alert For {tickers[i]}",
                                  msg=f"{tickers[i]} has reached a price of {last_prices[i]}. You might want to sell.")
            toast.add_actions(label="Go to Stockbroker", launch="https://softforware.tech/")
            toast.set_audio(audio.LoopingAlarm6, loop=True)
            toast.show()
        elif last_prices[i] < lower_limits[i]:
            toast = Notification(app_id="Serkan Stock Alarm Bot",
                                  title=f"Price Alert For {tickers[i]}",
                                  msg=f"{tickers[i]} has reached a price of {last_prices[i]}. You might want to buy.")
            toast.add_actions(label="Go to Stockbroker", launch="https://softforware.tech/")
            toast.set_audio
