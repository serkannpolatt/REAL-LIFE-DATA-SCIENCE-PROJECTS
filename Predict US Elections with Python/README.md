## English
##  Sentiment Analysis: A Comparison of Politicians' Reviews
This repository contains code for performing sentiment analysis on politicians' reviews. The code utilizes libraries such as Pandas, NumPy, Seaborn, Matplotlib, TextBlob, and WordCloud for data analysis and visualization purposes.

### Purpose
The purpose of this code is to analyze politicians' reviews and conduct sentiment analysis. Using the TextBlob library, the emotional sentiment of the reviews is calculated and labeled as positive, negative, or neutral. Additionally, the code visualizes the percentage of positive and negative sentiments for each politician.

### Dataset
The code uses a dataset named "Trumpall2.csv," which contains reviews for Trump and Biden. Each review is represented as a record with text and sentiment analysis results.

### Usage
To use this code, follow these steps:

1. Ensure that the necessary dependencies, including Pandas, NumPy, Seaborn, Matplotlib, TextBlob, and WordCloud, are installed.

2. Prepare the dataset in CSV format and save it as "Trumpall2.csv" in the same directory as the code.

3. Run the code using a Python interpreter or your preferred integrated development environment.

4. The code performs the following steps:
	- Loads the dataset and provides an initial preview.
	- Utilizes TextBlob to calculate the emotional sentiment of the reviews.
	- Appends the sentiment analysis results to the dataset.
	- Labels neutral sentiment as "Neutral."
	- Labels positive and negative sentiments as "positive" and "negative," respectively.
	- Removes reviews with neutral sentiment from the dataset.
	- Checks the size of the dataset and performs sampling if necessary.
	- Calculates the percentage of positive and negative sentiments in the reviews.
	- Visualizes the positive and negative sentiment percentages for the politicians.

### Results
The code performs sentiment analysis on politicians' reviews and visualizes the percentages of positive and negative sentiments. This analysis can be used to understand the public perception of the politicians.

> *Please note that the interpretation and application of the results may vary depending on the specific business context and dataset used.*

## Türkçe 
##  Duygu Analizi ile Politikacıların İncelemelerinin Karşılaştırılması
Bu depo, politikacıların incelemelerinin duygu analizi ile karşılaştırılması için kod içermektedir. Kod, Pandas, NumPy, Seaborn, Matplotlib, TextBlob ve WordCloud gibi kütüphaneleri kullanarak veri analizi ve görselleştirme işlemlerini gerçekleştirir.

### Amaç
Bu kodun amacı, politikacıların incelemelerini analiz etmek ve duygu analizi yapmaktır. TextBlob kütüphanesi kullanılarak incelemelerin duygusal durumu hesaplanır ve pozitif, negatif veya nötr olarak etiketlenir. Ayrıca, politikacıların pozitif ve negatif duygusal yüzdeleri görselleştirilir.

### Veri Kümesi
Kod, "Trumpall2.csv" adlı bir veri kümesini kullanır. Bu veri kümesi, Trump ve Biden için yapılan incelemeleri içerir. Her bir inceleme, metin ve duygu analizi sonucunu içeren bir kayıt olarak temsil edilir.

### Kullanım
Bu kodu kullanmak için aşağıdaki adımları izleyin:

1. pandas, numpy, seaborn, matplotlib, textblob ve wordcloud gibi gerekli bağımlılıkların yüklü olduğundan emin olun.

2. Veri kümesini CSV formatında hazırlayın ve kod ile aynı dizinde "Trumpall2.csv" olarak kaydedin.

3. Python yorumlayıcısı veya tercih ettiğiniz bir entegre geliştirme ortamında kodu çalıştırın.

4. Kod aşağıdaki adımları gerçekleştirir:
	- Veri kümesini yükler ve başlangıçta bir önizleme yapar.
	- İncelemelerin duygusal durumunu hesaplamak için TextBlob'u kullanır.
	- Duygu analizi sonuçlarını veri kümesine ekler.
	- Nötr duygusal durumları "Neutral" olarak etiketler.
	- Pozitif ve negatif duygusal durumları "positive" ve "negative" olarak etiketler.
	- Duygu analizi sonucu nötr olan incelemeleri veri kümesinden çıkarır.
	- Veri kümesinin boyutunu kontrol eder ve gerektiğinde örnekleme yapar.
	- İncelemelerin pozitif ve negatif yüzdesini hesaplar.
	- Politikacıların pozitif ve negatif yüzdelerini görselleştirir.

### Sonuçlar
Kod, politikacıların incelemelerinin duygu analizini yapar ve pozitif ve negatif yüzdelerini görselleştirir. Bu analiz, politikacıların halk nezdindeki algısını anlamak için kullanılabilir.

> *Lütfen unutmayın ki sonuçların yorumlanması ve uygulanması, özel iş bağlamı ve kullanılan veri kümesine bağlı olarak değişebilir.*
