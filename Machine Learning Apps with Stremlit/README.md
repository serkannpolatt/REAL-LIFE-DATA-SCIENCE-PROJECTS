## English
## CIFAR-10 Web Classifier
This project implements a CIFAR-10 image classifier using TensorFlow and Streamlit. It consists of two main parts: model training and a web application.

### Model Training
The model training section trains a convolutional neural network (CNN) using the CIFAR-10 dataset. It performs the following steps:

1. **Dataset Loading:** The CIFAR-10 dataset is loaded using TensorFlow's cifar10.load_data() function.

2. **Data Preprocessing:** The pixel values of the images are normalized to the range [0, 1].

3. **Label Preprocessing:** The labels are one-hot encoded using TensorFlow's to_categorical() function.

4. **Model Architecture:** A CNN model is created using the Sequential API from Keras. It consists of convolutional layers with ReLU activation, max pooling layers, and fully connected layers. The final layer uses softmax activation for multi-class classification.

5. **Model Compilation:** The model is compiled with categorical cross-entropy loss, the Adam optimizer, and accuracy as the evaluation metric.

6. **Model Training:** The model is trained on the training data for 10 epochs with a batch size of 64. The validation data is used for model evaluation during training.

7. **Model Saving:** The trained model is saved to a file named "cifar10_model_2.h5".

### Web Application
The web application allows users to upload an image and make predictions using the trained model. It follows these steps:

1. **User Interface:** The web application displays a title and a description. It provides a file uploader for users to upload an image.

2. **Image Processing:** The uploaded image is processed and resized to 32x32 pixels. It is converted to a NumPy array and normalized to have values between 0 and 1.

2. **Model Loading:** The saved model file "cifar10_model_2.h5" is loaded using the h5py library. The model is loaded using TensorFlow's tf.keras.models.load_model() function.

4. **Prediction:** The loaded model predicts the class probabilities for the uploaded image.

5. **Visualization:** The predicted probabilities are visualized using a horizontal bar chart. The chart displays the probability values for each CIFAR-10 class.

By running the web application, users can upload an image and see the predicted probabilities for each CIFAR-10 class.

## Türkçe
## CIFAR-10 Web Sınıflandırıcı
Bu proje, TensorFlow ve Streamlit kullanan bir CIFAR-10 görüntü sınıflandırıcısı uygular. Model eğitimi ve web uygulaması olmak üzere iki ana bölümden oluşur.

### Model Eğitimi
Model eğitimi bölümü, CIFAR-10 veri setini kullanarak evrişimli bir sinir ağını (CNN) eğitir. Aşağıdaki adımları gerçekleştirir:

1. **Veri Kümesi Yükleme:** CIFAR-10 veri kümesi, TensorFlow'un cifar10.load_data() işlevi kullanılarak yüklenir.

2. **Veri Ön İşleme:** Görüntülerin piksel değerleri [0, 1] aralığına normalleştirilir.

3. **Etiket Ön İşleme:** Etiketler, TensorFlow'un to_categorical() işlevi kullanılarak tek seferde kodlanır.

4. **Model Mimarisi:** Keras'tan Sequential API kullanılarak bir CNN modeli oluşturulur. ReLU etkinleştirmeli evrişimli katmanlardan, maksimum havuzlama katmanlarından ve tamamen bağlı katmanlardan oluşur. Son katman, çok sınıflı sınıflandırma için softmax aktivasyonunu kullanır.

5. **Model Derleme:** Model, kategorik çapraz entropi kaybı, Adam iyileştirici ve değerlendirme ölçütü olarak doğrulukla derlenir.

6. **Model Eğitimi:** Model, parti boyutu 64 olan 10 dönemlik eğitim verileri üzerinde eğitilir. Doğrulama verileri, eğitim sırasında model değerlendirmesi için kullanılır.

7. **Model Kaydetme:** Eğitilen model "cifar10_model_2.h5" adlı bir dosyaya kaydedilir.

### Web Uygulaması
Web uygulaması, kullanıcıların eğitimli modeli kullanarak bir görüntü yüklemesine ve tahminler yapmasına olanak tanır. Şu adımları takip eder:

1. **Kullanıcı Arayüzü:** Web uygulaması bir başlık ve açıklama görüntüler. Kullanıcıların bir resim yüklemesi için bir dosya yükleyici sağlar.

2. **Görüntü İşleme:** Yüklenen görüntü işlenir ve 32x32 piksel olarak yeniden boyutlandırılır. Bir NumPy dizisine dönüştürülür ve 0 ile 1 arasında değerlere sahip olacak şekilde normalleştirilir.

2. **Model Yükleme:** Kaydedilen "cifar10_model_2.h5" model dosyası, h5py kitaplığı kullanılarak yüklenir. Model, TensorFlow'un tf.keras.models.load_model() işlevi kullanılarak yüklenir.

4. **Tahmin:** Yüklenen model, yüklenen görüntü için sınıf olasılıklarını tahmin eder.

5. **Görselleştirme:** Öngörülen olasılıklar, yatay bir çubuk grafik kullanılarak görselleştirilir. Grafik, her bir CIFAR-10 sınıfı için olasılık değerlerini gösterir.

Web uygulamasını çalıştırarak, kullanıcılar bir resim yükleyebilir ve her bir CIFAR-10 sınıfı için tahmin edilen olasılıkları görebilir.