## English
##  Stock Analyzer 

### Purpose
The purpose of this code is to provide a stock analyzer application that can analyze and visualize the historical data of a given stock. It offers various technical indicators and predictions using linear regression to assist users in making informed investment decisions.

### Functionality
This Python code utilizes the Streamlit library to create a user-friendly interface for the stock analyzer application. It retrieves stock data from the Yahoo Finance API and presents it in a visually appealing and interactive manner. The application offers the following features:

- **Display of stock data:** The application retrieves and displays the historical stock data for a given stock ticker symbol.

- **Technical indicators:** Users can explore various technical indicators such as Close Prices, Relative Strength Index (RSI), Bollinger Bands, On-Balance Volume (OBV), Moving Average Convergence Divergence (MACD), Momentum, and Support/Resistance. These indicators provide insights into the stock's price trends, momentum, and potential support and resistance levels.

- **Linear Regression Predictions:** The application utilizes linear regression to generate predictions for future stock prices based on historical data.

- **Chart zooming:** Users can zoom in on the charts to examine the stock's support and resistance levels more closely.

- **Indicator explanations:** The application provides explanations and descriptions for each technical indicator to help users understand their significance and interpretation.

### Usage
To use the stock analyzer application:

- Install the necessary dependencies by running the command: pip install streamlit numpy pandas yahoo_fin matplotlib mpld3 pandas_ta sklearn fpdf.

- Execute the code by running: streamlit run stock_analyzer.py.

- The Streamlit server will start, and the application will open in your browser.

- Enter the desired stock ticker symbol in the text input field. If no ticker is entered, the default ticker "GOOG" will be used.

- The application will retrieve the stock data and display the entered ticker. You can then explore the various technical indicators, predictions, and charts.

### Contributing
If you wish to contribute to this project, feel free to fork the repository and make any desired changes. You can also contribute by opening issues or submitting pull requests for improvements or bug fixes.

### License
This code is licensed under the MIT License. You are free to use, modify, and distribute it in accordance with the terms of the license.

### Disclaimer
Please note that this code and the information provided by the application are intended for educational and informational purposes only. They should not be considered as financial advice. Always conduct your own research and consult with a financial professional before making any investment decisions.


## Türkçe
## Hisse Senedi Analizörü

### Amaç
Bu kodun amacı, belirli bir hisse senedinin geçmiş verilerini analiz edebilen ve görselleştirebilen bir hisse senedi analizörü uygulaması sunmaktır. Lineer regresyon kullanarak çeşitli teknik göstergeler ve tahminler sunarak kullanıcıların bilinçli yatırım kararları almasına yardımcı olur.

### İşlevsellik
Bu Python kodu, hisse senedi analizörü uygulaması için kullanıcı dostu bir arayüz oluşturmak için Streamlit kütüphanesini kullanır. Yahoo Finance API'den hisse senedi verilerini alır ve görsel olarak çekici ve etkileşimli bir şekilde sunar. Uygulama aşağıdaki özellikleri sunar:

- **Hisse senedi verilerinin görüntülenmesi:** Uygulama, belirli bir hisse senedi sembolü için geçmiş hisse senedi verilerini alır ve görüntüler.

- **Teknik göstergeler:** Kullanıcılar Kapanış Fiyatları, Göreceli Güç Endeksi (RSI), Bollinger Bantları, On-Balance Volume (OBV), Hareketli Ortalama Yakınsama Diverjansı (MACD), Momentum ve Destek/Direnç gibi çeşitli teknik göstergeleri inceleyebilir. Bu göstergeler, hisse senedinin fiyat trendleri, momentumu ve potansiyel destek ve direnç seviyeleri hakkında bilgi sağlar.

- **Lineer Regresyon Tahminleri:** Uygulama, geçmiş verilere dayanarak gelecekteki hisse senedi fiyatları için tahminler oluşturmak için lineer regresyon kullanır.

- Grafik yakınlaştırma: Kullanıcılar grafikleri yakınlaştırarak hisse senedinin destek ve direnç seviyelerini daha yakından inceleyebilir.

- **Gösterge açıklamaları:** Uygulama, her teknik gösterge için açıklamalar ve tanımlamalar sunar, böylece kullanıcılar bunların önemini ve yorumunu anlamalarına yardımcı olur.

### Kullanım
Hisse senedi analizörü uygulamasını kullanmak için:

- Gerekli bağımlılıkları yüklemek için şu komutu çalıştırın: pip install streamlit numpy pandas yahoo_fin matplotlib mpld3 pandas_ta sklearn fpdf.

- Kodu çalıştırmak için şu komutu çalıştırın: streamlit run stock_analyzer.py.

- Streamlit sunucusu başlayacak ve uygulama tarayıcınızda açılacaktır.

- Metin giriş alanına istediğiniz hisse senedi sembolünü girin. Eğer sembol girilmezse, varsayılan sembol olarak "GOOG" kullanılacaktır.

- Uygulama hisse senedi verilerini alacak ve girilen sembolü görüntüleyecektir. Ardından çeşitli teknik göstergeleri, tahminleri ve grafikleri keşfedebilirsiniz.

### Katkıda Bulunma
Bu projeye katkıda bulunmak isterseniz, depoyu çatallayabilir ve istediğiniz değişiklikleri yapabilirsiniz. Ayrıca, iyileştirmeler veya hata düzeltmeleri için sorunları açabilir veya birleştirme istekleri gönderebilirsiniz.

### Lisans
Bu kod MIT Lisansı altında lisanslanmıştır. Lisansın şartlarına uygun olarak özgürce kullanabilir, değiştirebilir ve dağıtabilirsiniz.

### Feragatname
Lütfen bu kodu ve uygulama tarafından sağlanan bilgileri yalnızca eğitim ve bilgilendirme amaçlı olarak kullanın. Finansal tavsiye olarak değerlendirilmemelidir. Her zaman kendi araştırmanızı yapın ve yatırım kararları vermeden önce bir finansal uzmana danışın.
