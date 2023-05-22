## English
## LSTM Stock Price Prediction
This code implements an LSTM (Long Short-Term Memory) model for stock price prediction. It uses historical stock price data of Tesla (TSLA) from a CSV file to train the model and predicts future stock prices.

### Dependencies
The following libraries are required to run the code:

- numpy for numerical computations
- pandas for data manipulation and analysis
- tensorflow for building and training the LSTM model
- matplotlib for plotting the stock price data

Additionally, the code imports the following modules and classes from other libraries:

- MinMaxScaler from sklearn.preprocessing for data normalization
- mean_squared_error from sklearn.metrics to evaluate the model's performance
- Sequential, Dense, LSTM, Dropout from tensorflow.keras.layers to build the LSTM model
- ModelCheckpoint, EarlyStopping from tensorflow.keras.callbacks for model checkpointing and early stopping

### Data Loading and Exploration
The code reads stock price data from a CSV file (TSLA.csv) using pandas and displays some basic information about the dataset, such as its shape, data types, head, tail, missing values, and quantiles.

### Data Preprocessing
The code performs the following steps to preprocess the data:

- Converts the "Date" column to a datetime format
- Selects the "Date" and "Close" columns from the dataset for further processing
- Sets the "Date" column as the index
- Drops the "Date" column from the dataset
- Displays a plot of the stock price data using matplotlib

### Data Splitting and Scaling
The code splits the preprocessed data into training and test sets. It uses the split_data function to split the data based on a specified test size. The function returns the training set, test set, and the position of the split.

Next, the code applies min-max scaling to the training and test sets using MinMaxScaler from sklearn.preprocessing. The scaling is done to normalize the data between the range of 0 and 1, which is beneficial for training the LSTM model.

### Creating Input Features
The code defines the create_features function, which creates input features and target variables for the LSTM model. It takes a data array and a lookback parameter as input and returns the input features (X) and target variables (Y) as numpy arrays.

The lookback parameter determines the number of previous time steps used to predict the current time step. The function iterates over the data array and creates X and Y pairs by considering a sliding window of size lookback.

The code then applies the create_features function to both the training and test sets to create the input features and target variables.

### Reshaping Input Data
The input data arrays are reshaped to fit the expected input shape of the LSTM model. The training and test sets are reshaped using np.reshape to add an additional dimension for the LSTM input.

### Model Architecture
The LSTM model architecture is defined using Sequential from tensorflow.keras.models. The model consists of the following layers:

- LSTM layer with 50 units, ReLU activation function, and input shape based on the training data shape
- Dropout layer with a dropout rate of 0.2
- Dense layer with 1 unit

The model summary is displayed, showing the layer configuration and the number of trainable parameters.

### Model Compilation and Training
The model is compiled with the mean squared error loss function and the Adam optimizer using model.compile. Additionally, a list of callbacks is defined for model checkpointing and early stopping.

The model is then trained using model.fit with the training data, target variables, and other parameters like the number of epochs, batch size, and validation data. The training history is stored in the history variable.

### Model Evaluation
The training and validation loss curves are plotted using matplotlib to visualize the model's training performance.

The model's loss is evaluated on the test set using model.evaluate. The loss value represents the mean squared error between the predicted and actual stock prices.

### Inverse Scaling and RMSE Calculation
The predicted values from the model are inverse transformed using the respective scalers to obtain the actual stock prices. The original target variables are also inverse transformed for comparison.

The root mean squared error (RMSE) is calculated between the actual and predicted stock prices for both the training and test sets. The RMSE provides a measure of the model's prediction error.

### Visualizing Predictions
The code selects the predicted stock prices from both the training and test sets and combines them with the original stock price data. The predicted values are plotted alongside the real values to visualize the model's predictions.

### Conclusion
This code demonstrates the use of LSTM for stock price prediction. It preprocesses the data, creates input features, builds and trains an LSTM model, evaluates the model's performance, and visualizes the predictions. The RMSE values provide an indication of the model's accuracy in predicting future stock prices.

## Türkçe
## LSTM Hisse Fiyatı Tahmini
Bu kod, hisse fiyatı tahmini için bir LSTM (Uzun Kısa Dönem Belleği) modelini uygular. Modeli eğitmek için Tesla (TSLA) hisse fiyatı geçmiş verilerini bir CSV dosyasından kullanır ve gelecekteki hisse fiyatlarını tahmin eder.

### Bağımlılıklar
Kodun çalışması için aşağıdaki kütüphanelere ihtiyaç vardır:

- Sayısal hesaplamalar için numpy
- Veri manipülasyonu ve analizi için pandas
- LSTM modelini oluşturmak ve eğitmek için tensorflow
- Hisse fiyatı verilerini çizdirmek için matplotlib

Ayrıca, kod diğer kütüphanelerden aşağıdaki modül ve sınıfları içe aktarır:

- Veriyi normalleştirmek için sklearn.preprocessing içindeki MinMaxScaler
- Modelin performansını değerlendirmek için sklearn.metrics içindeki mean_squared_error
- LSTM modelini oluşturmak için tensorflow.keras.layers içindeki Sequential, Dense, LSTM, Dropout
- Model kontrol noktaları ve erken durdurma için tensorflow.keras.callbacks içindeki ModelCheckpoint, EarlyStopping

