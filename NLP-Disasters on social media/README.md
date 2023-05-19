## English
## Project Title: Social Media Text Classification
This project aims to perform text classification on social media data to determine the relevance of the text to a specific topic or event. The project involves several steps, including data preprocessing, feature extraction, model training, and evaluation.

### Project Steps:

1. Data Preprocessing:
	- The initial step is to read the input data file (socialmedia_relevant_cols.csv) and clean it by removing any unwanted characters or symbols. The sanitized data is then saved to a new file (socialmedia_relevant_cols_clean.csv).

2. Standardize Text:
	- The standardize_text function is used to further clean the text by removing URLs, mentions, and special characters. The text is also converted to lowercase for consistency.

3. Tokenization:
	- The text is tokenized using the RegexpTokenizer from the NLTK library. The resulting tokens are stored in a new column called "tokens" in the DataFrame.

4. Vocabulary Analysis:
	- The vocabulary analysis is performed to determine the total number of words and the vocabulary size in the dataset. Additionally, the maximum sentence length is calculated.

5. Sentence Length Histogram:
	- A histogram is plotted to visualize the distribution of sentence lengths in the dataset.

6. Train-Test Split:
	- The dataset is split into training and testing sets using a ratio of 80:20. The X_train and X_test variables contain the text data, while y_train and y_test contain the corresponding class labels.

7. Feature Extraction - Bag of Words:
	- The CountVectorizer is used to convert the text data into a matrix of token counts. The cv function performs this feature extraction on the training data.

8. Latent Semantic Analysis (LSA):
	- LSA is applied to the bag of words representation to reduce the dimensionality of the data to 2D. The resulting representation is visualized using a scatter plot.

9. Model Training - Logistic Regression:
	- Logistic Regression is used as the classification model. The LogisticRegression class from scikit-learn is employed to train the model on the bag of words features.

10. Model Evaluation:
	- Various evaluation metrics such as accuracy, precision, recall, and F1 score are calculated to assess the performance of the trained model.

11. Confusion Matrix:
	- A confusion matrix is plotted to visualize the performance of the model in predicting the class labels.

12. Important Features:
	- The most important features (words) for each class are identified using the trained Logistic Regression model and the CountVectorizer. The top and bottom words for relevance are plotted to provide insights into the model's decision-making process.

13. Feature Extraction - TF-IDF:
	- The TF-IDF (Term Frequency-Inverse Document Frequency) representation is used as an alternative feature extraction method. The tfidf function converts the text data into TF-IDF vectors.

14. Model Training with TF-IDF:
	- Logistic Regression model is trained using the TF-IDF features.

15. TF-IDF vs. Bag of Words Comparison:
	- The performance of the TF-IDF-based model is compared to the Bag of Words-based model using evaluation metrics and confusion matrices.

16. Text Generation (Optional):
	- This part of the code generates random reviews based on a trained LSTM model. It uses a pre-trained model to predict the next character in the sequence and generates a new text based on the predicted characters.

> *Please note that the code provided above is for reference and demonstration purposes. Make sure to adapt it to your specific needs and dataset.*


## Türkçe
## Sosyal Medya Metin Sınıflandırması
Bu proje, sosyal medya verilerindeki metinleri belirli bir konu veya olayla ilgili olup olmadığını belirlemek için metin sınıflandırması yapmayı amaçlamaktadır. Proje, veri ön işleme, özellik çıkarımı, model eğitimi ve değerlendirme adımlarını içermektedir.

### Proje Adımları:
1. Veri Ön İşleme:
	- İlk adım, giriş veri dosyasını (socialmedia_relevant_cols.csv) okuyarak istenmeyen karakterleri veya sembolleri temizlemektir. Elde edilen temiz veriler yeni bir dosyaya (socialmedia_relevant_cols_clean.csv) kaydedilir.

2. Metinleri Standartlaştırma:
	- Metinleri daha da temizlemek için standartlaştır_text fonksiyonu kullanılır. Bu fonksiyon, URL'leri, bahsetmeleri ve özel karakterleri kaldırır. Ayrıca metinleri tutarlılık için küçük harflere dönüştürür.

