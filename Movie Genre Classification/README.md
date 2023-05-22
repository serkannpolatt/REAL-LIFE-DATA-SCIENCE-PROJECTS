## English
## Movie Genre Prediction Project

### Objective
This project aims to create a machine learning model to predict movie genres. Here are the project steps:

1. Data Preparation:
	- Read the movie_metadata.tsv and plot_summaries.tsv data files.
	- Rename the necessary columns and merge the data frames.
	- Clean the genre labels and remove rows without a genre.

2. Data Exploration:
	- Calculate the number of unique movie genres and determine their frequencies.
	- Visualize the top 50 most common genres.

3. Text Preprocessing:
	- Clean unnecessary characters from the text data.
	- Remove stop words.
	- Stem words to their roots.

4. Data Splitting:
	- Split the dataset into training and test sets.

5. Feature Extraction:
	- Convert the text data into numerical features using TfidfVectorizer.

6. Model Creation:
	- Create a multi-class logistic regression model using OneVsRestClassifier.

7. Model Evaluation:
	- Evaluate the performance of the model using the F1 score.

8. Predictions:
	- Predict movie genres for a specific movie summary.

By following these steps, you can create a model that predicts movie genres using movie summaries.


## Türkçe
## Film Türü Tahminleme Projesi

### Amaç
Bu proje, film türlerini tahminlemek için bir makine öğrenimi modeli oluşturmayı amaçlamaktadır. İşte proje adımları:

1. Veri Hazırlama:
	- movie_metadata.tsv ve plot_summaries.tsv veri dosyalarını okuyun.
	- Gerekli sütunları yeniden adlandırın ve veri çerçevelerini birleştirin.
	- Tür etiketlerini temizleyin ve türü olmayan satırları kaldırın.

2. Veri Keşfi:
	- Benzersiz film türlerinin sayısını hesaplayın ve frekanslarını belirleyin.
	- En çok geçen 50 türü görselleştirin.

3. Metin Önişleme:
	- Metin verilerindeki gereksiz karakterleri temizleyin.
	- Stop kelimelerini kaldırın.
	- Kelimeleri köklerine indirgeyin.

4. Veri Bölme:
	- Veri setini eğitim ve test setlerine ayırın.

5. Özellik Çıkarımı:
	- TfidfVectorizer kullanarak metin verilerini sayısal özelliklere dönüştürün.

6. Model Oluşturma:
	- OneVsRestClassifier kullanarak çok sınıflı bir lojistik regresyon modeli oluşturun.

7. Model Değerlendirme:
	- F1 skoru kullanarak modelin performansını değerlendirin.

8. Tahminler:
	- Belirli bir film özeti için film türlerini tahminleyin.


Bu adımları takip ederek, film özetleri kullanarak film türlerini tahminleyen bir model oluşturabilirsiniz.
