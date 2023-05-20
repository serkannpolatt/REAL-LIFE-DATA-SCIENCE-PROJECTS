## English
## Linear Regression for Startups' Profit Prediction
This repository contains code for performing linear regression to predict the profit of startups. The code utilizes libraries such as NumPy, Pandas, Matplotlib, and Seaborn for data analysis and visualization purposes.

### Purpose
The main purpose of this code is to predict the profit of startups based on their R&D Spend, Administration, and Marketing Spend. By training a linear regression model on historical data, the code aims to provide insights into the factors that influence startup profitability.

### Dataset
The code uses the "Startups.csv" dataset, which contains information about different startups, including their R&D Spend, Administration costs, Marketing Spend, and Profit. The dataset allows for understanding the relationship between these variables and the resulting profit.

### Usage
To use this code, follow these steps:

1. Ensure that the necessary dependencies, including NumPy, Pandas, Matplotlib, and Seaborn, are installed.

2. Prepare the dataset in CSV format and save it as "Startups.csv" in the same directory as the code.

3. Run the code using a Python interpreter or your preferred integrated development environment.

4. The code performs the following steps:
	- Loads the dataset and displays the first few rows for initial inspection.
	- Provides summary statistics of the dataset.
	- Generates a heatmap to visualize the correlation between different variables.
	- Prepares the input features (R&D Spend, Administration, Marketing Spend) and the target variable (Profit).
	- Converts the input features and target variable into NumPy arrays for further processing.
	- Splits the data into training and testing sets using the train_test_split function from scikit-learn.
	- Imports the LinearRegression class from scikit-learn and trains a linear regression model on the training data.
	- Predicts the profit for the test data using the trained model.
	- Creates a new DataFrame to display the predicted profit values.

### Results
The code outputs the predicted profit values for the test data. These predicted values can be used to evaluate the performance of the linear regression model in estimating startup profitability based on the given input features.

> *Please note that the interpretation and application of the results may vary depending on the specific business context and dataset used.*


## Türkçe 
## Startups' Profit Tahmini için Doğrusal Regresyon
Bu depo, başlangıç şirketlerinin karını tahmin etmek için doğrusal regresyon gerçekleştiren kodları içermektedir. Kod, veri analizi ve görselleştirme amaçları için NumPy, Pandas, Matplotlib ve Seaborn gibi kütüphanelerden yararlanır.

### Amaç
Bu kodun temel amacı, başlangıç şirketlerinin karını Ar-Ge Harcamaları, Yönetim Harcamaları ve Pazarlama Harcamalarına dayanarak tahmin etmektir. Tarihsel veriler üzerinde bir doğrusal regresyon modeli eğiterek, kod giriş özelliklerinin başlangıç şirketlerinin karlılığını etkileyen faktörler hakkında bilgi sağlamayı amaçlar.

### Veri Kümesi
Kod, "Startups.csv" adlı veri kümesini kullanır. Bu veri kümesi, farklı başlangıç şirketleri hakkında bilgiler içerir ve Ar-Ge Harcamaları, Yönetim Harcamaları, Pazarlama Harcamaları ve Kar gibi değişkenleri içerir. Bu veri kümesi, bu değişkenler ile elde edilen kar arasındaki ilişkiyi anlamamıza olanak sağlar.

### Kullanım
Bu kodu kullanmak için aşağıdaki adımları izleyin:

1. NumPy, Pandas, Matplotlib ve Seaborn gibi gerekli bağımlılıkların yüklendiğinden emin olun.

2. Veri kümesini CSV formatında hazırlayın ve kod ile aynı dizinde "Startups.csv" olarak kaydedin.

3. Kodu bir Python yorumlayıcısı veya tercih ettiğiniz bir entegre geliştirme ortamında çalıştırın.

4. Kod aşağıdaki adımları gerçekleştirir:
	- Veri kümesini yükler ve ilk birkaç satırını başlangıç incelemesi için gösterir.
	- Veri kümesinin özet istatistiklerini sağlar.
	- Farklı değişkenler arasındaki ilişkiyi görselleştirmek için bir ısı haritası oluşturur.
	- Giriş özelliklerini (Ar-Ge Harcamaları, Yönetim Harcamaları, Pazarlama Harcamaları) ve hedef değişkeni (Kar) hazırlar.
	- Giriş özelliklerini ve hedef değişkenini ileri işleme için NumPy dizilerine dönüştürür.
	- Veriyi scikit-learn kütüphanesindeki train_test_split fonksiyonunu kullanarak eğitim ve test setlerine ayırır.
	- scikit-learn kütüphanesinden LinearRegression sınıfını içe aktarır ve eğitim verisinde doğrusal regresyon modelini eğitir.
	- Test verisi için kar tahmini yapar.
	- Tahmin edilen kar değerlerini göstermek için yeni bir DataFrame oluşturur.

### Sonuçlar
Kod, test verisi için tahmin edilen kar değerlerini çıktı olarak verir. Bu tahmin edilen değerler, verilen giriş özellikleri temelinde doğrusal regresyon modelinin başlangıç şirketlerinin karlılığını tahmin etme performansını değerlendirmek için kullanılabilir.

> *Lütfen unutmayın ki sonuçların yorumlanması ve uygulanması, özel iş bağlamı ve kullanılan veri kümesine bağlı olarak değişebilir.*
