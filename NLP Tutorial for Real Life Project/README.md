## English
## Author Identification using Text Analysis
This project aims to develop a model that can accurately identify authors based on their writing style using text analysis techniques. The goal is to create a system that can predict the author of a given text sample by analyzing its linguistic features.

### Project Steps

**1. Data Acquisition:** The project starts by downloading the required dataset from the UCI Machine Learning Repository. The dataset contains text samples from various authors.

**2. Data Preparation:** The downloaded dataset is extracted and organized into a suitable folder structure. Each text file is read and stored in a dictionary, labeled by the author's name.

**3. Text Parsing:** The project utilizes the Spacy library to parse the text samples and convert them into Spacy doc objects. This step allows for further linguistic analysis and feature extraction.

**4. TextBlob Conversion:** The text samples are also converted into TextBlob objects, which provide additional text processing capabilities such as sentiment analysis and noun phrase extraction.

**5. Text Cleaning:** The project performs various text cleaning tasks, including removing unnecessary characters, special symbols, and newline characters. The cleaned text is then stored for further analysis.

**6. Sentence and Tokenization:** The text samples are segmented into sentences and tokens using Spacy's sentence and tokenization functions. This step enables the analysis of sentence-level and token-level features.

**7. Lemmatization and Stemming:** The project applies lemmatization and stemming techniques to normalize the tokens and reduce them to their base forms. This process helps in reducing vocabulary size and capturing the essence of the text.

**8. Part-of-Speech Tagging:** The project utilizes Spacy's part-of-speech tagging functionality to assign grammatical tags to each token. This information can be used as a feature for author identification.

**9. N-gram Generation:** N-grams, which are contiguous sequences of n tokens, are generated from the text samples. This step provides insights into the co-occurrence patterns of words and captures higher-level language structures.

**10. Stop Word Removal:** Stop words, such as common articles and prepositions, are removed from the text samples. This step helps in eliminating noise and focusing on more meaningful features.

**11. Custom Text Processing:** Custom text processing functions are implemented to handle specific requirements, such as removing non-alphabetic characters and generating customized feature sets.

**12. Feature Extraction:** Various linguistic features, such as the frequency of specific words, syntactic patterns, and structural characteristics, are extracted from the text samples. These features serve as inputs for the author identification models.

**13. Model Training and Evaluation:** Two classification models, namely Naive Bayes and Support Vector Machines (SVM), are trained on the extracted features. The models are evaluated using accuracy scores and classification reports to measure their performance.

**14. Model Selection and Optimization:** Grid search is performed to identify the best hyperparameters for the SVM model. The model with the highest F1 score is selected as the final model for author identification.

**15. Model Persistence:** The final selected model is serialized and saved to disk using the joblib library. This allows for later reuse and deployment.

### Usage
To use this project, follow the steps outlined in the code. Make sure to have the necessary dependencies installed and the dataset downloaded from the provided link. Adjust the code as needed for different datasets or specific requirements.

> Please note that the code provided in this example is for demonstration purposes only and may need modifications to fit your specific use case or dataset.

### Conclusion
Author identification using text analysis techniques can be a challenging yet interesting task. By leveraging the power of natural language processing and machine learning, it is possible to develop models that can accurately predict the author of a given text sample. This project provides a foundation for further exploration and refinement in the field of author identification and related applications.


## Türkçe
## Metin Analizi Kullanarak Yazar Tanımlama
Bu proje, metin analizi tekniklerini kullanarak yazarları yazı tarzlarına dayalı olarak doğru bir şekilde tanımlayabilen bir model geliştirmeyi amaçlamaktadır. Hedef, bir metin örneğinin dilbilimsel özelliklerini analiz ederek verilen metin örneğinin yazarını tahmin edebilen bir sistem oluşturmaktır.

### Proje Adımları

**1. Veri Edinme:** Proje, gerekli veri kümesini UCI Makine Öğrenimi Deposu'ndan indirerek başlar. Veri kümesi çeşitli yazarların metin örneklerini içermektedir.

**2. Veri Hazırlığı:** İndirilen veri kümesi çıkarılır ve uygun bir klasör yapısına yerleştirilir. Her bir metin dosyası yazarın adıyla etiketlenmiş bir sözlükte okunur ve depolanır.

**3. Metin Ayrıştırma:** Proje, metin örneklerini ayrıştırmak ve bunları Spacy doc nesnelerine dönüştürmek için Spacy kütüphanesini kullanır. Bu adım, daha ileri dilbilimsel analiz ve özellik çıkarımı için olanak sağlar.

