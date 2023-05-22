## English
## HR Dataset Analysis and Classification
This README provides an overview of the code's functionality without including the code itself. The code performs analysis and classification tasks on the HR dataset. Below is a step-by-step explanation of the code:

### Dependencies
- The code imports the pandas library and assigns it the alias 'pd' to work with data structures.
- Other libraries used later in the code are imported as needed.

### Dataset Loading
- The HR dataset is loaded from a CSV file named 'hr.csv' using the pd.read_csv() function.
- The column names of the dataset are extracted and stored in the list 'col_names'.

### Dataset Exploration
- The code prints the column names using the print() function.
- The first few rows of the dataset are displayed using the head() function.

### Column Renaming
- The code renames the column 'sales' to 'department' using the rename() function.

### Data Preprocessing
- Categorical variables 'department' and 'salary' are one-hot encoded using the pd.get_dummies() function.
- The encoded variables are joined with the original dataset.
- Two unnecessary columns (index 8 and 9) are dropped from the dataset.


### Feature Selection
- The code prepares the dataset for classification by separating the target variable ('left') from the independent variables.
- The features to be used for classification are stored in the list 'X', excluding the target variable.
- The target variable is stored in the list 'y'.

### Logistic Regression Model
- A logistic regression model is created using the LogisticRegression class from scikit-learn.
- The model is trained on the training data using the fit() function.
- Logistic Regression Model Evaluation
- The code calculates and prints the accuracy of the logistic regression model using the accuracy_score() function from scikit-learn.

### Random Forest Model
- A random forest classifier is created using the RandomForestClassifier class from scikit-learn.
- The model is trained on the training data using the fit() function.

### Random Forest Model Evaluation
- The code calculates and prints the accuracy of the random forest model using the accuracy_score() function from scikit-learn.

### Classification Report
- The code generates and prints a classification report using the classification_report() function from scikit-learn.
- The report includes precision, recall, F1-score, and support for each class.

### Confusion Matrix and Heatmap
- The code generates a confusion matrix using the confusion_matrix() function from scikit-learn.
- The confusion matrix is visualized as a heatmap using the seaborn and matplotlib libraries.
- Separate heatmaps are created for the random forest and logistic regression models.

### Receiver Operating Characteristic (ROC) Curve
- The code calculates the ROC AUC (Area Under the Curve) score for the logistic regression and random forest models.
- The ROC curve is plotted using the roc_curve() function from scikit-learn and visualized with matplotlib.

### Feature Importance
- The code calculates the feature importance using the feature_importances_ attribute of the random forest model.
- The importance values are sorted, and the feature labels are printed along with their respective importance percentages.

This code provides an analysis of the HR dataset and demonstrates the use of logistic regression and random forest models for classification tasks.

## Türkçe
## İnsan Kaynakları (HR) Veri Kümesi Analizi ve Sınıflandırma
Bu README, kodun işlevselliğine ilişkin bir genel bakış sunar, ancak kodu kendisi içermez. Kod, İnsan Kaynakları (HR) veri kümesinde analiz ve sınıflandırma görevleri gerçekleştirir. Aşağıda kodun adım adım açıklaması yer almaktadır:

### Bağımlılıklar
- Kod, veri yapılarıyla çalışmak için pandas kütüphanesini içe aktarır ve 'pd' takma adını atar.
- Kodun daha sonra ihtiyaç duyulan diğer kütüphaneler içe aktarılır.

### Veri Kümesi Yükleme
- HR veri kümesi, 'hr.csv' adlı bir CSV dosyasından pd.read_csv() fonksiyonu kullanılarak yüklenir.
- Veri kümesinin sütun adları çıkarılır ve 'col_names' listesinde saklanır.

### Veri Kümesi Keşfi
- Kod, print() fonksiyonunu kullanarak sütun adlarını yazdırır.
- Veri kümesinin ilk birkaç satırı, head() fonksiyonu kullanılarak görüntülenir.

### Sütun Adlarının Yeniden Adlandırılması
- Kod, sütunu 'sales' olanı 'department' olarak yeniden adlandırır, bunun için rename() fonksiyonunu kullanır.

### Veri Ön İşleme
- Kategorik değişkenler 'department' ve 'salary', pd.get_dummies() fonksiyonu kullanılarak bir-hot kodlanır.
- Kodlanmış değişkenler, orijinal veri kümesine eklenir.
- Veri kümesinden gereksiz iki sütun (8. ve 9. sütunlar) çıkarılır.

### Özellik Seçimi
- Kod, sınıflandırma için veri kümesini hedef değişken ('left') ile bağımsız değişkenlere ayırarak sınıflandırmaya hazırlar.
- Sınıflandırmada kullanılacak özellikler 'X' listesinde saklanır (hedef değişken hariç).
- Hedef değişken 'y' listesinde saklanır.

### Lojistik Regresyon Modeli
- scikit-learn'den LogisticRegression sınıfını kullanarak bir lojistik regresyon modeli oluşturulur.
- Model, fit() fonksiyonunu kullanarak eğitim verilerinde eğitilir.

### Lojistik Regresyon Modeli Değerlendirmesi
- Kod, scikit-learn'deki accuracy_score() fonksiyonunu kullanarak lojistik regresyon modelinin doğruluk değerini hesaplar ve yazdırır.

### Rastgele Orman Modeli
- scikit-learn'den RandomForestClassifier sınıfını kullanarak bir rastgele orman sınıflandırıcısı oluşturulur.
- Model, fit() fonksiyonunu kullanarak eğitim verilerinde eğitilir.

### Rastgele Orman Modeli Değerlendirmesi
- Kod, scikit-learn'deki accuracy_score() fonksiyonunu kullanarak rastgele orman modelinin doğruluk değerini hesaplar ve yazdırır.

### Sınıflandırma Raporu
- Kod, scikit-learn'deki classification_report() fonksiyonunu kullanarak bir sınıflandırma raporu oluşturur ve yazdırır.
- Rapor, her sınıf için hassasiyet (precision), duyarlılık (recall), F1-skoru ve destek (support) içerir.

### Karışıklık Matrisi ve Isı Haritası
- Kod, scikit-learn'deki confusion_matrix() fonksiyonunu kullanarak bir karışıklık matrisi oluşturur.
- Karışıklık matrisi, seaborn ve matplotlib kütüphaneleri kullanılarak bir ısı haritası olarak görselleştirilir.
- Rastgele orman ve lojistik regresyon modelleri için ayrı ayrı ısı haritaları oluşturulur.

### Alıcı İşletim Karakteristiği (ROC) Eğrisi
- Kod, lojistik regresyon ve rastgele orman modelleri için ROC AUC (Alan Altındaki Eğri) skorunu hesaplar.
- ROC eğrisi, scikit-learn'deki roc_curve() fonksiyonu kullanılarak çizilir ve matplotlib ile görselleştirilir.

### Özellik Önemi
- Kod, rastgele orman modelinin feature_importances_ özelliğini kullanarak özellik önemini hesaplar.
- Önem değerleri sıralanır ve özellik etiketleri, ilgili önem yüzdeleriyle birlikte yazdırılır.

Bu kod, İnsan Kaynakları (HR) veri kümesinin analizini sağlar ve sınıflandırma görevleri için lojistik regresyon ve rastgele orman modellerinin kullanımını gösterir.
