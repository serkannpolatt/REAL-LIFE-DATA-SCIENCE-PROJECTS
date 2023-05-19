## English
## IMDb Sentiment Analysis Model

Bu proje, IMDb veri kümesini kullanarak duygu analizi yapmak için bir makine öğrenimi modeli oluşturmayı amaçlamaktadır. Model, metin tabanlı film incelemelerini analiz ederek pozitif veya negatif duyguyu tahminlemektedir.

### Adımlar
1. Veri Hazırlama:
	- IMDB-Dataset.csv dosyası pd.read_csv fonksiyonu ile okunur.
	- İncelemelerde bulunan HTML etiketleri clean fonksiyonu ile kaldırılır.
	- Özel karakterler is_special fonksiyonu ile temizlenir.
	- Metinler küçük harflere dönüştürülür (to_lower fonksiyonu).
	- Stop kelimeleri (stopwords) çıkarılır (rem_stopwords fonksiyonu).
	- Köklerine indirgenmiş hali elde edilir (stem_txt fonksiyonu).

1. Özellik Çıkarımı:
	- Temizlenmiş incelemeleri sayısal özelliklere dönüştürmek için CountVectorizer kullanılır.

2. Veri Bölme:
	- Veri seti eğitim ve test setlerine ayrılır (train_test_split fonksiyonu).

3. Model Oluşturma:
	- Gaussian, Multinomial ve Bernoulli olmak üzere üç farklı Naive Bayes sınıflandırıcısı oluşturulur (GaussianNB, MultinomialNB, BernoulliNB).
	- Eğitim seti kullanılarak modeller eğitilir.

4. Model Değerlendirme:
	- Test seti üzerinde modelin doğruluğu (accuracy_score) değerlendirilir.

5. Model Kaydetme:
	- Eğitilen en iyi model (BernoulliNB) model1.pkl dosyasına pickle kullanılarak kaydedilir.

6. Tahminler:
	- Belirli bir inceleme için duyguyu tahminlemek için oluşturulan model kullanılır.


Bu projeyi takip ederek, IMDb veri kümesini kullanarak duygu analizi yapabilen bir model oluşturabilirsiniz. Detaylı adımlar ve kullanılan fonksiyonlar kod parçacığında bulunmaktadır.


## English
## IMDb Sentiment Analysis Model
This project aims to create a machine learning model for sentiment analysis using the IMDb dataset. The model analyzes text-based movie reviews to predict whether the sentiment is positive or negative.

### Steps
1. Data Preparation:
	- The IMDB-Dataset.csv file is read using the pd.read_csv function.
	- HTML tags in the reviews are removed using the clean function.
	- Special characters are cleaned using the is_special function.
	- Texts are converted to lowercase (to_lower function).
	- Stop words are removed (rem_stopwords function).
	- Texts are stemmed (stem_txt function) to reduce them to their root form.

2. Feature Extraction:
	- Cleaned reviews are transformed into numerical features using CountVectorizer.

3. Data Split:
	- The dataset is split into training and testing sets using the train_test_split function.

4. Model Creation:
	- Three different Naive Bayes classifiers, Gaussian, Multinomial, and Bernoulli, are created (GaussianNB, MultinomialNB, BernoulliNB).
	- The models are trained using the training set.

5. Model Evaluation:
	- The accuracy of the models is evaluated on the test set (accuracy_score).

6. Model Saving:
	- The best-trained model (BernoulliNB) is saved to the model1.pkl file using pickle.

7. Predictions:
	- The created model is used to predict the sentiment for a specific review.

By following this project, you can create a model capable of sentiment analysis using the IMDb dataset. Detailed steps and the functions used can be found in the code snippet.




