## English
## Stock Alarm and Stock Data Collection
This project includes useful code snippets in Python for monitoring stock prices using an alarm system and collecting stock data.

### Usage
#### **Stock Alarm**
- Uses the yf.download function to retrieve stock data using the yfinance library.
- The tickers list contains the stock symbols you want to monitor.
- The upper_limits and lower_limits lists contain the upper and lower price limits for specific stock symbols.
- Runs in an infinite loop and waits for a specified period of time (e.g., 2 seconds).
- In each iteration, retrieves the latest stock data using yf.download.
- The stock price is obtained from the latest closing price in the Adj Close column.
- The obtained prices are added to the last_prices list.
- Compares the prices with the upper_limits and lower_limits and sends a notification to the user when a specific price threshold is reached.
- The Notification class uses the winotify library to create Windows notifications.
- Notifications are created with a specific message, title, and actions (e.g., redirection to a link).
- When a price threshold is reached, a notification is displayed, and the loop continues.

### **Stock Data Collection**

- Retrieves stock data using the yf.download function to collect stock data using the yfinance library.
- The start and end variables specify the start and end dates for the data collection.
- The stock symbol is set as "TSLA". You can use your desired symbol.
- The retrieved data is saved in a DataFrame named data.
- The data.to_csv function allows saving the data to a CSV file. You can modify the name and path of the file.

#### **Dependencies**
- **time:** It is a standard library in Python used for time operations.
- **yfinance:** It is a library used for retrieving financial data. You can install it using the pip install yfinance command.
- **winotify:** It is a library used for creating Windows notifications. You can install it using the pip install winotify command.
- **backtesting (optional):** It is a library used for testing stock strategies. If you want to use the relevant part in your project, you can install it using the pip install backtesting command.


## Türkçe
## Borsa Alarmı ve Hisse Senedi Veri Toplama
Bu proje, Python kullanarak borsa fiyatlarını izlemek için bir alarm sistemi ve hisse senedi verilerini toplamak için yararlı kod parçaları içerir.

### **Kullanım**
#### Borsa Alarmı
- yfinance kütüphanesini kullanarak borsa verilerini almak için yf.download fonksiyonunu kullanır.
- tickers listesi, izlemek istediğiniz hisse senedi sembollerini içerir.
- upper_limits ve lower_limits listeleri, belirli hisse senedi sembolleri için üst ve alt fiyat limitlerini içerir.
- Sonsuz bir döngü içinde çalışır ve belirli bir süre (örneğin, 2 saniye) bekler.
- Her döngüde, yf.download kullanılarak güncel hisse senedi verileri alınır.
- Hisse senedi fiyatı, Adj Close sütunundaki son kapanış fiyatından alınır.
- Alınan fiyatlar, last_prices listesine eklenir.
- upper_limits ve lower_limits ile karşılaştırılır ve belirli bir fiyat eşiğine ulaşıldığında kullanıcıya bir bildirim gönderilir.
- Notification sınıfı, Windows bildirimleri oluşturmak için winotify kütüphanesini kullanır.
- Bildirimler, belirli bir mesaj, başlık ve eylemlerle (örneğin, bir bağlantıya yönlendirme) oluşturulur.
- Belirli bir fiyat eşiğine ulaşıldığında, bildirim gösterilir ve bir döngüye devam edilir.

#### **Hisse Senedi Veri Toplama**
- yfinance kütüphanesini kullanarak hisse senedi verilerini almak için yf.download fonksiyonunu kullanır.
- start ve end değişkenleri, toplanacak verilerin başlangıç ve bitiş tarihlerini belirtir.
- Hisse senedi sembolü "TSLA" olarak ayarlanmıştır. İstediğiniz sembolü kullanabilirsiniz.
- Alınan veriler data adlı bir DataFrame'e kaydedilir.
- data.to_csv fonksiyonu, verilerin CSV formatında bir dosyaya kaydedilmesini sağlar. İsim ve kayıt yolu değiştirilebilir.

### **Bağımlılıklar**
- **time:** Python'ın standart kütüphanesidir ve zaman işlemleri için kullanılır.
- **yfinance:** Finansal verileri almak için kullanılan bir kütüphanedir. Kurulum için pip install yfinance komutunu kullanabilirsiniz.
- **winotify: **Windows bildirimleri oluşturmak için kullanılan bir kütüphanedir. Kurulum için pip install winotify komutunu kullanabilirsiniz.
- **backtesting (opsiyonel): **Hisse senedi stratejilerini test etmek için kullanılan bir kütüphanedir. İlgili kısımı projenizde kullanmak isterseniz, kurulum için pip install backtesting komutunu kullanabilirsiniz.
