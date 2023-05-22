import streamlit as st
import numpy as np
import pandas as pd
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components
import pandas_ta as pta
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
import base64
from tempfile import NamedTemporaryFile

figs = []


st.markdown("""# Stock Analyser/Stok Analizi""")
st.markdown("""
### The one place for all your stock needs
We not only provide several technical indicators to understand the movement of the stock better but also 
we have a Neural Network to predict the future price.
### Tüm stok ihtiyaçlarınız için tek yer
Hisse senedi hareketini daha iyi anlamak için sadece birkaç teknik gösterge sağlamakla kalmıyor, aynı zamanda
gelecekteki fiyatı tahmin etmek için bir Sinir Ağımız var.
""")

# Get the stock ticker from user input
# Kullanıcıdan hisse senedi simgesini al
ticker = st.text_input('Stock Ticker')

# If no ticker is entered, set it as "GOOG" (default value)
# Eğer bir simge girilmemişse, varsayılan olarak "GOOG" olarak ayarla
if ticker == "":
    ticker = "GOOG"

# Display the entered ticker
# Girilen simgeyi görüntüle
st.write('Ticker entered: ', ticker)

# Get the stock data for the ticker from the financial API (e.g., Yahoo Finance)
# Finansal API'den (Örn: Yahoo Finance) simgeye ait hisse verilerini al
df = si.get_data(ticker)
df['date'] = df.index

# Extract the necessary data from the stock DataFrame
# Hisse DataFrame'inden gerekli verileri çıkar
open_prices = df['open']
close_prices = df['close']
volumes = df['volume']
high_prices = df['high']
low_prices = df['low']
dates = df['date']
DATA_LEN = 300  # Data length to consider

# Retrieve the last DATA_LEN number of data points for each data column
# Her veri sütunu için son DATA_LEN sayısı kadar veri noktasını al
dates = dates[len(dates) - DATA_LEN:len(dates)].to_list()
close_prices = close_prices[len(close_prices) - DATA_LEN:len(close_prices)].to_list()
open_prices = open_prices[len(open_prices) - DATA_LEN:len(open_prices)].to_list()
volumes = volumes[len(volumes) - DATA_LEN:len(volumes)].to_list()
high_prices = high_prices[len(high_prices) - DATA_LEN:len(high_prices)].to_list()
low_prices = low_prices[len(low_prices) - DATA_LEN:len(low_prices)].to_list()

# Select the 'close' column for further calculations
# İleriki hesaplamalar için 'close' sütununu seç
close_for_calc = df['close']
close_for_calc = close_for_calc[len(close_for_calc) - DATA_LEN:len(close_for_calc)]



st.text("");st.text("");st.text("")

st.markdown("## Technical Indicators/Teknik Göstergeler")

# Close prices plot/Kapanış Fiyatı Görselleştirme
fig = plt.figure()
plt.title(f"Close prices for: {ticker} currently at {round(close_prices[len(close_prices) - 1], 2)}", fontsize=15)
plt.xlabel("Days after", fontsize=12)
plt.ylabel("Price", fontsize=12)
plt.plot(close_prices, label='Close Price')
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)
st.markdown("***")


# RSI
relative_strength_indexs = pta.rsi(close_for_calc, length = 14)
relative_strength_indexs = relative_strength_indexs.to_list()

fig = plt.figure()
plt.plot(relative_strength_indexs, label='Share Price')
plt.title(f"RSI with period of 14 days", fontsize=17)
plt.xlabel("Number of days after", fontsize=15)
plt.ylabel("RSI Value", fontsize=15)
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)

st.text("")
st.markdown("In the given chart an RSI > 70 indicates an overbought share and an RSI < 30 indicates an oversold share." "/" "Verilen grafikte, RSI > 70 aşırı alım hissesini ve RSI < 30 aşırı satım hissesini gösterir.")

st.markdown("***")

# Bollinger Bands
# Calculate the rolling average of the close prices with a window size of 5
# 5 birimlik bir pencere boyutunda kapanış fiyatlarının hareketli ortalamasını hesapla
close_avg = close_for_calc.rolling(5).mean().to_list()

