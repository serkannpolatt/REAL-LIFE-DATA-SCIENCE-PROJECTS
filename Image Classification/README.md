## English
## Image Classification

This README provides an overview of the project, its objectives, and the steps involved. The project involves building an image classifier using a Convolutional Neural Network (CNN) architecture.

### Project Description
The main goal of this project is to develop an image classifier that can classify images into two classes: "Happy" and "Sad". The classifier will be trained on a dataset of images and will learn to distinguish between happy and sad expressions in images.

### Steps Involved
1. Preprocessing:
	- The code begins by setting up the GPU devices and enabling memory growth.
	- It checks for valid image extensions and removes images with unsupported extensions.
	- The dataset directory and image extensions are defined.

2. Loading and Visualizing the Dataset:
	- The code uses the tf.keras.utils.image_dataset_from_directory function to load the dataset from the specified directory.
	- It visualizes a sample of images from the dataset using matplotlib.

3. Splitting the Dataset:
	- The code splits the dataset into training, validation, and test sets.
	- The sizes of the splits are defined based on percentages of the total dataset.

4. Building the Model:
	- The code builds a CNN model using the Sequential API from TensorFlow.
	- The model consists of multiple Convolutional, MaxPooling, Flatten, and Dense layers.
	- The model is compiled with the Adam optimizer, binary cross-entropy loss function, and accuracy as the evaluation metric.

5. Training the Model:
	- The code trains the model using the training and validation datasets.
	- It uses the fit function and specifies the number of epochs for training.
	- During training, the model's performance metrics are logged for visualization.

6. Evaluating the Model:
	- The code visualizes the loss and accuracy metrics of the trained model using matplotlib.
	- It uses the test dataset to evaluate the model's performance and computes precision, recall, and binary accuracy metrics.

7. Making Predictions:
	- The code demonstrates making predictions on a single image.
	- An example image is loaded, resized, and fed into the trained model for prediction.
	- The predicted class (happy or sad) is printed based on the prediction probability.

8. Saving and Loading the Model:
	- The code saves the trained model in the "models" directory.
	- The model is saved in HDF5 format using the save function.
	- Additionally, it demonstrates loading the saved model from the file and making predictions using the loaded model.



## Türkçe
## Görüntü Sınıflandırma
Bu README, projenin genel bir bakışını, hedeflerini ve içeren adımları sağlar. Bu proje, Evrişimli Sinir Ağı (CNN) mimarisi kullanarak bir görüntü sınıflandırıcısı oluşturmayı içerir.

### Proje Tanımı
Bu projenin temel amacı, görüntüleri "Mutlu" ve "Üzgün" olmak üzere iki sınıfa sınıflandırabilen bir görüntü sınıflandırıcısı geliştirmektir. Sınıflandırıcı, bir görüntü veri seti üzerinde eğitilecek ve görüntülerdeki mutlu ve üzgün ifadeleri ayırt etmeyi öğrenecektir.

### İçerilen Adımlar

1. Önişleme:
	- Kod, GPU cihazlarını yapılandırarak ve bellek büyümesini etkinleştirerek başlar.
	- Desteklenmeyen uzantılara sahip olan görüntüleri kontrol eder ve kaldırır.
	- Veri seti dizini ve görüntü uzantıları tanımlanır.

2. Veri Setinin Yüklenmesi ve Görselleştirilmesi:
	- Kod, tf.keras.utils.image_dataset_from_directory fonksiyonunu kullanarak veri setini belirtilen dizinden yükler.
	- Veri setinden örnek görüntülerin görselleştirilmesi için matplotlib kullanılır.

3. Veri Setinin Bölünmesi:
	- Kod, veri setini eğitim, doğrulama ve test kümelerine böler.
	- Bölünmüş kümelerin boyutları toplam veri setinin yüzdelikleri temel alınarak tanımlanır.

4. Modelin Oluşturulması:
	- Kod, TensorFlow'dan Sequential API kullanarak bir CNN modeli oluşturur.
	- Model, birden çok Evrişimli, MaxPooling, Flatten ve Dense katmanlarından oluşur.
	- Model, Adam optimizer, ikili çapraz entropi kaybı fonksiyonu ve doğruluk metriği ile derlenir.

5. Modelin Eğitilmesi:
	- Kod, eğitim ve doğrulama veri kümelerini kullanarak modeli eğitir.
	- fit fonksiyonunu kullanır ve eğitim için epoch sayısını belirtir.
	- Eğitim sırasında, modelin performans metrikleri görselleştirme için kaydedilir.

6. Modelin Değerlendirilmesi:
	- Kod, eğitilmiş modelin kayıp ve doğruluk metriklerini matplotlib kullanarak görselleştirir.
	- Modelin performansını değerlendirmek için test veri seti kullanılır ve hassasiyet, geri çağırma ve ikili doğruluk metrikleri hesaplanır.

7. Tahminlerin Yapılması:
	- Kod, tek bir görüntü üzerinde tahmin yapmayı gösterir.
	- Bir örnek görüntü yüklenir, yeniden boyutlandırılır ve eğitilmiş modele tahmin için verilir.
	- Tahmin olasılığına bağlı olarak, tahmin edilen sınıf (mutlu veya üzgün) yazdırılır.

8. Modelin Kaydedilmesi ve Yüklenmesi:
	- Kod, eğitilmiş modeli "models" dizinine kaydeder.
	- Model, save fonksiyonunu kullanarak HDF5 formatında kaydedilir.
	- Ayrıca, kaydedilen modelin dosyadan yüklenmesini ve yüklenen model kullanılarak tahmin yapmayı gösterir.
