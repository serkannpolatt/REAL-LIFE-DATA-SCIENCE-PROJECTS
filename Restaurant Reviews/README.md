## English
## Restaurant Reviews Sentiment Analysis
This code snippet demonstrates the usage of a Naive Bayes classifier for sentiment analysis on a restaurant review dataset. It includes the following steps:

 ### Dataset
The code utilizes a dataset named "Restaurant_Reviews.tsv". This dataset represents a table containing restaurant reviews. The review text is stored under the "Review" column, while the labels indicating whether the review is positive or negative are under the "Liked" column. The dataset consists of 1000 review examples.

### Steps
This code snippet includes the following steps:

1. The dataset is loaded into a DataFrame using the pd.read_csv() function from the "Restaurant_Reviews.tsv" file.
2. The size of the dataset is checked using df.shape and outputs (1000, 2).
3. The columns of the DataFrame are checked using df.columns and outputs ['Review', 'Liked'].
4. The first five rows of the DataFrame are displayed using df.head().
5. Text data is cleaned: special characters are removed, converted to lowercase, tokenized, stop words are removed, and words are stemmed.
6. The cleaned texts are transformed into a vocabulary and a numerical representation using CountVectorizer.
7. The dataset is split into training and test data.
8. The Naive Bayes classifier MultinomialNB is trained.
9. Predictions are made on the test dataset, and accuracy, precision, and recall metrics are calculated.
10. A confusion matrix is created and visualized using a heatmap.
11. Hyperparameter tuning is performed on the Naive Bayes classifier to find the best accuracy value and alpha value.
12. A new classifier is created and trained with the best alpha value.
13. The predict_sentiment() function is defined to make sentiment predictions on a single review.
14. Predictions are made on sample reviews, and the results are printed on the screen.

This code snippet provides a starting point for predicting whether restaurant reviews are positive or negative based on the dataset. However, since the requirements of each project may vary, you may need to adapt or expand the code to suit your needs.

> *Please ensure that the necessary libraries are installed and the Restaurant_Reviews.tsv file is properly loaded for the code to run. Also, feel free to test it with your own reviews or work on a different dataset.*

## Türkçe
## Restoran İncelemeleri Duygu Analizi
Bu kod parçacığı, bir restoran inceleme veri seti üzerinde duygu analizi yapmak için kullanılan bir Naive Bayes sınıflandırıcısını göstermektedir. Aşağıdaki adımları içermektedir:

### Veri Seti
Kod, "Restaurant_Reviews.tsv" adlı bir veri setini kullanmaktadır. Bu veri seti, restoran incelemelerini içeren bir tabloyu temsil etmektedir. İnceleme metni, "Review" sütunu altında depolanırken, incelemenin olumlu veya olumsuz olduğunu belirten etiketler "Liked" sütunu altında yer almaktadır. Veri seti, 1000 inceleme örneği içermektedir.

### Adımlar
Bu kod parçacığı aşağıdaki adımları içermektedir:

1. Veri seti "Restaurant_Reviews.tsv" dosyasından pd.read_csv() fonksiyonuyla bir DataFrame'e yüklenir.
2. Veri setinin boyutu df.shape kullanılarak kontrol edilir ve (1000, 2) olarak çıktı verir.
3. DataFrame'in sütunları df.columns ile kontrol edilir ve ['Review', 'Liked'] olarak çıktı verir.
4. DataFrame'in ilk beş satırı df.head() ile görüntülenir.
5. Metin verileri temizlenir: özel karakterler kaldırılır, küçük harflere dönüştürülür, kelimelere ayrılır, durma kelimeleri çıkarılır ve kökleri bulunur.
6. CountVectorizer kullanılarak temizlenen metinler bir kelime dağarcığına dönüştürülür ve sayısal bir temsiliyet elde edilir.
7. Veri seti eğitim ve test verilerine ayrılır.
8. Naive Bayes sınıflandırıcısı MultinomialNB kullanılarak eğitilir.
9. Test veri seti üzerinde tahminler yapılır ve doğruluk, hassasiyet ve geri çağırma metrikleri hesaplanır.
10. Karışıklık matrisi oluşturulur ve ısı haritasıyla görselleştirilir.
11. Naive Bayes sınıflandırıcısının hiperparametre ayarlaması yapılır ve en iyi doğruluk değeri ve alfa değeri belirlenir.
12. En iyi alfa değeriyle yeni bir sınıflandırıcı oluşturulur ve eğitilir.
13. Tek bir inceleme üzerinde duygu tahmini yapmak için predict_sentiment() fonksiyonu tanımlanır.
14. Örnek incelemeler üzerinde tahminler yapılır ve sonuçlar ekrana yazdırılır.

Bu kod parçacığı, veri setindeki restoran incelemelerinin olumlu veya olumsuz olduğunu tahmin etmek için kullanılan bir başlangıç noktası sunmaktadır. Ancak, her projenin gereksinimleri farklı olabileceğinden, kodu ihtiyaçlarınıza uyacak şekilde uyarlamak veya genişletmek gerekebilir.

> *Lütfen kodun çalışması için gerekli kütüphanelerin yüklü olduğundan ve Restaurant_Reviews.tsv dosyasının doğru bir şekilde yüklendiğinden emin olun. Ayrıca, kendi incelemelerinizi test etmek veya farklı bir veri seti üzerinde çalışmak için*