# Calculate the rolling standard deviations of the close prices with a window size of 5
# 5 birimlik bir pencere boyutunda kapanış fiyatlarının hareketli standart sapmasını hesapla
standard_deviations = close_for_calc.rolling(5).std().to_list()

upper_bollinger_band = []
lower_bollinger_band = []

# Calculate the upper and lower Bollinger Bands for each data point
# Her veri noktası için üst ve alt Bollinger Bantlarını hesapla
for i in range(len(standard_deviations)):
    # Calculate the upper bound as the close average plus two times the standard deviation
    # Üst sınırı, kapanış ortalaması artı iki kat standart sapma olarak hesapla
    upper_bound = close_avg[i] + (standard_deviations[i] * 2)

    # Calculate the lower bound as the close average minus two times the standard deviation
    # Alt sınırı, kapanış ortalamasından iki kat standart sapma çıkartarak hesapla
    lower_bound = close_avg[i] - (standard_deviations[i] * 2)

    upper_bollinger_band.append(upper_bound)
    lower_bollinger_band.append(lower_bound)



fig = plt.figure()
plt.plot(close_avg, label='Simple Moving Average')
plt.plot(upper_bollinger_band, label='Upper Band')
plt.plot(lower_bollinger_band, label='Lower Band')
plt.plot(close_prices, 'r', label='Close Price')
plt.title("Bollinger Bands with std of 2", fontsize=17)
plt.xlabel("Number of days after", fontsize=15)
plt.ylabel("Price", fontsize=15)
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)

st.markdown("***")


# OBV
on_balance_volumes = []
obv = 0

on_balance_volumes.append(obv)

# Calculate On-Balance Volume (OBV) for each data point
# Her veri noktası için On-Balance Volume (OBV) değerini hesapla
for i in range(1, len(volumes)):
    if close_prices[i] > close_prices[i - 1]:
        obv += volumes[i]
        on_balance_volumes.append(obv)

    elif close_prices[i] < close_prices[i - 1]:
        obv -= volumes[i]
        on_balance_volumes.append(obv)

    else:
        obv += 0
        on_balance_volumes.append(obv)


NUM_OF_DAYS_2 = 5
obv_df = pd.DataFrame(on_balance_volumes)
obv_sma = obv_df.rolling(NUM_OF_DAYS_2).mean()

fig = plt.figure()
plt.plot(on_balance_volumes, label='OBV')
plt.plot(obv_sma, label='Simple Moving Average for OBV')
plt.title("OBV :- On Balance Volume", fontsize=17)
plt.xlabel("Number of days after", fontsize=15)
plt.ylabel("OBV", fontsize=15)
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)

st.markdown("***")

# MACD
ema12 = close_for_calc.ewm(span=12, adjust=False).mean()
ema26 = close_for_calc.ewm(span=26, adjust=False).mean()

macd = ema12 - ema26

# Signal line of macd
signal = macd.ewm(span=9, adjust=False).mean()

fig = plt.figure()
plt.plot(macd.to_list(), label='MACD')
plt.plot(signal.to_list(), label='Signal')
plt.title("Moving Average Convergence Divergence", fontsize=17)
plt.ylabel("MACD", fontsize=15)
plt.xlabel("Days After", fontsize=15)
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)

st.markdown("***")


# Momentum
MOMENTUM_PERIOD = 10

momentum_values = []

# Calculate momentum values for each data point
# Her veri noktası için momentum değerlerini hesapla
for i in range(MOMENTUM_PERIOD, len(close_prices)):
    curr_close_price = close_prices[i]
    period_start_close_price = close_prices[i - MOMENTUM_PERIOD]

    # Calculate the momentum as the difference between the current closing price and the price from the start of the period
    # Momentumu, mevcut kapanış fiyatı ile dönem başından itibaren fiyat arasındaki fark olarak hesapla
    momentum_values.append(curr_close_price - period_start_close_price)

momentum_sum = 0

# Calculate the sum of momentum values
# Momentum değerlerinin toplamını hesapla
for i in range(len(momentum_values)):
    momentum_sum += momentum_values[i]

# Calculate the average momentum
# Ortalama momentumu hesapla
avg_momentum = momentum_sum / len(momentum_values)


