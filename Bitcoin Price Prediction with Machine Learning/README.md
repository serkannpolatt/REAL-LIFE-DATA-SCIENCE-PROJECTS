## English
## Bitcoin Price Prediction
This provides information about a program that predicts the future price of Bitcoin using the Support Vector Machine (SVM) algorithm. The program utilizes historical Bitcoin price data to train the SVM model and then makes predictions for the next 30 days.

### **Program Overview**
The program follows the following steps to predict Bitcoin prices:

- **Data Loading:** The program loads the Bitcoin price data from a CSV file.

- **Data Preprocessing:** The program removes the "Date" column from the dataset as it is not required for prediction.

- **Data Splitting:** The program splits the dataset into independent variables (x) and the target variable (y), which is the Bitcoin price to be predicted.

- **Data Preparation:** The program removes the last 30 rows from the independent variable dataset (x) as they represent the target variable values that we want to predict.

- **Model Training:** The program uses the SVM algorithm with a radial basis function (RBF) kernel to train the model on the training dataset (xtrain and ytrain).

- **Model Evaluation:** The program calculates the accuracy of the trained model using the testing dataset (xtest and ytest).

- **Price Prediction:** The program makes predictions for the next 30 days by using the trained SVM model and the prepared dataset of the last 30 days (predictionDays_array).

- **Results Display:** The program displays the predicted Bitcoin prices for the next 30 days and also shows the actual prices for the last 30 days.

### **Usage**
- Prepare your Bitcoin price data in a CSV file format.

- Update the program to load your specific CSV file by modifying the filename in the df = pd.read_csv("bitcoin.csv") line.

- Run the program and observe the predicted Bitcoin prices for the next 30 days as well as the actual prices for the last 30 days.

> *Note: The accuracy of the predictions may vary depending on the historical data and the chosen algorithm.*


## Türkçe
## Bitcoin Fiyat Tahmini
Bu, Bitcoin'in gelecekteki fiyatını tahmin eden bir program hakkında bilgi sağlar. Program, tarihsel Bitcoin fiyat verilerini kullanarak Destek Vektör Makinesi (SVM) algoritmasını eğitir ve ardından önümüzdeki 30 gün için tahminler yapar.

### **Program Genel Bakışı**
Program, Bitcoin fiyatlarını tahmin etmek için aşağıdaki adımları izler:

- **Veri Yükleme:** Program, CSV dosyasından Bitcoin fiyat verilerini yükler.

- **Veri Ön İşleme:** Program, tahmin için gerekli olmadığından veri kümesinden "Tarih" sütununu kaldırır.

- **Veri Ayırma:** Program, bağımsız değişkenleri (x) ve tahmin edilecek Bitcoin fiyatını temsil eden hedef değişkeni (y) veri kümesine böler.

- **Veri Hazırlama:** Program, hedef değişken değerlerini tahmin etmek istediğimiz için bağımsız değişken veri kümesinden (x) son 30 satırı kaldırır.

- **Model Eğitimi:** Program, eğitim veri kümesi (xtrain ve ytrain) üzerinde SVM algoritmasını kullanarak Radyal Tabanlı Fonksiyon (RBF) çekirdeği ile modeli eğitir.

- **Model Değerlendirmesi:** Program, test veri kümesi (xtest ve ytest) kullanılarak eğitilen modelin doğruluğunu hesaplar.

- **Fiyat Tahmini:** Program, eğitilmiş SVM modelini ve son 30 günlük hazırlanan veri kümesini (predictionDays_array) kullanarak önümüzdeki 30 gün için tahminler yapar.

- **Sonuçları Görüntüleme:** Program, önümüzdeki 30 gün için tahmin edilen Bitcoin fiyatlarını ve aynı zamanda son 30 gün için gerçek fiyatları görüntüler.

### Kullanım
- Bitcoin fiyat verilerinizi bir CSV dosya formatında hazırlayın.

- Programı, kendi belirli CSV dosyanızı yüklemek için df = pd.read_csv("bitcoin.csv") satırındaki dosya adını değiştirerek güncelleyin.

- Programı çalıştırın ve önümüzdeki 30 gün için tahmin edilen Bitcoin fiyatlarını ve aynı zamanda son 30 gün için gerçek fiyatları gözlemleyin.

> Not: Tahminlerin doğruluğu, tarihsel verilere ve seçilen algoritmaya bağlı olarak değişebilir.**
