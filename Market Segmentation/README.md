## English
## Customer Data Clustering and Prediction

This README provides an overview of the code you've shared, which includes data preprocessing, clustering using K-Means, and prediction using a Decision Tree model. The code also includes a Streamlit application for user input and prediction visualization.

### Data Preprocessing

1. Load the dataset from a CSV file called "Customer Data.csv" using pd.read_csv.
2. Display basic information about the dataset:
	- Shape of the DataFrame.
	- Information about the columns and their data types.
	- Summary statistics using df.describe().
	- Count of missing values using df.isnull().sum().

3. Fill missing values in the "MINIMUM_PAYMENTS" and "CREDIT_LIMIT" columns with their respective means.
4. Check for duplicate rows in the dataset using df.duplicated().sum().
5. Drop the "CUST_ID" column as it is not used in the analysis.
6. Visualize data distributions using KDE plots for numerical columns.

### Principal Component Analysis (PCA)

1. Scale the data using StandardScaler.
2. Apply PCA with two components and create a new DataFrame pca_df to visualize the data in 2D.

### K-Means Clustering

1. Perform K-Means clustering with a range of values for K (number of clusters) to determine the optimal number of clusters using the "Elbow Method."
2. Create a K-Means model with the selected number of clusters (4 in this case).
3. Visualize the clusters in 2D using a scatterplot.

### Cluster Analysis

1. Find the cluster centers and inverse transform them to get the original scale values.
2. Create a new column "Cluster" in the DataFrame to store cluster labels.
3. Separate the data into four DataFrames, one for each cluster.

### Cluster Visualization

1. Visualize the distribution of clusters using a countplot.
2. Create histograms for each feature within each cluster.

### Saving Models and Data

1. Save the K-Means model using joblib.dump.
2. Save the clustered customer data to a CSV file named "Clustered_Customer_Data.csv."

### Machine Learning - Decision Tree

1. Split the clustered data into training and testing sets.
2. Build a Decision Tree classification model using the "entropy" criterion.
3. Make predictions on the test set.
4. Evaluate the model's performance using a confusion matrix and classification report.
5. Save the Decision Tree model using pickle.

### Streamlit Application

1. Load the saved Decision Tree model and the clustered customer data.
2. Create a Streamlit app for user input and prediction.
3. Collect user input for various customer features.
4. Display the predicted cluster for the user's input data.
5. Visualize histograms of each feature within the predicted cluster using plt.subplots() and st.pyplot().


## Türkçe
## Müşteri Verilerini Kümeleme ve Tahmin

Bu README, veri ön işlemeyi, K-Means kullanarak kümelemeyi ve Karar Ağacı modelini kullanarak tahmin yapmayı içeren, paylaştığınız koda ilişkin bir genel bakış sağlar. Kod ayrıca kullanıcı girişi ve tahmin görselleştirmesi için bir Streamlit uygulaması içerir.

### Veri Ön İşleme

1. pd.read_csv'yi kullanarak "Customer Data.csv" adlı CSV dosyasından veri kümesini yükleyin.
2. Veri kümesiyle ilgili temel bilgileri görüntüleyin:
- DataFrame'in şekli.
- Sütunlar ve veri türleri hakkında bilgi.
- df.describe() kullanılarak özet istatistikler.
- df.isnull().sum() kullanılarak eksik değerlerin sayısı.

3. "MINIMUM_PAYMENTS" ve "CREDIT_LIMIT" sütunlarındaki eksik değerleri ilgili araçlarıyla doldurun.
4. df.duplicated().sum() işlevini kullanarak veri kümesindeki yinelenen satırları kontrol edin.
5. Analizde kullanılmadığından "CUST_ID" sütununu bırakın.
6. Sayısal sütunlar için KDE grafiklerini kullanarak veri dağılımlarını görselleştirin.

### Temel Bileşen Analizi (PCA)

1. StandardScaler'ı kullanarak verileri ölçeklendirin.
2. PCA'yı iki bileşenle uygulayın ve verileri 2B olarak görselleştirmek için yeni bir DataFrame pca_df oluşturun.

### K-Kümeleme Anlamına Gelir

1. "Dirsek Yöntemi"ni kullanarak optimum küme sayısını belirlemek için K (küme sayısı) için bir dizi değerle K-Ortalamalar kümelemesi gerçekleştirin.
2. Seçilen sayıda kümeyle (bu durumda 4) bir K-Means modeli oluşturun.
3. Dağılım grafiği kullanarak kümeleri 2 boyutlu olarak görselleştirin.

### Küme analizi

1. Küme merkezlerini bulun ve orijinal ölçek değerlerini elde etmek için bunları ters dönüştürün.
2. Küme etiketlerini depolamak için DataFrame'de yeni bir "Küme" sütunu oluşturun.
3. Verileri, her küme için bir tane olmak üzere dört DataFrame'e ayırın.

### Küme Görselleştirme

1. Bir sayım grafiği kullanarak kümelerin dağılımını görselleştirin.
2. Her kümedeki her özellik için histogramlar oluşturun.

### Modelleri ve Verileri Kaydetme

1. Joblib.dump'ı kullanarak K-Means modelini kaydedin.
2. Kümelenmiş müşteri verilerini "Clustered_Customer_Data.csv" adlı bir CSV dosyasına kaydedin.

### Makine Öğrenimi - Karar Ağacı

1. Kümelenmiş verileri eğitim ve test setlerine bölün.
2. "Entropi" kriterini kullanarak bir Karar Ağacı sınıflandırma modeli oluşturun.
3. Test seti üzerinde tahminlerde bulunun.
4. Karışıklık matrisi ve sınıflandırma raporunu kullanarak modelin performansını değerlendirin.
5. Karar Ağacı modelini turşu kullanarak kaydedin.

### Kolaylaştırılmış Uygulama

1. Kaydedilen Karar Ağacı modelini ve kümelenmiş müşteri verilerini yükleyin.
2. Kullanıcı girişi ve tahmini için bir Streamlit uygulaması oluşturun.
3. Çeşitli müşteri özelliklerine ilişkin kullanıcı girdilerini toplayın.
4. Kullanıcının giriş verileri için tahmin edilen kümeyi görüntüleyin.
5. Plt.subplots() ve st.pyplot()'u kullanarak tahmin edilen küme içindeki her bir özelliğin histogramlarını görselleştirin.