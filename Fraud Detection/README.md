## English
## Credit Card Fraud Detection using K-means Clustering
This project focuses on detecting credit card fraud using the K-means clustering algorithm. Python is utilized along with the following libraries: numpy, sklearn, pandas, and matplotlib.

### Installation
To run the project, make sure you have the required libraries installed. You can install them using the following commands:

- pip install numpy
- pip install sklearn
- pip install pandas
- pip install matplotlib

### Dataset
- The credit card dataset used in this project is loaded from a CSV file named "creditcard.csv". 
- It contains features related to credit card transactions, including the target variable "Class" indicating whether the transaction is fraudulent or not.

### K-means Clustering
K-means clustering is applied to the dataset to identify patterns and separate fraudulent transactions from legitimate ones. The steps involved in the clustering process are as follows:

1. Loading the dataset into a pandas DataFrame.
2. Splitting the dataset into input features (X) and the target variable (y).
3. Scaling the input features using the scale() function from sklearn.preprocessing.
4. Applying Principal Component Analysis (PCA) to reduce the dimensionality of the data to 2 dimensions.
5. Splitting the data into training and testing sets using train_test_split() from sklearn.model_selection.
6. Creating a K-means clustering model with 2 clusters using KMeans() from sklearn.cluster.
7. Fitting the model to the training data.
8. Plotting the decision boundary and visualizing the clusters using matplotlib.
9. Predicting the labels for the testing data.
10. Evaluating the performance of the model by calculating accuracy and false negative rate.

### Results and Evaluation
The performance of the K-means clustering model is evaluated using various metrics. The following results are displayed:

- **Accuracy:** The percentage of correctly classified instances in the test data.
- **False negative rate (with respect to misclassifications):** The rate of falsely classifying legitimate transactions as fraudulent.
- **False negative rate (with respect to all the data):** The rate of falsely classifying any transaction as fraudulent.
- **False negatives, false positives, mispredictions:** The number of falsely classified instances.
- **Total test data points:** The total number of instances in the test data.

> *Please note that this project provides a basic implementation of fraud detection using K-means clustering and may not be suitable for production use without further refinement and feature engineering.*

## Türkçe
## K-means Kümeleme Algoritması Kullanarak Kredi Kartı Dolandırıcılığı Tespiti
Bu proje, K-means kümeleme algoritması kullanarak kredi kartı dolandırıcılığını tespit etmeye odaklanmaktadır. Python, numpy, sklearn, pandas ve matplotlib gibi kütüphaneler kullanılarak projenin geliştirilmesi sağlanmıştır.

### Kurulum
Projeyi çalıştırmak için gereken kütüphanelerin yüklü olduğundan emin olun. Aşağıdaki komutları kullanarak kütüphaneleri yükleyebilirsiniz:

- pip install numpy
- pip install sklearn
- pip install pandas
- pip install matplotlib

## #Veri Seti
- Bu projede kullanılan kredi kartı veri seti, "creditcard.csv" adlı bir CSV dosyasından yüklenir.
- Veri seti, kredi kartı işlemleri ile ilgili özellikler içermekte olup, işlemin dolandırıcılık olup olmadığını belirten "Class" hedef değişkenini içermektedir.

### K-means Kümeleme
K-means kümeleme, veri setindeki desenleri belirlemek ve dolandırıcı işlemleri gerçek işlemlerden ayırmak için kullanılmaktadır. Kümeleme sürecinde aşağıdaki adımlar izlenir:

1. Veri setinin bir pandas DataFrame'e yüklenmesi.
2. Veri setinin giriş özellikleri (X) ve hedef değişkeni (y) olarak bölünmesi.
3. Giriş özelliklerinin sklearn.preprocessing kütüphanesindeki scale() fonksiyonuyla ölçeklendirilmesi.
4. Temel Bileşen Analizi (PCA) kullanılarak verinin boyutunun 2'ye indirgenmesi.
5. Verinin eğitim ve test kümelerine sklearn.model_selection kütüphanesindeki train_test_split() fonksiyonuyla bölünmesi.
6. sklearn.cluster kütüphanesindeki KMeans() fonksiyonunu kullanarak 2 küme içeren bir K-means kümeleme modelinin oluşturulması.
7. Modelin eğitim verisine uygun hale getirilmesi.
8. Karar sınırlarının çizilmesi ve kümelere ilişkin görselleştirmenin matplotlib kullanılarak yapılması.
9. Test verisi için etiketlerin tahmin edilmesi.
10. Modelin performansının değerlendirilmesi için doğruluk ve yanlış negatif oranının hesaplanması.

### Sonuçlar ve Değerlendirme
K-means kümeleme modelinin performansı çeşitli metrikler kullanılarak değerlendirilir. Aşağıdaki sonuçlar görüntülenir:
- **Doğruluk:** Test verisinde doğru sınıflandırılan örneklerin yüzdesi.
- **Yanlış negatif oranı (yanlış sınıflandırmalara göre):** Gerçek işlemleri yanlışlıkla dolandırıcı olarak sınıflandırma oranı.
- **Yanlış negatif oranı (tüm verilere göre):** Herhangi bir işlemi yanlışlıkla dolandırıcı olarak sınıflandırma oranı.
- **Yanlış negatifler, yanlış pozitifler, yanlış sınıflandırmalar:** Yanlış sınıflandırılan örneklerin sayısı.
- **Toplam test veri noktaları:** Test verisindeki toplam örnek sayısı.

> *Lütfen bu proje, K-means kümeleme kullanarak dolandırıcılık tespiti için temel bir uygulama sağlamaktadır ve daha fazla iyileştirme ve özellik mühendisliği gerektirmeden doğrudan üretim kullanımı için uygun olmayabilir.*
