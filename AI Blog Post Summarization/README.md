## English

 This code snippet demonstrates how to use the Transformers library to perform text summarization on a blog post. The code uses the pip install transformers command to install the required library and imports the necessary modules: pipeline from Transformers, and BeautifulSoup and requests for web scraping.
**Load Summarization Pipeline:** The code initializes a summarization pipeline using the pipeline("summarization") function from Transformers.

**Get Blog Post from Medium:** The code fetches the content of a blog post from a Medium or Hacker Noon URL. The URL can be modified to retrieve content from different sources. It uses the requests library to make an HTTP  request to the URL and BeautifulSoup to parse the HTML response.

**Preprocess Text:** The code performs some preprocessing on the article text to split it into chunks of a maximum length (500 words in this case) to fit the summarization model's input requirements. It splits the text  ###  into sentences by adding "<eos>" at the end of each sentence and then divides the sentences into chunks of suitable size.

** Summarize Text:** The code iterates over the chunks and uses the summarization pipeline to generate summaries for each chunk. It sets the maximum summary length to 120 words and the minimum length to 30 words. The ### ### do_sample parameter is set to False to generate deterministic outputs.

**Output to Text File:** The code joins the generated summaries into a single text string and writes it to a file named "blogsummary.txt".

> *Note*: Make sure to install the required libraries (transformers, beautifulsoup4) before running the code.

  
  
## Türkçe
Bu kod örneği, bir blog yazısında metin özetleme işlemini gerçekleştirmek için Transformers kütüphanesinin nasıl kullanılacağını göstermektedir. Kod, gerekli kütüphaneyi yüklemek için pip install transformers komutunu kullanır ve gerekli modülleri içe aktarır: Transformers'dan pipeline ve web kazıma için BeautifulSoup ve requests.

**Özetleme Pipeline'ını Yükle**: Kod, Transformers'dan pipeline("summarization") işlevini kullanarak bir özetleme pipeline'ı başlatır.

**Medium'dan Blog Yazısı Al:** Kod, bir Medium veya Hacker Noon URL'sinden blog yazısı içeriğini alır. URL, farklı kaynaklardan içerik almak için değiştirilebilir. Kod, URL'ye bir HTTP isteği yapmak için requests kütüphanesini kullanır ve HTML yanıtını ayrıştırmak için BeautifulSoup'u kullanır.

**Metni Ön İşle:** Kod, makale metnini özetleme modelinin giriş gereksinimlerine uyacak şekilde maksimum uzunluğa (bu durumda 500 kelime) sahip parçalara bölmek için bazı ön işlemler yapar. Metni cümlelere bölmek için her cümlenin sonuna "<eos>" ekler ve ardından cümleleri uygun boyutta parçalara böler.

**Metni Özetle:** Kod, parçalar üzerinde döngü oluşturarak her bir parça için özetleme pipeline'ını kullanır ve özetler oluşturur. Maksimum özet uzunluğunu 120 kelime, minimum uzunluğunu ise 30 kelime olarak ayarlar. do_sample parametresi False olarak ayarlanır ve belirlenmiş çıktılar üretmek için kullanılır.

**Metni Metin Dosyasına Yaz:** Kod, oluşturulan özetleri tek bir metin dizesine birleştirir ve "blogsummary.txt" adında bir dosyaya yazar.

> *Not: Kodu çalıştırmadan önce gereken kütüphanelerin (transformers, beautifulsoup4) yüklü olduğundan emin olun.*
