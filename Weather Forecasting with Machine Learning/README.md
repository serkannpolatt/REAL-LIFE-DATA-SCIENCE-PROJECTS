## English
## Weather Data Analysis and Visualization
This code provides functionalities for analyzing and visualizing weather data. It performs several tasks related to data processing, clustering, trend analysis, and forecasting. The code is written in Python and utilizes various libraries such as NumPy, Pandas, Plotly, and Scikit-learn.

### Features
1. Data Loading and Preprocessing:

	- The code reads weather data from a CSV file using Pandas.
	- It prepares the data for analysis by converting the format and sorting it based on the date.

2. Temperature Visualization:

	- The code visualizes the temperature data over time using Plotly.
	- It creates a line plot to show the temperature variations throughout the timeline.
	- The plot allows zooming and provides buttons for selecting different time ranges.

3. Clustering Analysis:

	- The code performs K-means clustering on the temperature data.
	- It calculates the sum of squared distances (SSE) for different numbers of clusters.
	- The SSE values are plotted to help determine the optimal number of clusters.
	- The temperature data is labeled based on the clustering results, and a scatter plot is generated to visualize the clusters.

4. Frequency Analysis:

	- The code generates a histogram to analyze the frequency distribution of temperature readings.
	- The histogram provides insights into the occurrence of different temperature ranges.

5. Seasonal Analysis:

	- The code calculates the seasonal mean temperatures by averaging specific months' data.
	- It visualizes the seasonal mean temperatures over the years using scatter plots with trendlines.
	- The scatter plots are grouped by season to compare the temperature trends.

6. Decision Tree Regression:

	- The code utilizes a Decision Tree Regressor to predict future temperature values.
	- It splits the data into training and testing sets, trains the model, and evaluates its performance using the R-squared metric.
	- The model is used to forecast temperature values for the next year.

7. Temperature Forecasting:

	- The code combines the forecasted temperature values with the original data.
	- It calculates the yearly mean temperature for each year, including the forecasted values.
	- A line plot is generated to visualize the forecasted temperature trend over time.

### Usage
1. Ensure that the required libraries (NumPy, Pandas, Plotly, Scikit-learn) are installed.
2. Prepare a CSV file named "Weather.csv" containing the weather data.
3. Execute the code step by step or as a whole to perform the desired analysis and visualization tasks.

Feel free to modify the code according to your specific requirements or adapt it to work with different datasets.

> *Note: The code assumes a specific structure and format of the weather data. Please ensure that your data matches the expected format or make necessary modifications to the code for compatibility.*

## Türkçe
## Hava Durumu Verisi Analizi ve Görselleştirme
Bu kod, hava durumu verilerinin analizi ve görselleştirilmesi için işlevsellik sağlar. Veri işleme, kümeleme, trend analizi ve tahminleme gibi çeşitli görevleri gerçekleştirir. Kod Python dilinde yazılmış olup, NumPy, Pandas, Plotly ve Scikit-learn gibi çeşitli kütüphanelerden yararlanır.

### Özellikler
1. Veri Yükleme ve Ön İşleme:

	- Kod, Pandas kullanarak CSV dosyasından hava durumu verilerini okur.
	- Veriyi analiz için uygun hale getirmek için formatını dönüştürür ve tarihe göre sıralar.

2. Sıcaklık Görselleştirme:

	- Kod, Plotly kullanarak zamana bağlı olarak sıcaklık verilerini görselleştirir.
	- Zaman çizelgesi boyunca sıcaklık değişimlerini gösteren bir çizgi grafiği oluşturur.
	- Grafiğe yakınlaşma imkanı sağlar ve farklı zaman aralıklarını seçmek için düğmeler sunar.

3. Kümeleme Analizi:

	- Kod, sıcaklık verileri üzerinde K-ortalama (K-means) kümeleme işlemi gerçekleştirir.
	- Farklı küme sayıları için kare hataların toplamını (SSE) hesaplar.
	- SSE değerlerini görselleştirerek optimal küme sayısını belirlemeye yardımcı olur.
	- Kümeleme sonuçlarına göre sıcaklık verileri etiketlenir ve kümeleme sonuçlarını görselleştirmek için bir scatter plot oluşturulur.

4. Frekans Analizi:

	- Kod, sıcaklık okumalarının frekans dağılımını analiz etmek için bir histogram oluşturur.
	- Histogram, farklı sıcaklık aralıklarının ne sıklıkla gerçekleştiğine dair bilgiler sağlar.

5. Mevsimsel Analiz:

	- Kod, belirli ayların verilerini ortalamayarak mevsimsel ortalama sıcaklıkları hesaplar.
	- Mevsimsel ortalama sıcaklıkları yıllara göre trend çizgileriyle scatter plot kullanarak görselleştirir.
	- Scatter plotlar, mevsimlere göre gruplandırılarak sıcaklık trendlerini karşılaştırmak için kullanılır.

6. Karar Ağacı Regresyonu:

	- Kod, gelecekteki sıcaklık değerlerini tahmin etmek için Karar Ağacı Regresyonu algoritmasını kullanır.
	- Veriyi eğitim ve test setlerine böler, modeli eğitir ve R-kare metriği kullanarak performansını değerlendirir.
	- Model, bir sonraki yıl için sıcaklık değerlerini tahmin etmek için kullanılır.

7. Sıcaklık Tahmini:

	- Kod, tahmin edilen sıcaklık değerlerini orijinal veriyle birleştirir.
	- Her yıl için, tahmin edilen değerler de dahil olmak üzere yıllık ortalama sıcaklık hesaplanır.
	- Sıcaklık trendini zaman içinde görselleştirmek için bir çizgi grafiği oluşturulur.
	
### Kullanım

1. Gerekli kütüphanelerin (NumPy, Pandas, Plotly, Scikit-learn) yüklü olduğundan emin olun.
2. "Weather.csv" adında hava durumu verilerini içeren bir CSV dosyası hazırlayın.
3. Kodu adım adım veya bir bütün olarak çalıştırarak istenen analiz ve görselleştirme işlemlerini gerçekleştirin.

Kodu, belirli gereksinimlerinize göre değiştirmekte veya farklı veri kümeleriyle çalışacak şekilde adapte etmekte özgürsünüz.

> *Not: Kod, hava durumu verilerinin belirli bir yapı ve formata sahip olduğunu varsayar. Lütfen verilerinizin beklenen formata uyduğundan emin olun veya uyumluluk için gerekli değişiklikleri yapın.*
