## English
## Sentiment Analysis with Naive Bayes Classifier 
This code performs sentiment analysis using the Naive Bayes classifier on a given dataset. It aims to classify text data into positive or negative sentiments. The main purpose of the code is to demonstrate a simple implementation of sentiment analysis using the Naive Bayes algorithm.

### Purpose and Functionality
The purpose of this code is to analyze text data and determine the sentiment associated with it. It uses the Naive Bayes classifier, a popular machine learning algorithm, to classify text into positive or negative sentiments. The code includes the following functionality:

**1. Data Loading and Splitting:** The code loads the dataset from a CSV file and splits it into a training set and a test set. The training set is used to train the Naive Bayes classifier, while the test set is used to evaluate the performance of the trained model.

**2. Data Preprocessing:** The code preprocesses the text data in the training set by removing neutral sentiments and separating positive and negative sentiments. It also defines a helper function, wordcloud_draw, to generate word clouds based on the text data, which can provide insights into the most frequent words associated with each sentiment.

**3. Text Processing:** The code further processes the text data by filtering out stopwords (common words that do not carry much meaning) and removing URLs, usernames, and other irrelevant symbols. This step helps in improving the quality of the data used for training and classification.

**4. Feature Extraction and Model Training:** The code extracts features from the processed text data using the Naive Bayes algorithm. It creates a feature set based on the frequency distribution of words in the training set. The extracted features are then used to train the Naive Bayes classifier.

**5. Model Evaluation:** The code evaluates the trained model using the test set. It applies the trained classifier to classify the text in the test set into positive or negative sentiments. The number of correctly classified positive and negative sentiments is counted and displayed as the evaluation result.

The code provides a simple implementation of sentiment analysis using the Naive Bayes classifier. It can serve as a starting point for sentiment analysis tasks and can be extended or customized according to specific needs and datasets.

> *Please note that the code provided in this project is a sample application of sentiment analysis on the "Sentiment.csv" dataset. To use the code with your own dataset, you may need to modify it according to your specific requirements.*

## Türkçe
## Naive Bayes Sınıflandırıcısı ile Duygu Analizi
Bu kod, verilen bir veri kümesi üzerinde Naive Bayes sınıflandırıcısı kullanarak duygu analizi yapmaktadır. Metin verilerini pozitif veya negatif duygulara sınıflandırmayı amaçlamaktadır. Kodun temel amacı, Naive Bayes algoritmasını kullanarak duygu analizi yapmanın basit bir uygulamasını sunmaktır.

### Amaç ve İşlev
Bu kodun amacı, metin verilerini analiz etmek ve ilişkilendirilen duyguyu belirlemektir. Metin verilerini pozitif veya negatif duygulara sınıflandırmak için yaygın olarak kullanılan Naive Bayes sınıflandırıcısını kullanır. Kod aşağıdaki işlevleri içermektedir:

**1. Veri Yükleme ve Bölümleme:** Kod, veri kümesini bir CSV dosyasından yükler ve eğitim kümesine ve test kümesine böler. Eğitim kümesi, Naive Bayes sınıflandırıcısını eğitmek için kullanılırken, test kümesi ise eğitilmiş modelin performansını değerlendirmek için kullanılır.

**2. Veri Önişleme:** Kod, eğitim kümesindeki metin verilerini önişleme işlemine tabi tutar. Nötr duyguları çıkarır ve pozitif ve negatif duyguları ayırır. Ayrıca, metin verilerine dayalı olarak en sık kullanılan kelimelerin belirlenmesine yardımcı olan wordcloud_draw adlı bir yardımcı fonksiyon tanımlar.

**3. Metin İşleme:** Kod, metin verilerini daha da işlemek için stopwords (anlam taşımayan yaygın kelimeler) filtrelemesi yapar ve URL'leri, kullanıcı adlarını ve diğer ilgisiz sembolleri kaldırır. Bu adım, eğitim ve sınıflandırma için kullanılan verinin kalitesini artırmaya yardımcı olur.

**4. Özellik Çıkarma ve Model Eğitimi:** Kod, işlenmiş metin verilerinden özellikler çıkararak Naive Bayes algoritmasını kullanır. Eğitim kümesindeki kelimelerin frekans dağılımına dayalı olarak bir özellik kümesi oluşturur. Elde edilen özellikler, Naive Bayes sınıflandırıcısını eğitmek için kullanılır.

**5. Model Değerlendirme:** Kod, test kümesini kullanarak eğitilmiş modeli değerlendirir. Eğitilmiş sınıflandırıcıyı test kümesindeki metinleri pozitif veya negatif duygulara sınıflandırmak için kullanır. Doğru bir şekilde sınıflandırılan pozitif ve negatif duyguların sayısı hesaplanır ve değerlendirme sonucu olarak gösterilir.

Bu kod, Naive Bayes sınıflandırıcısı kullanarak duygu analizi yapmanın basit bir uygulamasını sunar. Duygu analizi görevleri için bir başlangıç noktası olarak hizmet edebilir ve belirli ihtiyaçlara ve veri kümelerine göre genişletilebilir veya özelleştirilebilir.

> *Lütfen unutmayın, bu projedeki kod, "Sentiment.csv" veri kümesi üzerinde duygu analizi için bir örnek uygulamadır. Kendi veri kümenizi kullanmak için kodu belirli gereksinimlerinize göre değiştirmeniz gerekebilir.*
