## English
## Sentiment Analysis with Logistic Regression

### Project Description
This project focuses on sentiment analysis using logistic regression. It aims to analyze the sentiment (positive or negative) of movie reviews from the IMDB dataset. The project involves preprocessing the data, feature extraction using bag-of-words and TF-IDF methods, label encoding, and training a logistic regression model to predict sentiment.

### Steps

1. Data Loading and Initial Analysis:
	- Load the IMDB dataset using the read_csv function from the pandas library.
	- Perform initial analysis such as checking the columns, detecting missing values, and getting descriptive statistics.

2. Data Preprocessing:
	- Import necessary libraries like seaborn, matplotlib.pyplot, nltk, and others.
	- Perform data cleaning steps including noise removal, stemming, and removing stopwords.
	- Use BeautifulSoup for text tokenization.

3. Bag-of-Words (BOW) Representation:
	- Create a CountVectorizer object for BOW representation.
	- Transform the training and test reviews into BOW features using the CountVectorizer.
	- Print the shape of the transformed data.

4. TF-IDF Representation:
	- Create a TfidfVectorizer object for TF-IDF representation.
	- Transform the training and test reviews into TF-IDF features using the TfidfVectorizer.
	- Print the shape of the transformed data.

5. Label Encoding:
	- Use LabelBinarizer to convert the sentiment labels into binary form.
	- Print the shape of the transformed sentiment data.

6. Model Training and Evaluation:
	- Split the sentiment data into training and test sets.
	- Initialize a logistic regression model with specified parameters.
	- Fit the logistic regression model on the BOW features and the sentiment training data.
	- Predict the sentiment labels for the test set using the trained model.
	- Calculate and print the accuracy score for the BOW representation.
	- Fit the logistic regression model on the TF-IDF features and the sentiment training data.
	- Predict the sentiment labels for the test set using the trained model.
	- Calculate and print the accuracy score for the TF-IDF representation.

> *Please note that the provided code example is not a complete README file and does not include detailed explanations for each step. It is recommended to provide additional information, such as the purpose of each step, data source, and expected output.*


## Türkçe
## Lojistik Regresyon ile Duygu Analizi


### Proje Açıklaması
Bu proje, lojistik regresyon kullanarak duygu analizi üzerinde odaklanmaktadır. IMDB veri setindeki film incelemelerinin duygusunu (olumlu veya olumsuz) analiz etmeyi amaçlamaktadır. Proje, veri ön işleme, kelime çantası (bag-of-words) ve TF-IDF yöntemleri kullanarak özellik çıkarımı, etiket kodlama ve duygu tahmini yapmak için lojistik regresyon modelinin eğitilmesini içermektedir.

### Adımlar

1. Veri Yükleme ve İlk Analiz:
	- Pandas kütüphanesinden read_csv fonksiyonunu kullanarak IMDB veri setini yükleyin.
	- Sütunları kontrol etme, eksik değerleri tespit etme ve tanımlayıcı istatistikler elde etme gibi ilk analizleri gerçekleştirin.

2. Veri Ön İşleme:
	- seaborn, matplotlib.pyplot, nltk ve diğer gerekli kütüphaneleri içe aktarın.
	- Gürültüyü kaldırma, kök çıkarma (stemming) ve stop kelimelerini çıkarma gibi veri temizleme adımlarını gerçekleştirin.
	- Metin belgelerini işaretleyici cümlelere ayırmak için BeautifulSoup'ı kullanın.

3. Kelime Çantası (Bag-of-Words) Temsili:
	- Kelime çantası temsili için bir CountVectorizer nesnesi oluşturun.
	- Eğitim ve test incelemelerini CountVectorizer kullanarak kelime çantası özelliklerine dönüştürün.
	- Dönüştürülen verinin şeklini yazdırın.

4. TF-IDF Temsili:
	- TF-IDF temsili için bir TfidfVectorizer nesnesi oluşturun.
	- Eğitim ve test incelemelerini TfidfVectorizer kullanarak TF-IDF özelliklerine dönüştürün.
	- Dönüştürülen verinin şeklini yazdırın.

5. Etiket Kodlama:
	- Duygu etiketlerini ikili formata dönüştürmek için LabelBinarizer kullanın.
	- Dönüştürülen duygu verisinin şeklini yazdırın.

6. Model Eğitimi ve Değerlendirme:
	- Duygu verisini eğitim ve test kümelerine ayırın.
	- Belirli parametrelerle bir lojistik regresyon modeli başlatın.
	- Lojistik regresyon modelini kelime çantası özellikleri ve duygu eğitim verisi üzerinde eğitin.
	- Eğitilmiş modeli kullanarak test kümeleri için duygu etiketlerini tahmin edin.
	- Kelime çantası temsili için doğruluk puanını hesaplayın ve yazdırın.
	- Lojistik regresyon modelini TF-IDF özellikleri ve duygu eğitim verisi üzerinde eğitin.
	- Eğitilmiş modeli kullanarak test kümeleri için duygu etiketlerini tahmin edin.
	- TF-IDF temsili için doğruluk puanını hesaplayın ve yazdırın.

> *Lütfen verilen kod örneği tam bir README dosyası değildir ve her adım için detaylı açıklamalar içermez. Veri kaynağı, her adımın amacı ve beklenen çıktı gibi ek bilgiler sağlamanız önerilir.*
