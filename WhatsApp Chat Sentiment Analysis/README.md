## English
## WhatsApp Message Analysis
This code is used to analyze WhatsApp messages and perform sentiment analysis. The code reads messages, extracts date and time information, identifies message authors, and retrieves the message content. It then analyzes the emotional content of the messages and calculates a positive, negative, or neutral sentiment intensity score.

### Libraries Used

- re
- pandas
- numpy
- emoji
- collections
- matplotlib
- PIL
- wordcloud
- nltk.sentiment.vader

### Functions
1. date_time(s): Extracts date and time information from a given string and checks if it is in the correct format.

2. find_author(s): Used to determine the author of a message.

3. getDatapoint(line): Extracts date, time, author, and message content information from a line.

4. Data Loading and Processing:

	- Reads a specified WhatsApp messages file.
	- Extracts the necessary information to analyze the messages.
	- Creates a dataframe using the extracted data.

5. Sentiment Analysis:

	- Analyzes the emotional content of the messages using the SentimentIntensityAnalyzer class.
	- Calculates the positive, negative, and neutral sentiment intensities for each message.

6. sentiment_score(a, b, c): Determines the overall sentiment based on the positive, negative, and neutral sentiment intensities and prints it to the screen.

### Usage

1. Install the required libraries.
2. Create a file, such as wp.txt, and paste the WhatsApp messages into this file.
3. Run the code and observe the results of the sentiment analysis.

You are free to modify and adapt the code according to specific requirements for WhatsApp message analysis.

## Türkçe
## WhatsApp Mesaj Analizi
Bu kod, WhatsApp mesajlarını analiz etmek ve duygusal bir analiz yapmak için kullanılır. Kod, mesajları okur, tarih ve saat bilgilerini çıkarır, mesaj yazarını belirler ve mesajların içeriğini alır. Ardından, mesajlardaki duygusal içeriği analiz eder ve pozitif, negatif veya nötr bir duygu yoğunluğu puanı hesaplar.

### Kullanılan Kütüphaneler

- re
- pandas
- numpy
- emoji
- collections
- matplotlib
- PIL
- wordcloud
- nltk.sentiment.vader

### İşlevler

1. date_time(s): Verilen bir dizeyi kullanarak tarih ve saat bilgilerini ayıklar ve doğru formatta olup olmadığını kontrol eder.
2. find_author(s): Bir mesajın yazarını belirlemek için kullanılır.
3. getDatapoint(line): Bir satırdan tarih, saat, yazar ve mesaj içeriği bilgilerini ayıklar.
4. Veri yükleme ve işleme:

	- Belirtilen bir WhatsApp mesajları dosyasını okur.
	- Mesajları analiz etmek için gerekli bilgileri ayıklar.
	- Ayıklanan verileri kullanarak bir veri çerçevesi oluşturur.

5. Duygu Analizi:

	- SentimentIntensityAnalyzer sınıfını kullanarak mesajların duygusal içeriğini analiz eder.
	- Her mesaj için pozitif, negatif ve nötr duygu yoğunluklarını hesaplar.

6. sentiment_score(a, b, c): Pozitif, negatif ve nötr duygu yoğunluklarına dayanarak genel duygu durumunu belirler ve ekrana yazdırır.

### Kullanım
1. Gerekli kütüphaneleri yükleyin.
2. wp.txt gibi bir dosya oluşturun ve WhatsApp mesajlarını içeren bu dosyaya mesajları yapıştırın.
3. Kodu çalıştırın ve duygusal analiz sonuçlarını gözlemleyin.

Kodu, WhatsApp mesajları analizi için kullanılan özel gereksinimlere göre düzenlemekte ve uyarlamakta özgürsünüz.
