## English
## Multiclass Text Classification with Transformer

### What Is It Used For?
This project is designed for multi-class text classification task using Transformer model. Its main purpose is to classify text reviews into different categories. The model was built using TensorFlow and Keras and uses the powerful Transformer architecture for natural language processing tasks.

### What Does It Do?
This project can be used to automatically classify text reviews. For example, it can automatically categorize social media comments, product reviews, or customer feedback. Such text classification models are widely used to understand texts in large data sets, gain insights and facilitate data analysis.

### Use
Follow the steps below to run the code:

1. Make sure the required libraries (numpy, pandas, matplotlib, tensorflow, scikit-learn, tensorflow_datasets, seaborn) are installed (see "Requirements" above).

2. Prepare your dataset and make sure it is in the correct format (eg CSV, JSON).

3. Open the Python script and adapt the data file paths and configurations to your own dataset and preferences.

4. Run the script to preprocess the data, create and train the Transformer model.

5. After training, the model will be evaluated on the test dataset and the accuracy result will be displayed on the screen.

### Example Usage
You can use the trained model to classify text samples as follows:

examples = [
"We got a call from Yalova Terma City hotel through a phenomenon. You won a vacation...",
"My refrigerator, which I've been using for 5 years, started leaking out of the freezer...",
"We bought a tracksuit from Hepsiburada. It set off on January 18th and it looks like it was delivered..."
]

predictions = end_to_end_model.predict(examples)
for pred in predictions:
print(id_to_category[np.argmax(pred)])

### Customize
You can customize the code in various aspects to suit your specific needs. For example, you can change the architecture of the Transformer model, tune hyperparameters, or try different preprocessing techniques.

Feel free to use the code by experimenting and adapting it to your needs!

### Note
Please note that this is a simple application for basic text classification using the Transformer model. Depending on the complexity and size of your dataset, you may need to fine-tune the model or perform additional preprocessing steps for better performance.

### Thanks
The codes in this repository are inspired by various educational and online resources on natural language processing and Transformer models. Special thanks to the TensorFlow and Keras communities for providing valuable resources and tools for deep learning projects.


## Türkçe
## Transformer ile Çok Sınıflı Metin Sınıflandırma

### Ne İçin Kullanılır?
Bu proje, Transformer modelini kullanarak çoklu sınıf metin sınıflandırması görevi için tasarlanmıştır. Temel amacı, metin incelemelerini farklı kategorilere sınıflandırmaktır. Model, TensorFlow ve Keras kullanılarak oluşturulmuş olup, doğal dil işleme görevleri için güçlü olan Transformer mimarisini kullanır.

### Ne İşe Yarar?
Bu proje, metin incelemelerini otomatik olarak sınıflandırmak için kullanılabilir. Örnek olarak, sosyal medya yorumlarını, ürün incelemelerini veya müşteri geri bildirimlerini otomatik olarak kategorilere ayırabilir. Bu tür metin sınıflandırma modelleri, büyük veri setlerindeki metinleri anlamak, içgörüler elde etmek ve veri analizini kolaylaştırmak için yaygın olarak kullanılır.

### Kullanım
Kodu çalıştırmak için aşağıdaki adımları izleyin:

1. Gerekli kütüphanelerin (numpy, pandas, matplotlib, tensorflow, scikit-learn, tensorflow_datasets, seaborn) yüklü olduğundan emin olun (yukarıdaki "Gereksinimler" bölümüne bakın).

2. Veri kümenizi hazırlayın ve doğru biçimde olduğundan emin olun (ör. CSV, JSON).

3. Python betiğini açın ve veri dosya yollarını ve yapılandırmalarını kendi veri kümenize ve tercihlerinize uyarlayın.

4. Betiği çalıştırarak veriyi ön işleme, Transformer modelini oluşturma ve eğitme işlemlerini gerçekleştirin.

5. Eğitildikten sonra, model test veri kümesinde değerlendirilecek ve doğruluk sonucu ekranda gösterilecektir.

### Örnek Kullanım
Eğitilen modeli metin örneklerini sınıflandırmak için aşağıdaki gibi kullanabilirsiniz:

	examples = [
		"Bir fenomen aracılığı ile Yalova Terma City otel'den arandık. Tatil kazandınız...",
		"5 yıl kullandığım buzdolabım buzluktan şu akıtmaya başladı...",
		"Hepsiburada'dan esofman takimi aldık. 18 ocakta yola çıktı ve teslim edildi gözüküyor..."
	]

	predictions = end_to_end_model.predict(examples)
	for pred in predictions:
		print(id_to_category[np.argmax(pred)])

### Özelleştirme
Kodu, özel gereksinimlerinize uyacak şekilde çeşitli yönlerde özelleştirebilirsiniz. Örneğin, Transformer modelinin mimarisini değiştirebilir, hiperparametreleri ayarlayabilir veya farklı ön işleme teknikleri deneyebilirsiniz.

Kodu deneyimleyerek ve ihtiyaçlarınıza göre uyarlayarak kullanmaktan çekinmeyin!

### Not
Lütfen unutmayın ki bu, Transformer modelini kullanarak temel metin sınıflandırma için yapılmış basit bir uygulamadır. Veri kümenizin karmaşıklığına ve boyutuna bağlı olarak, modeli ince ayar yapmanız veya daha iyi performans için ek ön işleme adımları uygulamanız gerekebilir.

### Teşekkürler
Bu depodaki kodlar, doğal dil işleme ve Transformer modelleriyle ilgili çeşitli eğitim ve online kaynaklardan ilham alınarak oluşturulmuştur. TensorFlow ve Keras topluluklarına, derin öğrenme projeleri için değerli kaynaklar ve araçlar sağladıkları için özel teşekkürler.
