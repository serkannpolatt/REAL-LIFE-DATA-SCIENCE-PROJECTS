## English
## Text Emotions Prediction
This code builds a model for emotional labeling and text-based emotion prediction. Its functionality is performed through the following steps:

1. Data Reading:

	- The read_data function reads the data from a file and stores the labels and texts together.
	- The read data is represented within a list called data.

2. Feature Generation:

	- The ngram function creates n-grams from the text. An n-gram is a combination of consecutive n words or characters.
	- The create_feature function generates a feature vector from a text. The text is first converted to lowercase and then non-alphanumeric characters are removed. Finally, n-grams are created within the specified n-gram range.
	- Each text example is represented as a Counter object, which maintains the frequency of n-grams.

3. Label Transformation:

	- The convert_label function converts labels into emotional categories. For example, let's consider a label represented as "1 0 0 0 0 0 0". This label represents the "joy" category.
	- The emotional categories are defined as "joy," "fear," "anger," "sadness," "disgust," "shame," and "guilt."

4. Data Preparation:

	- Labels and feature vectors are stored separately in lists: y_all and X_all.
	- The dataset is split into training and test datasets. The train_test_split function is used, and the test dataset ratio is set to 20%.
	- Feature vectors are transformed into a sparse matrix using DictVectorizer.

5. Classification Models and Training:

	- Four different classification models are used: SVC (Support Vector Machine), LinearSVC (Linear Support Vector Machine), RandomForestClassifier, and DecisionTreeClassifier.
	- Each model is trained on the training dataset, and the training accuracy and test accuracy are calculated.

6. Results and Analysis:

	- The training and test accuracies of the trained models are printed in tabular form.
	- A list of labels and their frequencies is generated, sorted starting from the label with the highest frequency, and printed.
	- A text list is defined for predictions, and emotion predictions are made for each text. The prediction result is printed on the screen using emoji representations.

### Usage
1. Read the data from a file named text.txt.
2. Convert the dataset into feature vectors and transform the labels.
3. Split the dataset into training and test datasets.
4. Train the classification models and calculate the test accuracies.
5. Print the label frequencies.
6. Perform emotion prediction for specific texts and display the results using emoji representations.

## Real Time Sentiment Analysis
This code uses a sentiment analysis model to perform real-time sentiment analysis. Its functionality is carried out through the following steps:

1. Receive user feedback.
2. Calculate the emotional intensity of the text using the SentimentIntensityAnalyzer class from the nltk library.
3. Determine the sentiment of the text based on its emotional intensity: "Negative," "Positive," or "Neutral."
4. Print the result on the screen.

### Usage
1. Get the user's feedback text.
2. Analyze the emotional intensity of the text.
3. Determine the sentiment of the text based on its emotional intensity.
4. Print the result on the screen.

## Türkçe
## Text Emotions Prediction
Bu kod, duygusal etiketleme (emotional labeling) ve metin tabanlı duygu tahmini (text-based emotion prediction) yapmak için bir model oluşturur. İşlevselliği şu adımlarla gerçekleştirir:

1. Veri Okuma:

	- read_data fonksiyonu, verileri bir dosyadan okur ve etiketleri ve metinleri birlikte saklar.
	- Okunan veri, data adlı bir liste içinde temsil edilir.

2. Özellik Oluşturma:

	- ngram fonksiyonu, metinden n-gramlar oluşturur. Bir n-gram, ardışık n kelime veya karakterin bir kombinasyonudur.
	- create_feature fonksiyonu, bir metinden özellik vektörü oluşturur. Metin öncelikle küçük harflere dönüştürülür ve ardından alfasayısal olmayan karakterler kaldırılır. Son olarak, belirtilen n-gram aralığında n-gramlar oluşturulur.
	- Her metin örneği, bir Counter nesnesine dönüştürülerek temsil edilir. Bu nesne, n-gramların frekansını tutar.

3. Etiket Dönüşümü:

	- convert_label fonksiyonu, etiketleri duygusal kategorilere dönüştürür. Örnek olarak, bir etiketin "1 0 0 0 0 0 0" şeklinde temsil edildiğini düşünelim. Bu etiket, "joy" kategorisini temsil eder.
	- Duygusal kategoriler, "joy", "fear", "anger", "sadness", "disgust", "shame" ve "guilt" olarak tanımlanır.

4. Veri Hazırlama:

	- Etiketler ve özellik vektörleri ayrı ayrı listelerde saklanır: y_all ve X_all.
	- Veri seti, eğitim ve test veri setlerine ayrılır. train_test_split fonksiyonu kullanılır ve test veri setinin oranı %20 olarak belirlenir.
	- Özellik vektörleri, DictVectorizer kullanılarak seyrek bir matrise dönüştürülür.

5. Sınıflandırma Modelleri ve Eğitim:

	- Dört farklı sınıflandırma modeli kullanılır: SVC (Destek Vektör Makinesi), LinearSVC (Doğrusal Destek Vektör Makinesi), RandomForestClassifier (Rastgele Orman Sınıflandırıcısı) ve DecisionTreeClassifier (Karar Ağacı Sınıflandırıcısı).
	- Her bir model, eğitim veri seti üzerinde eğitilir ve eğitim doğruluğu ile test doğruluğu hesaplanır.

6. Sonuçlar ve Analiz:

	- 	Eğitilen modellerin eğitim ve test doğrulukları, tablo şeklinde yazdırılır.
	- 	Etiketlerin ve frekanslarının bir listesi, en yüksek frekansa sahip olan etiketten başlayarak sıralanır ve yazdırılır.

	- 	Tahminler için bir metin listesi tanımlanır ve her bir metin için duygu tahmini yapılır. Tahmin sonucu, emoji temsilleri kullanılarak ekrana yazdırılır.

### Kullanım
1. text.txt adlı bir dosyadan verileri okuyun.
2. Veri setini özellik vektörlerine dönüştürün ve etiketleri dönüştürün.
3. Veri setini eğitim ve test veri setlerine ayırın.
4. Sınıflandırma modellerini eğitin ve test doğruluklarını hesaplayın.
5. Etiket frekanslarını yazdırın.
6. Belirli metinler için duygu tahmini yapın ve sonuçları emoji temsilleriyle gösterin.

## Real Time Sentiment Analysis
Bu kod, gerçek zamanlı duygu analizi yapmak için bir duygu analizi modeli kullanır. İşlevselliği aşağıdaki adımlarla gerçekleştirir:

1. Kullanıcının geribildirimini alır.
2. nltk kütüphanesinden SentimentIntensityAnalyzer sınıfını kullanarak metnin duygusal yoğunluğunu hesaplar.
3. Duygusal yoğunluğa göre metnin duygusunu belirler: "Negatif", "Pozitif" veya "Nötr".
4. Sonucu ekrana yazdırır.

### Kullanım
1. Kullanıcıdan geri bildirim metnini alın.
2. Metnin duygusal yoğunluğunu analiz edin.
3. Duygusal yoğunluğa göre metnin duygusunu belirleyin.
4. Sonucu ekrana yazdırın.
