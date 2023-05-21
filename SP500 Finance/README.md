

## English
## S&P 500 App
This Streamlit app retrieves the list of the S&P 500 companies from Wikipedia and displays their corresponding stock closing prices for the year-to-date. The purpose of this app is to provide an interactive interface for users to explore and analyze the stock data of S&P 500 companies.

### Python Libraries Used
- **streamlit:** Used for building the interactive web app.
- **pandas:** Used for data manipulation and analysis.
- **base64:** Used for encoding and decoding data for file download.
- **matplotlib:** Used for creating plots and visualizations.
- **seaborn:** Used for enhancing the visual appearance of plots.
- **numpy:** Used for numerical computations.
- **yfinance:** Used for downloading stock data from Yahoo Finance.

### Data Source
The data source for the S&P 500 companies is Wikipedia. The app scrapes the S&P 500 data from the Wikipedia page List of S&P 500 companies.

### User Input Features
The app includes a sidebar that allows users to select sectors of interest. The available sectors are dynamically populated based on the data retrieved from Wikipedia.

### Displaying Companies in Selected Sector
The app displays a table showing the companies in the selected sector. The table includes information such as the company name, ticker symbol, and other relevant data. The dimension of the data (number of rows and columns) is also displayed.

### Downloading S&P 500 Data
Users can download the displayed data as a CSV file. The "Download CSV File" link allows users to save the data locally.

### Stock Closing Price
The app utilizes the yfinance library to download the stock data for the selected companies. It retrieves the closing price of the stocks for the year-to-date period. Users can choose the number of companies to display using a slider in the sidebar.

### Plotting Closing Price
The app generates a line plot for each selected company, showing the closing price over time. The x-axis represents the date, and the y-axis represents the closing price. The plots are displayed when the "Show Plots" button is clicked.

> *Please note that this readme provides an overview of the functionality and purpose of the code. To run the app, you need to have the required libraries installed and execute the code using an appropriate development environment or tool.*

## Türkçe
## S&P 500 Uygulaması
Bu Streamlit uygulaması, S&P 500 şirketlerinin listesini Wikipedia'dan alır ve bunların yılın şu ana kadar olan hisse senedi kapanış fiyatlarını görüntüler. Bu uygulamanın amacı, kullanıcılara S&P 500 şirketlerinin hisse senedi verilerini keşfetmek ve analiz etmek için etkileşimli bir arayüz sağlamaktır.

### Kullanılan Python Kütüphaneleri
- **streamlit:** Etkileşimli web uygulaması oluşturmak için kullanılır.
- **pandas:** Veri manipülasyonu ve analizi için kullanılır.
- **base64:** Dosya indirme işlemleri için verinin kodlanması ve kod çözme işlemlerinde kullanılır.
- **matplotlib:** Grafik ve görselleştirmeler oluşturmak için kullanılır.
- **seaborn:** Grafiklerin görsel görünümünü geliştirmek için kullanılır.
- **numpy:** Sayısal hesaplamalar için kullanılır.
- **yfinance:** Hisse senedi verilerini Yahoo Finans'tan indirmek için kullanılır.

###Veri Kaynağı
S&P 500 şirketlerinin veri kaynağı Wikipedia'dır. Uygulama, S&P 500 verilerini Wikipedia'nın "List of S&P 500 companies" sayfasından çeker.

### Kullanıcı Giriş Özellikleri
Uygulama, kullanıcıların ilgilendikleri sektörleri seçmelerine olanak sağlayan bir yan panel içerir. Kullanılabilir sektörler, Wikipedia'dan alınan veriye bağlı olarak dinamik olarak oluşturulur.

### Seçilen Sektördeki Şirketlerin Gösterilmesi
Uygulama, seçilen sektördeki şirketleri gösteren bir tablo görüntüler. Tablo, şirket adı, sembol ve diğer ilgili veriler gibi bilgileri içerir. Verinin boyutu (satır ve sütun sayısı) de görüntülenir.

### S&P 500 Verisinin İndirilmesi
Kullanıcılar görüntülenen veriyi CSV dosyası olarak indirebilirler. "CSV Dosyasını İndir" bağlantısı kullanıcıların veriyi yerel olarak kaydetmelerine olanak sağlar.

### Hisse Senedi Kapanış Fiyatı
Uygulama, seçilen şirketlerin hisse senedi verilerini indirmek için yfinance kütüphanesini kullanır. Hisse senetlerinin yılın şu ana kadar olan kapanış fiyatlarını alır. Kullanıcılar, yan paneldeki bir kaydırıcı kullanarak görüntülenecek şirket sayısını seçebilirler.

### Kapanış Fiyatının Çizdirilmesi
Uygulama, her bir seçilen şirket için zaman içinde kapanış fiyatını gösteren bir çizgi grafiği oluşturur. X ekseni tarihi, Y ekseni ise kapanış fiyatını temsil eder. Çizelgeler, "Grafikleri Göster" düğmesine tıklandığında görüntülenir.

> *Lütfen bu readme dosyası, kodun işlevselliği ve amacı hakkında bir genel bakış sağlar. Uygulamayı çalıştırmak için gereken kütüphanelerin yüklü olduğundan emin olmalı ve kodu uygun bir geliştirme ortamında veya aracında çalıştırmalısınız.*
