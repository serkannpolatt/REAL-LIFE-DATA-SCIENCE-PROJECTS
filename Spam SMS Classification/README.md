## English
## Spam SMS Classification
This project focuses on classifying SMS messages as either spam or non-spam (ham) using machine learning techniques. The purpose of this project is to build and evaluate different models to accurately predict whether a given SMS message is spam or not.

### Dataset
The dataset used in this project is the "Spam SMS Collection" dataset, which contains SMS messages labeled as spam or ham. The dataset is loaded using pandas and consists of two columns: "label" (spam or ham) and "message" (SMS text).

### Data Exploration
To gain insights into the dataset, the following steps are performed:

- A count plot is created to visualize the distribution of spam and ham messages, highlighting the imbalanced nature of the dataset.
- To address the class imbalance, oversampling is applied to balance the dataset by replicating the spam messages.
- Another count plot is created to visualize the distribution of spam and ham messages in the balanced dataset.
- The word count distribution is analyzed for both spam and ham messages using histograms.

### Feature Engineering
Several features are created to improve the classification models:

- **"word_count":** The number of words in each SMS message is calculated and added as a feature.
- **"contains_currency_symbol":** A binary feature indicating whether a message contains a currency symbol (e.g., €, $, ¥, £, ₹).
- **"contains_number":** A binary feature indicating whether a message contains numerical digits.

### Text Preprocessing
The SMS messages are preprocessed to clean the text and prepare it for modeling. The following steps are performed for each message:

- Removal of special characters and punctuation, keeping only alphabetic characters.
- Conversion of the text to lowercase.
- Tokenization of the text into individual words.
- Removal of stop words (common words like "the," "and," etc.) from the text.
- Lemmatization of the remaining words to reduce them to their base form.

### Feature Extraction
The Bag of Words model is used to convert the preprocessed text data into numerical vectors. The TfidfVectorizer from scikit-learn is employed to transform the corpus of SMS messages into a matrix of TF-IDF features. The maximum number of features is set to 500.

### Model Building and Evaluation
Three classification models are trained and evaluated on the dataset:

1. Multinomial Naive Bayes (MNB)
2. Decision Tree
3. Random Forest

For each model, the following steps are performed:

- The dataset is split into training and testing sets.
- The model is fitted on the training set.
- Cross-validation is performed to evaluate the model's performance using F1-score as the evaluation metric.
- The classification report and confusion matrix are generated to assess the model's performance on the testing set.

Additionally, a VotingClassifier is created, combining the Decision Tree and MNB models.

### Prediction
A function named "predict_spam" is provided to classify a new SMS message as spam or ham. The function takes a sample message as input and returns the predicted label using the trained Random Forest model.

### Conclusion
The project demonstrates the process of building and evaluating machine learning models for spam SMS classification. By using text preprocessing, feature engineering, and a Bag of Words representation, accurate predictions can be made to identify spam messages. The Random Forest model achieved the highest F1-score, making it the preferred model for spam SMS classification in this project.

## Türkçe
## Spam SMS Sınıflandırma
Bu proje, SMS mesajlarını spam veya spam olmayan (ham) olarak sınıflandırmaya yönelik makine öğrenimi tekniklerini kullanmaktadır. Bu proje, verilen bir SMS mesajının spam olup olmadığını doğru bir şekilde tahmin etmek için farklı modeller oluşturmayı ve değerlendirmeyi amaçlamaktadır.

### Veri Seti
Bu projede kullanılan veri seti "Spam SMS Collection" veri setidir ve spam veya ham olarak etiketlenmiş SMS mesajlarını içermektedir. Veri seti pandas kullanılarak yüklenir ve "label" (spam veya ham) ve "message" (SMS metni) olmak üzere iki sütundan oluşur.

### Veri Keşfi
Veri seti hakkında bilgi edinmek için aşağıdaki adımlar uygulanır:

- Spam ve ham mesajların dağılımını görselleştirmek için bir sayım grafiği oluşturulur ve veri setinin dengesiz yapısı vurgulanır.
- Sınıf dengesizliğine çözüm olarak, spam mesajları çoğaltarak veri setini dengelemek için oversampling uygulanır.
- Dengelenmiş veri setinde spam ve ham mesajların dağılımını görselleştirmek için başka bir sayım grafiği oluşturulur.
- Spam ve ham mesajların kelime sayısı dağılımı histogramlar kullanılarak analiz edilir.

### Özellik Mühendisliği
Sınıflandırma modellerini iyileştirmek için çeşitli özellikler oluşturulur:

- **"word_count":** Her SMS mesajındaki kelime sayısı hesaplanır ve bir özellik olarak eklenir.
- **"contains_currency_symbol":** Bir mesajın para birimi simgesi içerip içermediğini gösteren ikili bir özellik (örneğin, €, $, ¥, £, ₹).
- **"contains_number":** Bir mesajın sayısal rakamlar içerip içermediğini gösteren ikili bir özellik.

### Metin Önişleme
SMS mesajları metinleri temizlemek ve modele hazırlamak için önişleme işlemleri gerçekleştirilir. Her mesaj için aşağıdaki adımlar uygulanır:

- Özel karakterlerin ve noktalama işaretlerinin kaldırılması, sadece alfabetik karakterlerin tutulması.
- Metnin küçük harflere dönüştürülmesi.
- Metnin kelimelere ayrılması (tokenization).
- Metinden yaygın kelimelerin (örneğin, "the", "and" gibi) çıkarılması.
- Kalan kelimelerin köklerine indirgenmesi (lemmatization).

### Özellik Çıkarımı
Önişlenmiş metin verilerinin sayısal vektörlere dönüştürülmesi için Çanta Kelime Modeli (Bag of Words) kullanılır. Scikit-learn'den TfidfVectorizer, SMS mesajlarının bir TF-IDF özellikleri matrisine dönüştürülmesi için kullanılır. Maksimum özellik sayısı 500 olarak ayarlanmıştır.

### Model Oluşturma ve Değerlendirme
Veri seti üzerinde üç sınıflandırma modeli eğitilir ve değerlendirilir:

1. Multinomial Naive Bayes (MNB)
2. Karar Ağacı (Decision Tree)
3. Rastgele Orman (Random Forest)

Her model için aşağıdaki adımlar uygulanır:

- Veri seti eğitim ve test kümelerine bölünür.
- Model eğitim veri kümesine uygun hale getirilir.
- F1 skoru değerlendirme metriği olarak kullanılarak modelin performansını değerlendirmek için çapraz doğrulama yapılır.
- Sınıflandırma raporu ve karışıklık matrisi, modelin test veri kümesindeki performansını değerlendirmek için oluşturulur.

Ayrıca, Karar Ağacı ve MNB modellerini birleştiren bir VotingClassifier oluşturulur.

### Tahmin
"predict_spam" adında bir fonksiyon, yeni bir SMS mesajını spam veya ham olarak sınıflandırmak için sağlanır. Fonksiyon, örnekleme mesajını girdi olarak alır ve eğitilmiş Rastgele Orman modelini kullanarak tahmin edilen etiketi döndürür.

### Sonuç
Bu proje, spam SMS sınıflandırması için makine öğrenimi modelleri oluşturma ve değerlendirme sürecini göstermektedir. Metin önişleme, özellik mühendisliği ve Çanta Kelime Modeli (Bag of Words) temsili kullanarak spam mesajlarını tanımlamak için doğru tahminler yapılabilir. Rastgele Orman modeli en yüksek F1 skoruna sahip olmuştur, bu nedenle bu projede spam SMS sınıflandırması için tercih edilen modeldir.
