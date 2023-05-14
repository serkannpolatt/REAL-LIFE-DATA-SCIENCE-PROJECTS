# Stok Analizi

## Türkçe

#### Bu kod, bir hisse senedinin teknik analizini yapmak için kullanılan bir araçtır.Kullanıcıdan bir hisse senedi sembolü alır ve o sembolle ilgili çeşitli teknik göstergeleri ve tahminleri sunar. Ayrıca, geçmiş verilere dayanarak gelecekteki fiyatları tahmin eder.

#### Kodun çalışması için aşağıdaki kütüphanelere ihtiyaç vardır:

```bash
pip install streamlit: Web tabanlı bir kullanıcı arayüzü oluşturmak için kullanılır.
import streamlit

```

```bash
pip install numpy: Sayısal hesaplamalar için kullanılır.
import streamlit
```

```bash
pip install pandas: Veri analizi için kullanılır.
import pandas
```

```bash
pip install yahoo_fin.stock_info: Hisse senedi verilerini çekmek için kullanılır.
import yahoo_fin.stock_info
```

```bash
pip install matplotlib.pyplot: Grafik çizimleri için kullanılır.
```

```bash
pip install mpld3: Matplotlib grafiklerini interaktif hale getirmek için kullanılır.
import mpld3
```

```bash
pip install pandas_ta: Teknik analiz göstergelerini hesaplamak için kullanılır.
import pandas_ta
```

```bash
pip install sklearn.preprocessing.MinMaxScaler: Verileri ölçeklendirmek için kullanılır.
import sklearn.preprocessing.MinMaxScaler
```

```bash
pip install sklearn.linear_model.LinearRegression: Doğrusal regresyon modeli oluşturmak için kullanılır.
import sklearn.linear_model.LinearRegression
```

```bash
pip install fpdf.FPDF: PDF dosyası oluşturmak için kullanılır.
import fpdf.FPDF
```

```bash
pip install base64: Dosya dönüşümleri için kullanılır.
import base64
```

```bash
pip install tempfile.NamedTemporaryFile: Geçici dosya oluşturmak için kullanılır.
import tempfile.NamedTemporaryFile
```

## Bu kod aşağıdaki işlevlere sahiptir:

- #### Kullanıcıdan bir hisse senedi sembolü alır.

- #### Seçilen hisse senedi için çeşitli teknik göstergeleri hesaplar ve grafiğini oluşturur.

- #### Gelecekteki fiyatları tahmin eder ve tahminlerin grafiğini oluşturur.
- #### Son olarak, oluşturulan raporu PDF formatında indirilebilir hale getirir.

# Stock Analyzer

## English

#### This code is a tool used to perform technical analysis of a stock. It takes a stock symbol from the user and provides various technical indicators and predictions related to that symbol. Additionally, it predicts future prices based on historical data.

# The code requires the following libraries to run:

```bash
pip install streamlit: Used to create a web-based user interface.
import streamlit
```

```bash
pip install numpy: Used for numerical computations.
import numpy
```

```bash
pip install pandas: Used for data analysis.
import pandas
```

```bash
pip install yahoo_fin.stock_info: Used to fetch stock data.
import yahoo_fin.stock_info
```

```bash
pip install matplotlib.pyplot: Used to make matplotlib graphs interactive.
import matplotlib.pyplot
```

```bash
pip install mpld3: Matplotlib grafiklerini interaktif hale getirmek için kullanılır.
import mpld3
```

```bash
pip install pandas_ta: Used to calculate technical analysis indicators.
import pandas_ta
```

```bash
pip install sklearn.preprocessing.MinMaxScaler: Used to scale data.
import sklearn.preprocessing.MinMaxScaler
```

```bash
pip install sklearn.linear_model.LinearRegression: Used to create a linear regression model.
import sklearn.linear_model.LinearRegression
```

```bash
pip install fpdf.FPDF: Used to create PDF files.
import fpdf.FPDF
```

```bash
pip install base64: Used for file conversions.
import base64
```

```bash
pip install tempfile.NamedTemporaryFile: Used to create temporary files.
import tempfile.NamedTemporaryFile
```

## This code has the following functionalities:

- #### Takes a stock symbol from the user.

- #### Calculates various technical indicators and plots the chart for the selected stock.

- #### Predicts future prices and plots the predictions chart.

- #### Finally, it makes the generated report downloadable in PDF format.