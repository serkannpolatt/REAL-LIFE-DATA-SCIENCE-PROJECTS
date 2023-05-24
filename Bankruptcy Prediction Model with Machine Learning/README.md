## English
## Bankruptcy Prediction
This project utilizes a logistic regression model to predict the likelihood of bankruptcy for a bank based on data. The relevant code segments include data loading, model training, and prediction operations.

### **Usage**
- numpy, pandas, matplotlib.pyplot, and seaborn libraries are used in the project.
- The train_test_split function from the sklearn.model_selection module is used to split the dataset into training and testing subsets.
- The LogisticRegression class from the sklearn.linear_model module is used to apply the logistic regression model.
- The accuracy_score function from the sklearn.metrics module is used to compute the accuracy score of the model.
- The warnings library is used to ignore warning messages.
- Data is read from a CSV file named "bank.csv" and stored in the data DataFrame.
- The dataset is divided into independent variables (X) and the dependent variable (y) using the Bankrupt? column as the target variable.
- The dataset is split into training and testing subsets using the train_test_split function, with a test size of 20%.
- The LogisticRegression class is used to create a logistic regression model and fit it with the training data.
- The accuracy score of the model is calculated on the test data using the score method.

### **Dependencies**
- **numpy:** A library used for scientific computations.
- **pandas:** A library used for data analysis and manipulation.
- **matplotlib.pyplot**: A library used for data visualization.
- **seaborn:** A library used for visual analysis.
- **sklearn:** A library used for machine learning models and metrics.
- **warnings:** A library used to manage warning messages.



## Türkçe
## Banka İflası Tahmini
Bu proje, verileri kullanarak bir bankanın iflas olasılığını tahminlemek için bir lojistik regresyon modeli kullanır. İlgili kod parçaları, veri yükleme, model eğitimi ve tahmin yapma işlemlerini içerir.

### **Kullanım**
- numpy, pandas, matplotlib.pyplot ve seaborn kütüphaneleri projede kullanılır.
- sklearn.model_selection modülündeki train_test_split fonksiyonu, veri kümesini eğitim ve test alt kümelerine ayırmak için kullanılır.
- sklearn.linear_model modülündeki LogisticRegression sınıfı, lojistik regresyon modelini uygulamak için kullanılır.
- sklearn.metrics modülündeki accuracy_score fonksiyonu, modelin doğruluk skorunu hesaplamak için kullanılır.
- warnings kütüphanesi, uyarı mesajlarını görmezden gelmek için kullanılır.
- bank.csv adlı bir CSV dosyasından veri okunur ve data DataFrame'ine aktarılır.
- Veri seti, Bankrupt? sütununu hedef değişken olarak kullanarak bağımsız değişkenler (X) ve bağımlı değişken (y) olarak ayrılır.
- Veri seti, train_test_split fonksiyonu kullanılarak eğitim ve test alt kümelerine ayrılır. Test boyutu, %20 olarak belirlenir.
- LogisticRegression sınıfı bir lojistik regresyon modeli oluşturmak için kullanılır ve eğitim verileriyle uyum sağlar.
- Modelin doğruluk skoru, score yöntemi kullanılarak test verileri üzerinde hesaplanır.

### **Bağımlılıklar**
- **numpy:** Bilimsel hesaplamalar için kullanılan bir kütüphanedir.
- **pandas:** Veri analizi ve işleme için kullanılan bir kütüphanedir.
- **matplotlib.pyplot:** Veri görselleştirme için kullanılan bir kütüphanedir.
- **seaborn:** Görsel analiz için kullanılan bir kütüphanedir.
- **sklearn:** Makine öğrenimi modelleri ve metrikleri için kullanılan bir kütüphanedir.
- **warnings**: Uyarı mesajlarını yönetmek için kullanılan bir kütüphanedir.


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