fig = plt.figure()
plt.plot(momentum_values, label='Momentum Values')
plt.title(f"Momentum of stock over {MOMENTUM_PERIOD} days", fontsize=17)
plt.ylabel("Momentum", fontsize=15)
plt.xlabel("Days After", fontsize=15)
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)

# Resistance and support lines/Direnç ve destek hatları
pivot_points = []

# Calculate pivot points for each data point
# Her veri noktası için pivot noktalarını hesapla
for i in range(len(close_for_calc)):
    if i == 0:
        pivot_points.append(float("nan"))  # Set the first pivot point as NaN
    else:
        prev_high = high_prices[i - 1]
        prev_low = low_prices[i - 1]
        prev_close = close_prices[i - 1]

        # Calculate the pivot point as the average of the previous high, low, and close prices
        # Pivot noktasını önceki yüksek, düşük ve kapanış fiyatlarının ortalaması olarak hesapla
        pivot_point = (prev_high + prev_low + prev_close) / 3
        pivot_points.append(pivot_point)

resistance_1 = []
support_1 = []
resistance_2 = []
support_2 = []

# Calculate support and resistance levels based on pivot points
# Pivot noktalarına göre destek ve direnç seviyelerini hesapla
for i in range(len(pivot_points)):
    if i == 0:
        resistance_1.append(float("nan"))  # Set the first resistance level as NaN
        support_1.append(float("nan"))  # Set the first support level as NaN
    else:
        # Calculate the first resistance and support levels using the previous day's high and low prices
        # Birinci direnç ve destek seviyelerini önceki günün yüksek ve düşük fiyatlarını kullanarak hesapla
        r1 = (2 * pivot_points[i]) - low_prices[i - 1]
        s1 = (2 * pivot_points[i]) - high_prices[i - 1]

        # Calculate the second resistance and support levels based on the first levels and the pivot point
        # İkinci direnç ve destek seviyelerini birinci seviyelere ve pivot noktasına göre hesapla
        r2 = (pivot_points[i] - s1) + r1
        s2 = pivot_points[i] - (r1 - s1)

        resistance_1.append(r1)
        support_1.append(s1)
        resistance_2.append(r2)
        support_2.append(s2)




fig = plt.figure()
plt.plot(close_prices, label='Close Price')
plt.plot(resistance_1, label='Resistance (first)')
plt.plot(support_1, label='Support (first)')
plt.plot(resistance_2, label='Resistance (second)')
plt.plot(support_2, label='Support (second)')
plt.xlabel("Days After", fontsize=15)
plt.ylabel("Price", fontsize=15)
plt.title("Support And Resistance", fontsize=17)
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)

st.text("")
st.markdown("To get a better view of the support and resistances please zoom into the chart.""/"" ""Destek ve dirençleri daha iyi görmek için lütfen grafiği yakınlaştırın.")

st.markdown("***")



st.markdown("## Linear Regression Predictions"
            
            "## Doğrusal Regresyon Tahminleri")


import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
import streamlit as st

# Linear Regression code

# Prepare the dataset/hazırla veri kümesi
dataset = close_prices

dataset = np.array(dataset)
training = len(dataset)
dataset = np.reshape(dataset, (dataset.shape[0], 1))

# Scale the dataset/veri kümesini ölçeklendirin
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

train_data = scaled_data[0:int(training), :]
print(len(train_data))

# Prepare features and labels/özellik ve etiketleri hazırla
x_train = []
y_train = []
prediction_days = 60

for i in range(prediction_days, len(train_data)):
    x_train.append(train_data[i-prediction_days:i, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1]))

# Train the Linear Regression model/Doğrusal Regresyon modelini eğitin
reg = LinearRegression().fit(x_train, y_train)

x_tomm = close_prices[len(close_prices) - prediction_days:len(close_prices)]
x_tomm = np.array(x_tomm)
x_tomm_reshaped = x_tomm.reshape(-1, 1)

# Scale the reshaped data/Yeniden şekillendirilmiş verileri ölçeklendirin
x_tomm_scaled = scaler.transform(x_tomm_reshaped)

