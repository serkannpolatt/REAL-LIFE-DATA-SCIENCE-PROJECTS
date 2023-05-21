## English
## Systemic Risk Model User Interface
This project is developed to create a user interface for a systemic risk model. This interface provides an interactive environment for users to analyze and visualize risks in the financial system.

### Features
- Loads the necessary data sets (df_exposures.csv, nodes.json, edges.json) for the systemic risk model.
- Offers various options to the user through menu selections:
	- Regulator layout selection
	- Financial system selection
	- Chart type selection (Transaction Relationships or Risk Graph)
- Visualizes the risk status of the financial system by updating the charts:
	 - Transaction Relationships graph: Shows the transaction relationships in the financial system.
	 - Risk Graph: Presents a network graph indicating the areas where the risk is concentrated.
- Displays certain measurements of systemic risk using bar charts with the Bqplot library:
	 - Chart illustrating the impact of collateralization on systemic risk
	 - Chart illustrating the impact of collateralization on systemic risk on a counterparty basis
	 - Chart displaying risk concentration

### Requirements
The following requirements are needed to run this project:

- Python 3.x
- Numpy
- Pandas
- Matplotlib
- Seaborn
- Bqplot
- Networkx
- VisJS2jupyter
- ipywidgets

### Installation
1.  Download the entire project to your computer.
2.  Install the required libraries using Anaconda or pip.
3.  Place the data sets (df_exposures.csv, nodes.json, edges.json) in the root directory of the project.

### Usage
1. Open the project files in a Python environment such as Anaconda or Jupyter Notebook.
2. Open the main.ipynb file.
3. Start the user interface by running all the cells sequentially.
4. Update the charts and measurements by making selections from the menu.

### Contributions
This project is open source and welcomes contributions. Please submit a pull request for any bug fixes, feature additions, or improvement suggestions.

### License
This project is licensed under the MIT License. For detailed information, please refer to the LICENSE file.

This README file describes the purpose, features, installation, usage, contribution policy, and license of the systemic risk model user interface. Anyone interested in the project can better understand and utilize it through this file.

## Türkçe
## Sistemik Risk Modeli Kullanıcı Arayüzü
Bu proje, bir sistemik risk modelinin kullanıcı arayüzünü oluşturmak için geliştirilmiştir. Bu arayüz, finansal sistemdeki riskleri analiz etmek ve görselleştirmek için kullanıcıya interaktif bir ortam sunmaktadır.

### Özellikler
- Sistemik risk modeli için gerekli veri setlerini (df_exposures.csv, nodes.json, edges.json) yükler.
- Menü seçenekleri aracılığıyla kullanıcıya çeşitli seçenekler sunar:
	- Düzenleyici düzen seçimi
	- Finansal sistem seçimi
	- Grafik türü seçimi (İşlem İlişkileri veya Risk Grafiği)
- Grafikleri güncelleyerek finansal sistemin risk durumunu görselleştirir:
	- İşlem İlişkileri grafiği: Finansal sisteme ait işlem ilişkilerini gösterir.
	- Risk Grafiği: Riskin odaklandığı bölgeleri gösteren bir ağ grafiği sunar.
- Bqplot kütüphanesini kullanarak sistemik riskin bazı ölçümlerini çubuk grafiklerle gösterir:
	- Kollateralizasyonun sistemik risk üzerindeki etkisini gösteren grafik
	- Kollateralizasyonun karşı taraf bazında sistematik risk üzerindeki etkisini gösteren grafik
	- Risk konsantrasyonunu gösteren grafik

### Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki gereksinimlere ihtiyaç vardır:

- Python 3.x
- Numpy
- Pandas
- Matplotlib
- Seaborn
- Bqplot
- Networkx
- VisJS2jupyter
- ipywidgets
- Kurulum
- Projenin tamamını bilgisayarınıza indirin.
- Anaconda veya pip aracılığıyla gerekli kütüphaneleri kurun.
- Veri setlerini (df_exposures.csv, nodes.json, edges.json) projenin kök dizinine yerleştirin.

### Kullanım
1. Anaconda veya Jupyter Notebook gibi bir Python ortamında proje dosyalarını açın.
2. main.ipynb dosyasını açın.
3. Tüm hücreleri sırasıyla çalıştırarak kullanıcı arayüzünü başlatın.
4. Menüden seçim yaparak grafikleri ve ölçümleri güncelleyebilirsiniz.

### Katkılar
Bu proje açık kaynaklıdır ve katkılara açıktır. Herhangi bir hata düzeltmesi, özellik eklemesi veya geliştirme önerisi için lütfen bir pull talebi gönderin.

### Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Detaylı bilgi için LICENSE dosyasını inceleyebilirsiniz.

Bu README dosyası, sistemik risk modeli kullanıcı arayüzünün amacını, özelliklerini, kurulumunu, kullanımını, katkıları kabul etme politikasını ve lisansını açıklamaktadır. Projeyle ilgilenen herkes, bu dosya aracılığıyla projeyi daha iyi anlayabilir ve kullanabilir.

![](https://i.imgur.com/Z1JUT5q.gif)


