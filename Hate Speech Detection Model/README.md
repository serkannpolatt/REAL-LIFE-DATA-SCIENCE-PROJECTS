## English
## Hate Speech Detection Model
This project aims to provide an overview of the steps involved in text data preprocessing and classification using a machine learning model.

### Project Description
The main objective of this project is to demonstrate how to clean and preprocess text data, handle imbalanced datasets, and train a classification model for sentiment analysis.

### Steps Involved
**1. Loading the Data**
The project begins by loading the training and test datasets using the pandas library.

**2. Text Cleaning**
Text cleaning is performed to remove unnecessary characters and standardize the text for further analysis. This step involves converting the text to lowercase, removing special characters, URLs, and usernames. The cleaning process ensures that the text data is uniform and ready for analysis.

**3. Handling Imbalanced Datasets**
Imbalanced datasets, where one class has significantly fewer samples than the other, can affect the performance of classification models. To address this issue, upsampling the minority class is applied. This involves creating additional samples from the minority class to balance the dataset, ensuring that the model can learn from both classes effectively.

**4. Text Vectorization and Classification Model**
Text vectorization is performed to convert the text data into numerical representations suitable for machine learning algorithms. This step involves creating a pipeline that combines the CountVectorizer and TfidfTransformer methods to convert the text into a matrix of TF-IDF features. Finally, a classification model, such as the SGDClassifier, is trained on the preprocessed data to classify sentiment.

**5. Evaluation**
The trained model is used to predict the sentiment of the test data. The performance of the model is evaluated using the F1-score, which provides a measure of the model's accuracy in classifying both positive and negative sentiments.

> Please note that the code snippets provided in this README are for reference purposes only and may need to be adapted to your specific project requirements.**


## Türkçe
## Nefret Söylemi Algılama Modeli
Bu proje, metin verilerinin önişleme ve sınıflandırma adımlarını kullanarak bir makine öğrenme modeliyle nasıl işlendiğine dair bir genel bakış sunmayı amaçlamaktadır.

### Proje Açıklaması
Bu projenin temel amacı, metin verilerini temizlemeyi, önişlemeyi ve dengesiz veri kümelerini yönetmeyi ve duygu analizi için bir sınıflandırma modeli eğitmeyi göstermektir.

### İzlenen Adımlar
**1. Verilerin Yüklenmesi**
Proje, eğitim ve test veri kümelerinin pandas kütüphanesi kullanılarak yüklenmesiyle başlar.

**2. Metin Temizleme**
Metin temizleme işlemi, gereksiz karakterleri kaldırmak ve metni daha fazla analiz için standart hale getirmek amacıyla yapılır. Bu adım, metni küçük harfe dönüştürme, özel karakterleri, URL'leri ve kullanıcı adlarını kaldırma işlemini içerir. Temizleme süreci, metin verilerinin homojen ve analiz için hazır hale getirilmesini sağlar.

**3. Dengesiz Veri Kümelerinin Yönetimi**
Bir sınıfın diğerinden önemli ölçüde daha az örneğe sahip olduğu dengesiz veri kümeleri, sınıflandırma modellerinin performansını etkileyebilir. Bu sorunu çözmek için azınlık sınıfını yükseltme işlemi uygulanır. Bu, azınlık sınıfından ek örnekler oluşturarak veri kümesini dengelemeyi ve modelin her iki sınıftan da etkili bir şekilde öğrenmesini sağlamayı içerir.

**4. Metin Vektörleme ve Sınıflandırma Modeli**
Metin vektörleme, metin verilerini makine öğrenimi algoritmaları için uygun sayısal temsillere dönüştürmek için yapılır. Bu adım, metni TF-IDF özelliklerinin bir matrisine dönüştürmek için CountVectorizer ve TfidfTransformer yöntemlerini birleştiren bir iş akışı oluşturmayı içerir. Son olarak, SGDClassifier gibi bir sınıflandırma modeli, önişlenmiş veri üzerinde eğitilerek duygu sınıflandırması yapılır.

**5. Değerlendirme**
Eğitilmiş model, test verilerinin duygusunu tahmin etmek için kullanılır. Modelin performansı, hem pozitif hem de negatif duyguları sınıflandırmada modelin doğruluğunu ölçen F1 skoru kullanılarak değerlendirilir.

> *Lütfen bu README'de sağlanan kod örneklerinin yalnızca referans amaçlı olduğunu ve projenizin özel gereksinimlerine göre uyarlanması gerekebileceğini unutmayın.*