# Reshape the scaled data back to (1, n_features)/Ölçeklenmiş verileri tekrar (1, n_features) olarak yeniden şekillendirin
x_tomm_scaled_reshaped = x_tomm_scaled.reshape(1, -1)

# Make the prediction/Tahmini yap
prediction = reg.predict(x_tomm_scaled_reshaped)
prediction = scaler.inverse_transform(prediction.reshape(1, -1))

# Display the prediction/Göster tahmini
st.markdown(f"#### Tomorrow's prediction for/Yarının tahmini için: {ticker} is {round(prediction[0][0], 2)}")



st.markdown("***")

# Future Predictions/Gelecek Tahminleri
import numpy as np
import streamlit as st

# User input for the number of future days (Recommended not to go over 20)
# Kullanıcıdan gelecek gün sayısı girişi (20'yi geçmemesi önerilir)
FUTURE_DAYS = st.text_input('Enter number of future days (Recommended not to go over 20) / Gelecek gün sayısını girin (20yi geçmemesi önerilir)')

try:
    FUTURE_DAYS = int(FUTURE_DAYS)
except:
    FUTURE_DAYS = 10

predicted_prices = []
tot_prices = list(close_prices)

# Predict future prices for the specified number of days
# Belirtilen gün sayısı için gelecekteki fiyatları tahmin et
for i in range(FUTURE_DAYS):
    x_prices = tot_prices[len(tot_prices) - prediction_days: len(tot_prices)]
    x_prices_reshaped = np.array(x_prices).reshape(1, -1)  # Reshape to have a single sample with multiple features
                                                           # Birden çok özelliğe sahip tek bir örneğe sahip olmak için yeniden şekillendirin
    
    # Scale each feature separately
    # Her özelliği ayrı ayrı ölçeklendirin
    x_prices_scaled = np.zeros_like(x_prices_reshaped)
    for j in range(x_prices_reshaped.shape[1]):
        feature = x_prices_reshaped[:, j]
        feature_scaled = scaler.transform(feature.reshape(-1, 1))
        x_prices_scaled[:, j] = feature_scaled.flatten()
    
    prediction = reg.predict(x_prices_scaled)
    
    # Inverse transform the prediction
    # Tahmini ters dönüştürme
    prediction_inverse_scaled = scaler.inverse_transform(prediction.reshape(-1, 1))
    
    tot_prices = np.concatenate((tot_prices, prediction_inverse_scaled.flatten()))
    predicted_prices.append(prediction_inverse_scaled)

tot_prices = np.array(tot_prices)
predicted_prices = np.array(predicted_prices)

tot_prices = np.reshape(tot_prices, (tot_prices.shape[0]))
predicted_prices = np.reshape(predicted_prices, (predicted_prices.shape[0]))




print(len(close_prices))
print(len(tot_prices))


fig = plt.figure()
plt.plot(tot_prices, label='Predicted Future Prices')
plt.plot(close_prices, label='Current Prices')
plt.xlabel("Days After", fontsize=15)
plt.ylabel("Price", fontsize=15)
plt.title("Future Price Predictions", fontsize=17)
plt.legend()
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=500)
figs.append(fig)






# PDF Download Functionality
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'



st.text("")
export_as_pdf = st.button("Export Report as PDF/Raporu PDF Olarak Dışa Aktar")

FONT_FAMILY = "Arial"
WIDTH = 210
HEIGHT = 297
name = ""