**4. TextBlob Dönüşümü:** Metin örnekleri aynı zamanda TextBlob nesnelerine dönüştürülür, bu da duygu analizi ve isim öbeği çıkarma gibi ek metin işleme yetenekleri sağlar.

**5. Metin Temizleme:** Proje, gereksiz karakterlerin, özel sembollerin ve yeni satır karakterlerinin kaldırılması da dahil olmak üzere çeşitli metin temizleme görevlerini gerçekleştirir. Temizlenmiş metin daha sonra ileri analiz için depolanır.

**6. Cümle ve Sözcük Bölümleme:** Metin örnekleri, Spacy'nin cümle ve sözcük bölümleme fonksiyonlarını kullanarak cümlelere ve sözcüklere ayrılır. Bu adım, cümle düzeyinde ve sözcük düzeyinde özelliklerin analizine olanak sağlar.

**7. Lemmatizasyon ve Kök Bulma:** Proje, sözcüklerin normalleştirilmesi ve köklerine indirgenmesi için lemmatizasyon ve kök bulma tekniklerini uygular. Bu süreç, kelime dağarcığını küçültmede ve metnin özünü yakalamada yardımcı olur.

**8. Kelime Cinsi Etiketleme:** Proje, her bir sözcüğe dilbilimsel etiketler atamak için Spacy'nin kelime cinsi etiketleme işlevselliğini kullanır. Bu bilgi, yazar tanımlama için bir özellik olarak kullanılabilir.

**9. N-gram Oluşturma:** Metin örneklerinden n-gramlar, n adet sözcüğün ardışık dizileri, oluşturulur. Bu adım, kelime eşzamanlılığı desenlerine ve daha yüksek düzeyde dil yapılarına ilişkin bilgiler sağlar.

**10. Stop Kelime Kaldırma:** Yaygın makaleler ve edatlar gibi stop kelimeler, metin örneklerinden kaldırılır. Bu adım, gürültünün giderilmesine ve daha anlamlı özelliklere odaklanmaya yardımcı olur.

**11. Özel Metin İşleme:** Özel metin işleme fonksiyonları, alfabeden olmayan karakterlerin kaldırılması ve özel özellik setlerinin oluşturulması gibi belirli gereksinimleri ele almak üzere uygulanır.

**12. Özellik Çıkarımı:** Metin örneklerinden belirli kelimelerin frekansı, sözdizimsel desenler ve yapısal özellikler gibi çeşitli dilbilimsel özellikler çıkarılır. Bu özellikler, yazar tanımlama modelleri için girdi olarak kullanılır.

**13. Model Eğitimi ve Değerlendirme:** Çıkarılan özellikler üzerinde Naive Bayes ve Destek Vektör Makineleri (SVM) gibi iki sınıflandırma modeli eğitilir. Modellerin performansını ölçmek için doğruluk puanları ve sınıflandırma raporları kullanılarak değerlendirilirler.

**14. Model Seçimi ve Optimizasyon:** SVM modeli için en iyi hiperparametreleri belirlemek için ızgara araması yapılır. F1 puanı en yüksek olan model, yazar tanımlama için final modeli olarak seçilir.

**15. Model Kalıcılığı:** Son seçilen model, joblib kütüphanesini kullanarak seri hale getirilir ve diske kaydedilir. Bu, daha sonra tekrar kullanım ve dağıtım için olanak sağlar.

### Kullanım
Bu projeyi kullanmak için, kod içinde belirtilen adımları takip edin. Gerekli bağımlılıkların yüklendiğinden ve veri kümesinin sağlanan bağlantıdan indirildiğinden emin olun. Kodu, farklı veri kümeleri veya belirli gereksinimler için gerektiği gibi ayarlayın.

> *Lütfen bu örnekte verilen kodun yalnızca gösterim amaçlı olduğunu ve belirli bir kullanım durumunuza veya veri kümenize uyacak şekilde değiştirilmesi gerekebileceğini unutmayın.*

### Sonuç
Metin analizi tekniklerini kullanarak yazar tanımlama, zorlu ancak ilginç bir görev olabilir. Doğal dil işleme ve makine öğrenimi gücünden yararlanarak, verilen bir metin örneğinin yazarını doğru bir şekilde tahmin edebilen modeller geliştirmek mümkündür. Bu proje, yazar tanımlama ve ilgili uygulamalar alanında daha fazla keşif ve geliştirme için bir temel sağlar.
