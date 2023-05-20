## English
##  Customer Churn Prediction
This repository contains code for predicting customer churn using a logistic regression model. The code performs various data preprocessing steps, exploratory data analysis, and trains a logistic regression model to predict customer churn.

### Purpose
The main purpose of this code is to predict customer churn, which refers to customers leaving a company's services or products. By analyzing customer data and training a predictive model, businesses can proactively identify customers who are likely to churn and take appropriate measures to retain them.

### Dataset
The code uses the "churn.csv" dataset, which contains information about customers and whether they churned or not. The dataset has 7043 rows and 21 columns, including features such as tenure, monthly charges, gender, internet service type, and more.

### Usage
To use this code, follow these steps:

1. Make sure you have the necessary dependencies installed, including numpy, pandas, sklearn, matplotlib, and seaborn.

2. Prepare your dataset in a CSV format and save it as "churn.csv" in the same directory as the code.

3. Run the code using a Python interpreter or an integrated development environment (IDE) of your choice.

4. The code performs the following steps:
	- Loads the dataset and displays its shape, column names, and summary statistics.
	- Analyzes the distribution of churned and retained customers.
	- Visualizes the count of churned customers based on gender and internet service type.
	- Conducts exploratory data analysis by plotting histograms for numeric features based on churn status.
	- Preprocesses the data by encoding categorical variables using label encoding and standardizes numeric features.
	- Splits the data into training and testing sets.
	- Trains a logistic regression model on the training data.
	- Predicts customer churn using the trained model on the testing data.
	- Prints the predictions and a classification report showing the performance metrics of the model.

### Results
The code outputs the predicted churn status for the testing data and provides a classification report, which includes metrics such as precision, recall, and F1-score. These metrics evaluate the performance of the logistic regression model in predicting customer churn.

Please note that the interpretation and application of the results may vary depending on the specific business context and dataset used.


## Türkçe
##  Müşteri Kaybı Tahmini
Bu depo, bir lojistik regresyon modeli kullanarak müşteri kaybını tahmin etmek için kod içermektedir. Kod, çeşitli veri ön işleme adımları, keşifsel veri analizi ve müşteri kaybını tahmin etmek için bir lojistik regresyon modeli eğitme işlemlerini gerçekleştirir.

### Amaç
Bu kodun temel amacı, müşteri kaybını tahmin etmektir. Müşteri kaybı, müşterilerin bir şirketin hizmetlerinden veya ürünlerinden ayrılması durumunu ifade eder. Müşteri verilerini analiz ederek ve bir tahmin modeli eğiterek, işletmeler, kaybetme olasılığı yüksek olan müşterileri önceden belirleyebilir ve onları elde tutmak için uygun önlemler alabilir.

### Veri Kümesi
Kod, "churn.csv" adlı veri kümesini kullanır. Bu veri kümesi, müşterilerle ilgili bilgileri ve müşterilerin kaybedilip kaybedilmediğini içerir. Veri kümesi, 7043 satır ve tenure, monthly charges, gender, internet service type gibi özellikler içeren 21 sütundan oluşmaktadır.

### Kullanım
Bu kodu kullanmak için aşağıdaki adımları izleyin:

1. numpy, pandas, sklearn, matplotlib ve seaborn gibi gerekli bağımlılıkların yüklü olduğundan emin olun.

2. Veri kümesini CSV formatında hazırlayın ve kod ile aynı dizinde "churn.csv" olarak kaydedin.

3. Kodu, tercih ettiğiniz bir Python yorumlayıcısı veya entegre geliştirme ortamında çalıştırın.

4. Kod aşağıdaki adımları gerçekleştirir:
	- Veri kümesini yükler ve şekli, sütun adları ve özet istatistiklerini görüntüler.
	- Kaybedilen ve elde tutulan müşterilerin dağılımını analiz eder.
	- Cinsiyet ve internet servis türüne göre kaybedilen müşterilerin sayısını görselleştirir.
	- Müşteri kaybı durumuna bağlı olarak sayısal özellikler için histogramlar çizerek keşifsel veri analizi yapar.
	- Kategorik değişkenleri etiket kodlama yöntemiyle kodlar ve sayısal özellikleri standartlaştırır.
	- Veriyi eğitim ve test kümelerine ayırır.
	- Eğitim verileri üzerinde bir lojistik regresyon modeli eğitir.
	- Eğitilen modeli kullanarak test verileri üzerinde müşteri kaybını tahmin eder.
	- Tahminleri ve modelin performans metriklerini gösteren bir sınıflandırma raporu yazdırır.

### Sonuçlar
Kod, test verileri için tahmin edilen müşteri kaybı durumunu ve hassasiyet, duyarlılık ve F1-skor gibi performans metriklerini içeren bir sınıflandırma raporu çıktısı verir. Bu metrikler, lojistik regresyon modelinin müşteri kaybını tahmin etmedeki performansını değerlendirir.

> *Lütfen unutmayın ki sonuçların yorumlanması ve uygulanması, özel iş bağlamı ve kullanılan veri kümesine bağlı olarak değişebilir.*