3. Kelime Parçalama (Tokenization):
	- Metinler NLTK kütüphanesindeki RegexpTokenizer kullanılarak kelimelere ayrıştırılır. Elde edilen kelimeler "tokens" adında yeni bir sütunda DataFrame içinde saklanır.

4. Kelime Dağarcığı Analizi:
	- Veri setindeki toplam kelime sayısı ve kelime dağarcığı boyutunu belirlemek için kelime dağarcığı analizi yapılır. Ayrıca, maksimum cümle uzunluğu hesaplanır.

5. Cümle Uzunluğu Histogramı:
- 	Veri setindeki cümle uzunluklarının dağılımını görselleştirmek için bir histogram çizilir.

6. Eğitim ve Test Veri Setlerinin Bölünmesi:
	- Veri seti, %80-%20 oranında eğitim ve test veri setlerine bölünür. X_train ve X_test değişkenleri metin verilerini, y_train ve y_test değişkenleri ise ilgili sınıf etiketlerini içerir.

7. Özellik Çıkarımı - Kelime Torbası (Bag of Words):
	- Metin verileri, CountVectorizer kullanılarak kelime sayısı matrisine dönüştürülür. cv fonksiyonu bu özellik çıkarımını eğitim veri setine uygular.

8. Latent Semantic Analysis (LSA):
	- LSA, kelime torbası temsilini 2 boyutlu veriye indirgemek için uygulanır. Elde edilen temsil, bir scatter plot ile görselleştirilir.

9. Model Eğitimi - Lojistik Regresyon:
	- Lojistik Regresyon, sınıflandırma modeli olarak kullanılır. Bag of Words özellikleri üzerinde modeli eğitmek için scikit-learn kütüphanesindeki LogisticRegression sınıfı kullanılır.

10. Model Değerlendirme:
	- Eğitilen modelin performansını değerlendirmek için doğruluk, hassasiyet, geri çağırma ve F1 skoru gibi çeşitli değerlendirme metrikleri hesaplanır.

11. Karma Matrisi:
- Modelin sınıf etiketlerini tahmin etmedeki performansını görselleştirmek için bir karma matrisi çizilir.

12. Önemli Özellikler:
	- Eğitilmiş Lojistik Regresyon modeli ve CountVectorizer kullanılarak her sınıf için en önemli özellikler (kelimeler) belirlenir. İlgiliğe göre en üstte ve en altta yer alan kelimeler, modelin karar verme sürecine ışık tutmak amacıyla görselleştirilir.

13. Özellik Çıkarımı - TF-IDF:
	- TF-IDF (Kelime Sıklığı-Ters Belge Frekansı) temsili, alternatif bir özellik çıkarım yöntemi olarak kullanılır. tfidf fonksiyonu metin verilerini TF-IDF vektörlerine dönüştürür.

14. TF-IDF ile Model Eğitimi:
	- TF-IDF özellikleri kullanılarak Lojistik Regresyon modeli eğitilir.

15. TF-IDF ve Kelime Torbası Karşılaştırması:
	- TF-IDF tabanlı modelin performansı, Kelime Torbası tabanlı modelle karşılaştırılır. Değerlendirme metrikleri ve karma matrisleri kullanarak karşılaştırma yapılır.

16. Metin Üretimi (İsteğe Bağlı):
	- Bu bölüm, eğitilmiş bir LSTM modeline dayanarak rastgele incelemeler üretir. Önceden eğitilmiş bir model kullanarak sıradaki karakteri tahmin eder ve tahmin edilen karakterlere dayanarak yeni bir metin üretir.


> *Lütfen yukarıdaki kod örneği, referans ve gösterim amaçlıdır. Kendi ihtiyaçlarınıza ve veri setinize uyacak şekilde uyarlamayı unutmayın.*



#### download pretrained google word vectors
http://mccormickml.com/2016/04/12/googles-pretrained-word2vec-model-in-python/
