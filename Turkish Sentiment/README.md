## English
## Turkish Sentiment Analysis
This project utilizes LSTM (Long Short-Term Memory) artificial neural networks to perform sentiment analysis. Its objective is to classify positive or negative sentiment on Turkish text data.

### Libraries
Make sure the following Python libraries are installed for the project to run properly:

- nltk
- pandas
- numpy
- re
- sklearn
- tensorflow
- keras

### Data Preparation
The project fetches data from an Excel file named "sentiment_analysis.xlsx". The data should be located in the worksheet named "Sheet1". The dataset should contain the columns "Text" for the text data and "Sentiment" for the sentiment labels.

The data preprocessing steps include:

- Removing punctuation marks
- Converting uppercase letters to lowercase
- Removing extra whitespace
- Removing stop words

### Data Splitting
The dataset needs to be split into training and test data. This is done using the train_test_split function. By default, 80% of the data is used for training, and 20% is used for testing.

### Tokenization and Sequencing
The text data in the dataset is tokenized, meaning it is divided into words, and then each word is converted into a numerical representation. This process is performed using the Tokenizer class. A word index is created based on the frequency of words in the dataset. The texts are transformed into sequences of numbers according to this word index.

### Model Creation
The project utilizes a sequential model. The model architecture consists of the following layers:

- An embedding layer to represent words
- Two LSTM (Long Short-Term Memory) layers
- A dense output layer

The model is compiled with the Adam optimizer and the binary_crossentropy loss function. A validation split of 25% is used during training.

### Training and Evaluation
The model is trained on the training data for the specified number of epochs. The training results are evaluated on the validation data. Finally, the model is evaluated on the test data.

### Results
After completing the training and testing processes, the model's performance metrics such as accuracy, loss, and AUC are obtained.

> *The provided code in this project offers an example application for sentiment analysis on the "sentiment_analysis.xlsx" dataset. Please adapt the code to your needs when using your own dataset.*

## Türkçe
## Turkish Sentiment

Bu proje, duygu analizi yapmak için LSTM (Uzun Kısa Vadeli Hafıza) yapay sinir ağlarını kullanmaktadır. Türkçe metin verileri üzerinde pozitif veya negatif duyguyu sınıflandırmayı amaçlamaktadır.

### Kütüphaneler
Projenin çalışması için aşağıdaki Python kütüphanelerinin kurulu olması gerekmektedir:

- nltk
- pandas
- numpy
- re
- sklearn
- tensorflow
- keras

Kütüphanelerin kurulu olduğundan emin olun.

### Veri Hazırlama
Proje, "sentiment_analysis.xlsx" adında bir Excel dosyasından veri alır. Veri, "Sheet1" adlı çalışma sayfasında bulunmalıdır. Veri seti, metin (Text) ve duygu etiketi (Sentiment) sütunlarını içermelidir.

Veri ön işleme aşamaları şunlardır:

- Noktalama işaretlerinin temizlenmesi
- Büyük harflerin küçük harflere dönüştürülmesi
- Fazladan boşlukların temizlenmesi
- Stop kelimelerin (durak kelimelerin) kaldırılması

### Veri Bölümleme
Veri seti, eğitim ve test verisi olarak bölünmelidir. Bu işlem, train_test_split fonksiyonu kullanılarak gerçekleştirilir. Varsayılan olarak, veri setinin %80'i eğitim için kullanılır ve %20'si test için ayrılır.

### Tokenizasyon ve Diziye Dönüştürme
Veri setindeki metinler, kelimelere bölünür ve ardından her kelime bir sayıya dönüştürülür. Bu işlem, Tokenizer sınıfı kullanılarak gerçekleştirilir. Veri setindeki kelimelerin sıklığına göre belirlenen bir kelime dizini oluşturulur. Metinler, bu kelime dizinine göre sayılara dönüştürülerek dizi haline getirilir.

### Model Oluşturma
Proje, ardışık (sequential) bir model kullanır. Modelin mimarisi şu şekildedir:

- Kelimeleri temsil etmek için bir gömme katmanı (embedding layer)
- İki LSTM (Uzun Kısa Vadeli Hafıza) katmanı
- Bir yoğun (dense) çıkış katmanı

Model, adam optimizeri ve binary_crossentropy kayıp fonksiyonuyla derlenir. Eğitim sırasında doğrulama bölümlemesi için %25 ayrılır.

### Modeli Eğitme ve Değerlendirme
Model, eğitim verisi üzerinde belirtilen sayıda epokla eğitilir. Eğitim sonuçları doğrulama verisi üzerinde değerlendirilir. Son olarak, model, test verisi üzerinde değerlendirilir.

### Sonuçlar
Eğitim ve test işlemleri tamamlandıktan sonra, modelin başarı metrikleri (doğruluk, kayıp, AUC) elde edilir.

> *Bu projede kullanılan kod, sentiment_analysis.xlsx veri seti üzerinde duygu analizi yapmak için örnek bir uygulama sunmaktadır. Lütfen kendi veri setinizi kullanmak için kodu ihtiyaçlarınıza göre uyarlayın.*
