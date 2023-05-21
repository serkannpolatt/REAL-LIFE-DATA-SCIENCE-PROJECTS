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

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/vsub21/systemic-risk-dashboard/master?filepath=systemic-risk-dashboard.ipynb)



