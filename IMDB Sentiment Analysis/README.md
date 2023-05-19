## English 
## IMDB Sentiment Analysis
This README provides an overview of the project, its purpose, and the steps involved. It does not contain any code but describes the project in detail.

### Project Description
The project aims to analyze sentiment analysis on movie reviews using machine learning algorithms. The dataset used for analysis is "IMDB Dataset.csv," which contains movie reviews along with their corresponding sentiments (positive or negative). The project involves preprocessing the data, training various machine learning models, and evaluating their performance.

### Steps Involved
1. Dataset Examination:
	- Analyze the shape of the dataset (number of rows and columns).
	- Check the data types of each column.
	- Perform missing values analysis and display the results.
	- Display the first few rows of the dataset.

2.  Exploratory Data Analysis (EDA):

	- Visualize the distribution of positive and negative sentiments using a pie chart and a count plot.

3. Data Preprocessing:

	- Remove HTML tags from the review sentences using the BeautifulSoup module.
	- Clean the reviews by removing punctuation and numbers using regular expressions (regex).
	- Convert the reviews to lowercase and split them into individual words.
	- Remove stopwords from the reviews using the nltk library.

4. Data Preparation:

	- Split the preprocessed reviews into independent and dependent variables.
	- Split the data into training and testing sets using the train_test_split function.
	- Convert the training data into a feature vector matrix using the CountVectorizer.
	- Convert the training data and labels to arrays.

5. Model Training and Evaluation:

	- Initialize and train multiple machine learning models, including Logistic Regression, Random Forest Classifier, and Decision Tree Classifier.
	- Convert the test data into a vector matrix using the CountVectorizer.
	- Make predictions on the test data using each trained model.
	- Evaluate the accuracy and F1 score of each model.


> *Note: The code snippets provided in the original message are not included in this README, as per the request to exclude code from the README file.

## Türkçe 

##  IMDB Duygu Analizi
Bu README dosyası, projenin genel bir açıklamasını, amacını ve içerdiği adımları sunmaktadır. Kod içermemekte, ancak projeyi detaylı bir şekilde açıklamaktadır.

### Proje Açıklaması
Bu proje, film incelemeleri üzerinde duygu analizi yapmayı amaçlamaktadır. Analiz için kullanılan veri seti "IMDB Dataset.csv" adını taşımaktadır ve film incelemelerini ile bunların karşılık gelen duygularını (olumlu veya olumsuz) içermektedir. Proje, verinin önişleme işlemlerini gerçekleştirmeyi, çeşitli makine öğrenimi modellerini eğitmeyi ve performanslarını değerlendirmeyi içermektedir.

### İşlem Adımları

1. Veri Seti İncelemesi:

	- Veri setinin şeklini (satır ve sütun sayısı) analiz etmek.
	- Her bir sütunun veri tiplerini kontrol etmek.
	- Eksik değer analizi yapmak ve sonuçları görüntülemek.
	- Veri setinin ilk birkaç satırını görüntülemek.

2. Keşifsel Veri Analizi (EDA):

	- Olumlu ve olumsuz duyguların dağılımını pasta grafik ve sütun grafiği ile görselleştirmek.

3. Veri Önişleme:

	- Inceleme cümlelerinden HTML etiketlerini kaldırmak için BeautifulSoup modülünü kullanmak.
	- Noktalama işaretlerini ve sayıları düzenli ifadeler (regex) kullanarak temizlemek.
	- İncelemeleri küçük harfe dönüştürmek ve kelimelere ayırmak.
	- Stop kelimelerini nltk kütüphanesini kullanarak kaldırmak.

4. Veri Hazırlığı:

	- Önişlenmiş incelemeleri bağımsız ve bağımlı değişkenlere ayırmak.
	- Veriyi eğitim ve test kümelerine train_test_split fonksiyonunu kullanarak bölmek.
	- Eğitim verisini CountVectorizer kullanarak bir özellik vektör matrisine dönüştürmek.
	- Eğitim verisini ve etiketleri dizilere dönüştürmek.

5. Model Eğitimi ve Değerlendirmesi:

	- Lojistik Regresyon, Rastgele Orman Sınıflandırıcısı ve Karar Ağacı Sınıflandırıcısı dahil olmak üzere çeşitli makine öğrenimi modellerini başlatmak ve eğitmek.
	- Test verisini CountVectorizer kullanarak bir vektör matrisine dönüştürmek.
	- Eğitilmiş her modelle test verisi üzerinde tahminler yapmak.
	- Her modelin doğruluk ve F1 skorunu değerlendirmek.

> *Not: Orijinal mesajda verilen kod örnekleri bu README dosyasına dahil edilmemiştir, README dosyasında kod bulunmaması istendiği için.

> *Projenin uygulanma detayları ve tam işlevselliği için lütfen gerçek kodlara başvurun.**



> Please refer to the actual code for the implementation details and complete functionality of the project.*
