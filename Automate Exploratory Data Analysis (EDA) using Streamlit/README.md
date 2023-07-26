## English 
## Automate Exploratory Data Analysis (EDA) using Streamlit
This Python script is designed to create a web app using Streamlit to automate the Exploratory Data Analysis (EDA) process for a given CSV dataset. The app allows users to upload a CSV file containing both continuous and categorical columns. Once the file is uploaded, the app provides various charts, statistics, and insights to understand the dataset better.

### Dependencies
- **streamlit:** The app is built using Streamlit, a Python library for creating interactive web apps for data science and machine learning.
- **pandas:** Used for data manipulation and analysis, providing data structures like DataFrame to handle tabular data.
- **numpy:** A fundamental package for scientific computing with Python.
- **collections.Counter:** Used to count the occurrences of elements in the dataset.
- **matplotlib.pyplot**: Used for creating correlation charts.
- **pandas_bokeh:** Enables Bokeh plotting with Pandas data structures.
- **missingno:** A library to visualize missing data.

### Functions

1. **create_correlation_chart(corr_df):** Creates a correlation chart using Matplotlib for a given correlation DataFrame corr_df. It displays the correlation values as colors with text annotations for each cell.

2. **create_missing_values_bar(df):** Creates a missing values distribution bar chart using Matplotlib for a given DataFrame df. It displays the missing values count for each column.

3. **find_cat_cont_columns(df):** Logic to separate continuous and categorical columns from a given DataFrame df. It identifies columns based on the number of unique values or the data type (less than or equal to 25 unique values or of object type).

### Web App Overview
The Streamlit app provides a user interface to upload a CSV file. Upon uploading the file, it displays three tabs for the following functionalities:

1. **Dataset Overview:** Displays the uploaded dataset, dataset statistics, a correlation chart, and a bar chart representing missing values.

2. **Individual Column Stats:** Provides the ability to analyze individual continuous and categorical columns. For continuous columns, it displays statistics like count, mean, standard deviation, minimum, maximum, and quantiles along with a histogram. For categorical columns, it shows a bar chart with value counts.

3. **Explore Relation Between Features:** Allows users to explore the relationship between two continuous columns using a scatter plot. Users can choose X-axis, Y-axis, and optionally color-encode the points based on a categorical column.

### How to Use

1. Install the required dependencies using pip install streamlit pandas numpy matplotlib pandas_bokeh missingno.
2. Save the script in a file named python_eda_app.py.
3. Run the app using the command streamlit run python_eda_app.py in the terminal.
4. The web app will open in a browser window. Upload a CSV file with both continuous and categorical columns to explore the dataset.

> **Note: Please ensure that your CSV file meets the requirements and has valid data. The app is designed to handle reasonable-sized datasets and may not be suitable for extremely large datasets.**



## Türkçe
## Streamlit kullanarak Keşifsel Veri Analizini (EDA) Otomatikleştirin
Bu Python betiği, belirli bir CSV veri kümesi için Keşif Veri Analizi (EDA) sürecini otomatikleştirmek üzere Streamlit'i kullanarak bir web uygulaması oluşturmak üzere tasarlanmıştır. Uygulama, kullanıcıların hem sürekli hem de kategorik sütunlar içeren bir CSV dosyası yüklemesine olanak tanır. Dosya yüklendikten sonra uygulama, veri kümesini daha iyi anlamak için çeşitli grafikler, istatistikler ve içgörüler sağlar.

### Bağımlılıklar
- **streamlit:** Uygulama, veri bilimi ve makine öğrenimi için etkileşimli web uygulamaları oluşturmaya yönelik bir Python kitaplığı olan Streamlit kullanılarak oluşturulmuştur.
- **pandalar:** Tablo verilerini işlemek için DataFrame gibi veri yapıları sağlayarak veri manipülasyonu ve analizi için kullanılır.
- **numpy:** Python ile bilimsel bilgi işlem için temel bir paket.
- **collections.Counter:** Veri kümesindeki öğelerin tekrarını saymak için kullanılır.
- **matplotlib.pyplot**: Korelasyon çizelgeleri oluşturmak için kullanılır.
- **pandas_bokeh:** Pandas veri yapılarıyla Bokeh çizimini etkinleştirir.
- **eksik yok:** Eksik verileri görselleştirmek için bir kitaplık.

### İşlevler

1. **create_correlation_chart(corr_df):** Belirli bir DataFrame corr_df korelasyonu için Matplotlib kullanarak bir korelasyon grafiği oluşturur. Korelasyon değerlerini, her hücre için metin ek açıklamalarıyla renkler olarak görüntüler.

2. **create_missing_values_bar(df):** Belirli bir DataFrame df için Matplotlib kullanarak bir eksik değerler dağıtım çubuğu grafiği oluşturur. Her sütun için eksik değerlerin sayısını görüntüler.

3. **find_cat_cont_columns(df):** Sürekli ve kategorik sütunları belirli bir DataFrame df'den ayırma mantığı. Benzersiz değerlerin sayısına veya veri türüne (25 benzersiz değerden veya nesne türünden küçük veya eşit) dayalı olarak sütunları tanımlar.

### Web Uygulamasına Genel Bakış
Streamlit uygulaması, bir CSV dosyası yüklemek için bir kullanıcı arabirimi sağlar. Dosyayı yükledikten sonra, aşağıdaki işlevler için üç sekme görüntüler:

1. **Veri Kümesine Genel Bakış:** Yüklenen veri kümesini, veri kümesi istatistiklerini, bir korelasyon grafiğini ve eksik değerleri temsil eden bir çubuk grafiği görüntüler.

2. **Bireysel Sütun İstatistikleri:** Tek tek sürekli ve kategorik sütunları analiz etme yeteneği sağlar. Sürekli sütunlar için sayım, ortalama, standart sapma, minimum, maksimum ve nicelikler gibi istatistikleri bir histogramla birlikte görüntüler. Kategorik sütunlar için değer sayımları içeren bir çubuk grafik gösterir.

3. **Özellikler Arasındaki İlişkiyi Keşfedin:** Kullanıcıların bir dağılım grafiği kullanarak iki sürekli sütun arasındaki ilişkiyi keşfetmesine olanak tanır. Kullanıcılar, X eksenini, Y eksenini seçebilir ve isteğe bağlı olarak kategorik bir sütuna göre noktaları renkli olarak kodlayabilir.

### Nasıl kullanılır

1. pip install streamlit pandas numpy matplotlib pandas_bokeh missno kullanarak gerekli bağımlılıkları kurun.
2. Komut dosyasını python_eda_app.py adlı bir dosyaya kaydedin.
3. Terminalde streamlit run python_eda_app.py komutunu kullanarak uygulamayı çalıştırın.
4. Web uygulaması bir tarayıcı penceresinde açılacaktır. Veri kümesini keşfetmek için hem sürekli hem de kategorik sütunlar içeren bir CSV dosyası yükleyin.

> **Not: Lütfen CSV dosyanızın gereksinimleri karşıladığından ve geçerli verilere sahip olduğundan emin olun. Uygulama, makul boyutlu veri kümelerini işlemek üzere tasarlanmıştır ve çok büyük veri kümeleri için uygun olmayabilir.**