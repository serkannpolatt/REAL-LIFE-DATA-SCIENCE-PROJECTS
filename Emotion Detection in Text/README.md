## English
## Emotion Classifier Application
This application enables emotional analysis using a text classification model. It evaluates the text input provided by the user and predicts the emotional state of the text. Additionally, it tracks user interactions within the application and provides statistics related to page visits.

### How to Use
To run the application in a local environment, follow these steps:

1. Install the Python packages:
		pip install -r requirements.txt
2. Launch the application by running the following command in the terminal:
		streamlit run app.py
3. Open your web browser and go to http://localhost:8501.

### Features
**Prediction of Text Emotional State**
- On the home page, the user can enter text input.
- The entered text is evaluated using a text classification model to predict the emotional state.
- The prediction result and confidence score are displayed to the user.

**Page Tracking and Analysis**

- The application tracks the pages visited by users and stores this information.
- On the "Monitor" page, page visits and statistics are displayed.
- Page visits are presented in the form of charts and tables.

**Database**
- The application uses a SQLite database to store user interactions and prediction results. The database file is created as ./data/data.db.

### Libraries and Tools
The application has been developed using the following libraries and tools:

- **Streamlit:** A Python library used for creating web applications.
- **Altair:** A Python library used for data visualization.
- **Plotly Express:** A Python library used for creating interactive charts.
- **Pandas:** A Python library used for data analysis and manipulation.
- **NumPy:** A Python library used for scientific computing and data manipulation.
- **SQLite:** A lightweight relational database management system.

## Türkçe
## Duygu Sınıflandırıcı Uygulaması
Bu uygulama, bir metin sınıflandırma modeli kullanarak duygusal analiz yapmayı sağlar. Kullanıcıdan alınan metinleri değerlendirir ve metnin duygusal durumunu tahmin eder. Ayrıca, kullanıcıların uygulama üzerindeki etkileşimlerini izler ve sayfa ziyaretleriyle ilgili istatistikler sunar.

### Nasıl Kullanılır
Uygulamayı yerel bir ortamda çalıştırmak için aşağıdaki adımları izleyin:

1. Python paketlerini yükleyin:
		pip install -r requirements.txt
2. Uygulamayı başlatmak için terminalde aşağıdaki komutu çalıştırın:
		streamlit run app.py
3. Web tarayıcınızda http://localhost:8501 adresine gidin.

### Özellikler
**Metin Duygusal Durumunun Tahmini**
- Ana sayfada, kullanıcı metin girişi yapabilir.
- Girilen metin, metin sınıflandırma modeli kullanılarak duygusal durumu tahmin edilir.
- Tahmin sonucu ve güvenilirlik skoru kullanıcıya gösterilir.

**Sayfa İzleme ve Analiz**

- Uygulama, kullanıcıların ziyaret ettiği sayfaları izler ve bu bilgileri kaydeder.
- "Monitor" sayfasında, sayfa ziyaretleri ve istatistikleri görüntülenir.
- Sayfa ziyaretleri grafikler ve tablolar halinde sunulur.

**Veritabanı**
- Uygulama, kullanıcı etkileşimlerini ve tahmin sonuçlarını saklamak için bir SQLite veritabanı kullanır. Veritabanı dosyası ./data/data.db olarak oluşturulur.

### Kütüphaneler ve Araçlar
Uygulama aşağıdaki kütüphaneler ve araçlar kullanılarak geliştirilmiştir:

- **Streamlit:** Web uygulaması oluşturmak için kullanılan bir Python kütüphanesi.
- **Altair:** Veri görselleştirmesi için kullanılan bir Python kütüphanesi.
- **Plotly Express:** İnteraktif grafikler oluşturmak için kullanılan bir Python kütüphanesi.
- **Pandas:** Veri analizi ve manipülasyonu için kullanılan bir Python kütüphanesi.
- **NumPy:** Bilimsel hesaplama ve veri manipülasyonu için kullanılan bir Python kütüphanesi.
- **SQLite:** Küçük ölçekli veritabanı yönetim sistemi.