if export_as_pdf:
    # Create a new PDF instance
    # Yeni bir PDF örneği oluştur
    pdf = FPDF()
    pdf.add_page()

    # Set font and size for the main title
    # Ana başlık için yazı tipini ve boyutunu ayarla
    pdf.set_font(FONT_FAMILY, size=40)
    pdf.ln(40)
    pdf.multi_cell(w=0, h=15, txt=f"An analysis of the stock: {ticker}")

    # Add a new page for the introduction
    # Giriş için yeni bir sayfa ekle
    pdf.add_page()
    pdf.set_font(FONT_FAMILY, size=40)
    pdf.cell(0, txt="Introduction")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=13)
    pdf.multi_cell(w=0, h=7, txt=f"This report will analyse the stock: {ticker} using several technical indicators and other techniques which will give an idea about the future trends of the given stock.")
    pdf.ln(15)

    # Add a new page for the indicators used
    # Kullanılan göstergeler için yeni bir sayfa ekle
    pdf.set_font(FONT_FAMILY, size=40)
    pdf.cell(0, txt="Indicators Used")
    pdf.ln(15)

    # Define a list of indicators
    # Göstergelerin bir listesini tanımla
    indicators = ["RSI", "Bollinger Bands", "OBV", "MACD", "Momentum"]
    pdf.set_font(FONT_FAMILY, size=13)

    for i in range(len(indicators)):
        pdf.cell(0, txt=f"{i + 1}. {indicators[i]}")
        pdf.ln(6)

    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=40)
    pdf.cell(0, txt="RSI")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=13)
    pdf.multi_cell(w=0, h=7,
                   txt=f"The RSI or the Relative Strength Index gives us an indiaction if the stock/asset is overbought or oversold. An RSI >= 70 indicates that a stock has been overbought and a potential drop in price could be near, while a RSI <= 30 indicates that a stock has been oversold and can potentially have a bullish trend in the near future..")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=25)
    pdf.multi_cell(w=0, h=8, txt=f"RSI chart over the year for: {ticker} is given below.")
    pdf.ln(8)
    # Save the RSI chart as a temporary image file
    # RSI grafiğini geçici bir resim dosyası olarak kaydet
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[1].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name, 12, 100, WIDTH - 20, 100)
    name = ""
    pdf.ln(115)
    pdf.set_font(FONT_FAMILY, size=13)

    curr_rsi = relative_strength_indexs[len(relative_strength_indexs) - 1]
    rsi_mean = pd.Series(relative_strength_indexs).mean()

    rsi_state_rel = f"high" if curr_rsi > rsi_mean + 2.5 else f"low"
    rsi_state_abs = f"low" if curr_rsi < 45 else (f"medium" if curr_rsi < 60 else f"high")
    sell_state = f"selling" if rsi_state_abs == "low" else f"buying"
    price_action_dir = f"upward" if sell_state == "selling" else f"downward"

    pdf.multi_cell(w=0, h=7,
                   txt=f"As it is seen the current RSI is: {round(curr_rsi, 2)} which is considered{rsi_state_rel} relative to a 1 year trend of the stock. In a normal scenario such an rsi is considered {rsi_state_abs}. Thus this indicates that there has been more of. {sell_state} and that there can be an {price_action_dir} trend in the near future. Keep in mind that this is a meare technical indication which does not take into account any sentiments of people regarding the company or the general performance or profitablity of the company, thus there is a risk to using this strategy. This does not hold true for this but all the other indicators also used henceforth.")
    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=40)
    pdf.cell(0, txt="Bollinger Bands")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=13)
    pdf.multi_cell(w=0, h=7,
                   txt=f"Using bollinger bands one can get an idea about the volitility about the stock market and if there are any major trends in motion. Bollinger bands when supplemented with the RSI give us a very clear picture regarding the state of a stock.")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=25)
    pdf.multi_cell(
        w=0, h=10, txt=f"A visualization of the Bollinger Bands for: {ticker} over the year.")
    pdf.ln(8)
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[2].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name,
              12, 90, WIDTH - 20, 100)
    name = ""
    pdf.ln(100)
    pdf.set_font(FONT_FAMILY, size=13)

    close_price_sma_status = "above" if close_prices[len(close_prices) - 1] > close_avg[len(close_avg) - 1] else "below"
    close_sma_stat_msg = "this means that the stock is showing a bullish trend over the SMA period which in this case is 5 days.." if close_price_sma_status == "above" else "this means that either recently or over the SMA period the stock has shown a bearish trend"

    pdf.multi_cell(w=0, h=7,
                   txt=f"In this case we can see that the current close price is {close_price_sma_status} the simple moving average computed over a 5 day period {close_sma_stat_msg}")
    pdf.ln(8)

    closer_band = "upper band" if abs(
        upper_bollinger_band[len(upper_bollinger_band) - 1] - close_prices[len(close_prices) - 1]) < abs(
        lower_bollinger_band[len(lower_bollinger_band) - 1] - close_prices[len(close_prices) - 1]) else "lower band"

    print(abs(upper_bollinger_band[len(upper_bollinger_band) - 1] - close_prices[len(close_prices) - 1]))
    print(abs(lower_bollinger_band[len(
        lower_bollinger_band) - 1] - close_prices[len(close_prices) - 1]))

    pdf.multi_cell(w=0, h=7,
                   txt=f"So now we can move on and look at the upper and lower bollinger bands. We can see that the stock of our choice is closer to the {closer_band}. By looking at this we can identify the trend of the stock and also its strength. Thus this supplements our RSI indicator very smoothly.")

    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=40)
    pdf.cell(0, txt="OBV")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=13)
    pdf.multi_cell(w=0, h=7,
                   txt=f"OBV or On Balance Volume can be used to get an idea of the total running volume of an asset and track if it is moving up or down. Any major movements in the OBV of a stock can be used to track any movements made by large institutional investors..")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=25)
    pdf.multi_cell(
        w=0, h=10, txt=f"A visualization of the OBV for: {ticker} over the year.")
    pdf.ln(3)
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[3].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name,
              12, 90, WIDTH - 20, 100)
    name = ""
    pdf.ln(120)
    pdf.set_font(FONT_FAMILY, size=13)
    pdf.multi_cell(w=0, h=7,
                   txt=f'In this case if we look at the recent OBV trend we can get a good idea about the general outlook that the stock has among not just large instututions but even the average investor. Besides this the OBV indicator does not require any further details.')

    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=40)
    pdf.cell(0, txt="MACD")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=13)
    pdf.multi_cell(w=0, h=7,
                   txt="The MACD indicator gives us a good idea about the trend of the stock. An increase in the MACD value indicates "
                       "that the price is showing and probably willses the sign show an increasing trend, the converse is also true. Another thing "
                       "to note is that the intersection of the MACD and the signal line indicates the begining of a new trend.")

    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=25)
    pdf.multi_cell(
        w=0, h=10, txt=f"A visualization of the Momentum for: {ticker} over the year.")
    pdf.ln(3)
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[4].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name,
              11, 100, WIDTH - 20, 100)
    name = ""

    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=40)
    pdf.cell(0, txt="Momentum")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=13)
    pdf.multi_cell(w=0, h=7,
                   txt=f"The Momentum indicator as its name gives us an idea of a stock's momentum i.e the strength of the trend that a stock has. By taking a look at the momentum we can determine how long a buying, selling, bullish or bearish trend will continue.he Momentum indicator as its name gives us an idea of a stock's momentum i.e the strength of the trend that a stock has. By taking a look at the momentum we can determine how long a buying, selling, bullish or bearish trend will continue.")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=25)
    pdf.multi_cell(
        w=0, h=10, txt=f"A visualization of the Momentum for: {ticker} over the year.")
    pdf.ln(3)
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[5].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name,
              12, 90, WIDTH - 20, 100)
    name = ""
    pdf.ln(110)
    pdf.set_font(FONT_FAMILY, size=13)

    momentum_over_0 = "over zero" if momentum_values[len(momentum_values) - 1] > 0 else "below zero"
    curr_momentum = momentum_values[len(momentum_values) - 1]
    pdf.multi_cell(
        w=0, h=7,
        txt=f"By looking at the recent momentum values one can easily deduce the momentum of the stock. The stock currently is having a momentum of {round(curr_momentum, 2)} and an average momentum of {round(avg_momentum, 2)} over the year.")


    pdf.add_page()
    pdf.ln(5)
    pdf.set_font(FONT_FAMILY, size=40)
    pdf.cell(0, txt="Final Future Trend")
    pdf.ln(15)
    pdf.set_font(FONT_FAMILY, size=13)
    pdf.multi_cell(
        w=0, h=10, txt=f"Our Machine Learning model's prediction regarding {ticker} over {FUTURE_DAYS} days")
    # pdf.ln(3)
    with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        figs[7].savefig(tmpfile.name)
        name = tmpfile.name

    pdf.image(name,
              12, 70, WIDTH - 20, 100)
    name = ""
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), f"{ticker} analysis")
    st.markdown(html, unsafe_allow_html=True)
    st.text("")