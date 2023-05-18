## English

This code demonstrates the usage of the Pegasus model for text summarization. Pegasus is a state-of-the-art transformer-based model designed specifically for abstractive text summarization.

### **Description**
The code imports the necessary dependencies from the Transformers library, which is a powerful library for natural language processing tasks. It utilizes the Pegasus model and tokenizer for text summarization.

### **The main steps involved in the code are as follows:**

- **Importing dependencies:** The code imports the PegasusForConditionalGeneration model and the PegasusTokenizer from the Transformers library.
- **Loading the tokenizer:** It loads the Pegasus tokenizer from the "google/pegasus-xsum" pre-trained model.
- **Loading the model:** It loads the pre-trained Pegasus model for conditional generation from "google/pegasus-xsum".
- **Creating tokens:** The input text is tokenized using the tokenizer, which converts the text into a numerical representation.
- **Generating summary:** The model is used to generate a summary for the given text.
- **Decoding summary:** The generated summary tokens are decoded back into human-readable text.

This code showcases the basic usage of the Pegasus model for text summarization. It can be used to summarize various types of text, such as articles, documents, or news.

### **How to Use**
- Install the Transformers library by running pip install transformers in your Python environment.
- Copy the code into your Python IDE or Jupyter Notebook.
- Make sure the Pegasus model and tokenizer are downloaded from the Hugging Face model hub.
- Modify the text variable to the desired input text that you want to summarize.
- Run the code and observe the generated summary.

> *Please note that the quality and accuracy of the generated summary may vary depending on the input text and the pre-trained model used.
Feel free to experiment with different inputs, adjust the tokenization and summarization parameters, or explore other transformer-based models provided by the Transformers library.*

## **Türkçe**

Bu kod, metin özetleme için Pegasus modelinin kullanımını göstermektedir. Pegasus, özgün metin özetleme için özel olarak tasarlanmış, son teknolojiye sahip bir transformer tabanlı modeldir.

### **Açıklama**
Kod, doğal dil işleme görevleri için güçlü bir kütüphane olan Transformers kütüphanesinden gerekli bağımlılıkları içe aktarır. Metin özetlemesi için Pegasus modelini ve belirteci kullanır.

### **Kodun içerdiği temel adımlar aşağıdaki gibidir:**
- **Bağımlılıkların içe aktarılması:** Kod, Transformers kütüphanesinden PegasusForConditionalGeneration modelini ve PegasusTokenizer'ı içe aktarır.
- **Belirtecin yüklenmesi:** "google/pegasus-xsum" önceden eğitilmiş modelinden Pegasus belirteci yüklenir.
- **Modelin yüklenmesi:** "google/pegasus-xsum" önceden eğitilmiş Pegasus modeli koşullu üretme için yüklenir.
- **Belirteçlerin oluşturulması:** Girdi metin, metinleri sayısal bir temsile dönüştüren belirteç kullanılarak belirteçlere ayrılır.
- **Özetin oluşturulması:** Model, verilen metin için bir özet oluşturmak için kullanılır.
- **Özetin çözümlenmesi:** Oluşturulan özet belirteçleri insan tarafından okunabilir metne çözümlenir.

Bu kod, metin özetleme için Pegasus modelinin temel kullanımını sergiler. Makaleler, belgeler veya haberler gibi çeşitli metin türlerini özetlemek için kullanılabilir.

### **Kullanım Talimatları**
- Transformers kütüphanesini Python ortamınızda pip install transformers komutunu çalıştırarak yükleyin.
- Kodu Python IDE'nize veya Jupyter Notebook'a kopyalayın.
- Pegasus modelini ve belirtecinin Hugging Face model havuzundan indirildiğinden emin olun.
- İstenilen girdi metni için text değişkenini düzenleyin.
- Kodu çalıştırın ve oluşturulan özet metnini gözlemleyin.

> *Lütfen oluşturulan özetin kalitesi ve doğruluğunun girdi metnine ve kullanılan önceden eğitilmiş modele bağlı olarak değişebileceğini unutmayın.
Transformers kütüphanesi tarafından sağlanan diğer transformer tabanlı modelleri keşfetmek için farklı girdilerle deney yapmaktan, belirteçleme ve özetleme parametrelerini ayarlamaktan çekinmeyin.*