### Veri Yükleme ve Keşfi
Kod, bir CSV dosyasından (TSLA.csv) hisse fiyatı verilerini pandas kullanarak okur ve veri kümesi hakkında temel bilgileri (şekil, veri tipleri, baş, son, eksik değerler, ve quantile'lar gibi) görüntüler.

### Veri Ön İşleme
Kod, veriyi ön işlemek için aşağıdaki adımları gerçekleştirir:

- "Tarih" sütununu datetime formatına dönüştürür
- İleride kullanmak için veri kümesinden "Tarih" ve "Kapanış" sütunlarını seçer
- "Tarih" sütununu indeks olarak ayarlar
- Veri kümesinden "Tarih" sütununu çıkarır
- Hisse fiyatı verilerinin bir çizimini matplotlib kullanarak görüntüler

### Veri Bölme ve Ölçeklendirme
Kod, ön işlenmiş veriyi eğitim ve test kümelerine böler. Veriyi belirtilen bir test boyutuna göre bölmek için split_data işlevini kullanır. İşlev, eğitim kümesini, test kümesini ve bölme konumunu döndürür.

Daha sonra, sklearn.preprocessing içindeki MinMaxScaler kullanarak eğitim ve test kümelerine min-max ölçeklendirme uygulanır. Ölçeklendirme, veriyi 0 ile 1 aralığında normalize etmek için yapılır ve bu, LSTM modelini eğitmek için faydalıdır.

### Giriş Özelliklerinin Oluşturulması
Kod, LSTM modeli için giriş özelliklerini ve hedef değişkenleri oluşturmak için create_features işlevini tanımlar. Veri dizisi ve bir "lookback" parametresi alır ve giriş özelliklerini (X) ve hedef değişkenleri (Y) numpy dizileri olarak döndürür.

"Lookback" parametresi, mevcut zaman adımını tahmin etmek için kullanılan önceki zaman adımlarının sayısını belirler. İşlev, veri dizisi üzerinde döngü yapar ve "lookback" boyutunda bir kaydırma penceresini dikkate alarak X ve Y çiftleri oluşturur.

Kod daha sonra create_features işlevini eğitim ve test kümelerine uygulayarak giriş özelliklerini ve hedef değişkenleri oluşturur.

### Giriş Verilerinin Yeniden Şekillendirilmesi
Giriş veri dizileri, LSTM modelinin beklenen giriş şekline uyması için yeniden şekillendirilir. Eğitim ve test kümeleri, LSTM girişi için ek bir boyut eklemek için np.reshape kullanılarak yeniden şekillendirilir.

### Model Mimarisi
LSTM modeli mimarisi, tensorflow.keras.models içindeki Sequential kullanılarak tanımlanır. Model aşağıdaki katmanlardan oluşur:

- 50 birime sahip LSTM katmanı, ReLU aktivasyon fonksiyonu ve eğitim veri şekline dayalı giriş şekli
- %20 dropout oranına sahip Dropout katmanı
- 1 birime sahip Dense katmanı

Modelin özeti görüntülenir, bu katman yapılandırmasını ve eğitilebilir parametre sayısını gösterir.

### Modelin Derlenmesi ve Eğitimi
Model, ortalama karesel hata kaybı fonksiyonu ve Adam optimize edici ile model.compile kullanılarak derlenir. Ayrıca, model kontrol noktaları ve erken durdurma için bir geri çağrılar listesi tanımlanır.

Model, model.fit kullanılarak eğitim verisi, hedef değişkenleri ve diğer parametreler (epok sayısı, grup boyutu, doğrulama verisi gibi) ile eğitilir. Eğitim geçmişi history değişkeninde saklanır.

### Modelin Değerlendirilmesi
Eğitim ve doğrulama kaybı eğrileri, modelin eğitim performansını görselleştirmek için matplotlib kullanılarak çizilir.

Modelin kaybı, model.evaluate kullanılarak test kümesinde değerlendirilir. Kayıp değeri, tahmin edilen ve gerçek hisse fiyatları arasındaki ortalama karesel hata anlamına gelir.

### Ters Ölçekleme ve RMSE Hesaplama
Modelden elde edilen tahmin değerleri, ilgili ölçekleyiciler kullanılarak gerçek hisse fiyatlarını elde etmek için ters dönüştürülür. Karşılaştırma yapmak için orijinal hedef değişkenler de ters dönüştürülür.

Kök ortalama karesel hata (RMSE), gerçek ve tahmin edilen hisse fiyatları arasındaki hata ölçüsünü sağlar. RMSE, hem eğitim hem de test kümeleri için hesaplanır.

### Tahminlerin Görselleştirilmesi
Kod, eğitim ve test kümelerinden tahmin edilen hisse fiyatlarını seçer ve bunları orijinal hisse fiyatı verileriyle birleştirir. Tahmin edilen değerler, modelin tahminlerini görselleştirmek için gerçek değerlerle birlikte çizdirilir.

### Sonuç
Bu kod, hisse fiyatı tahmini için LSTM kullanımını göstermektedir. Veriyi ön işler, giriş özelliklerini oluşturur, bir LSTM modeli oluşturur ve eğitir, modelin performansını değerlendirir ve tahminleri görselleştirir. RMSE değerleri, modelin gelecekteki hisse fiyatlarını tahmin etmedeki doğruluğunu gösterir.
