import streamlit as stl 
stl.set_page_config(layout="wide")

stl.header("Veri Ön İşleme ve Özellik Mühendisliği")

stl.subheader("EDA Özet")
stl.write("""EDA'dan bazı önemli sonuçlar
          6 sütunda eksik değerler var
          Yükseklik sütunu Site EUI ile oldukça iyi bir korelasyona sahip (*)
          Sisli günlerde eksik değerler var, bunlar knnimputer kullanılarak doldurulmalı, diğer 3 sütundaki eksik değerler mod değerleri kullanılarak ve çoğu değer 1 olduğu için ele alınabilir
          Modelde gürültü oluşturabileceği için kategorik bir sütun olan tesis türü sütunu kaldırıldı
          110F üzerindeki günler de kaldırılabilir
        """)

stl.subheader("Eksik Değerlerin İşlenmesi")

stl.write("Veri setindeki eksik değerlerin yüzdesi")
stl.image("EDA_Plots/Missing_values.jpg")

stl.write("""İlk adım, önemli miktarda eksik değere sahip özellikleri (yüzde 50'den fazla eksik değere sahip olanları) kaldırmak ve geri kalanını veri doldurma teknikleriyle ele almak.
          Sayısal değerlere sahip özelliklerdeki eksik değerleri doldurmak için KNNImputer kullanabiliriz. KNNImputer, ilgili özelliklerdeki eğilimleri gözlemleyerek değerleri doldurur. Ancak değerlerin yüzde 50'den fazlası eksik olduğu için, veriye birçok gürültülü desen ekleyeceğiz. 
          Bu durumda özellikleri kaldırmak en iyi çözümdür
          
          \n 
          """)

stl.subheader("Eksik Değerleri Doldurma")
stl.write("""
          Kategorik değerlerin NULL değerlerini tahmin ederek dolduruyoruz. Eksik değerleri doldurmak için geri kalan modellere basit bir regresyon modeli oluşturulur. Bu yöntemle year_built ve energy_star_rating özelliklerini dolduruyoruz.  """)

# stl.subheader("Bazı Özellikleri Kaldırma")

stl.write("Gürültülü Özellikleri Kaldırma")
stl.write("""
        İlk adım olarak Özellikleri kaldırmak: Yıl Faktörü, Tesis Türü, 110 F üzerindeki Günler. \n
          Tesis türü sütunu, yüksek boyutluluğa sahip bir kategorik sütundur ve modelde gürültülü desenler oluşturabilir. \n
          Eğitim setindeki tüm veri örneklerinin Year Factor özelliği '7' değerine sahiptir, ancak eğitim setinde '7' değerine sahip hiçbir veri örneğimiz yok. \n
          Year Factor özelliğini kaldırıyoruz, çünkü bu anonimleştirilmiş bir özelliktir. Bu özelliği orijinal değerine eşleştirmenin bir yolu yoktur. Bu nedenle, year factor kullanıcı girişi bizim için kullanılamaz. Bu yüzden modelimiz için bunu kaldırıyoruz.
         """)


stl.subheader("Özellik Mühendisliği")
stl.subheader("Çoklu Kolineerlikle Başa Çıkma")
stl.write("""
Çoklu kolineerlik sorununu ele almak için yüksek korelasyona sahip özellikleri belirlemek ilk adımdır. Çoklu kolineerlik sorununu çözmek için Varyans İnflasyon Faktörü (VIF) kullanıyoruz. Bu şekilde, VIF değeri 4'ten büyük olan özellikleri belirliyoruz.
\n
Mevsim özellikleri birbirleriyle yüksek korelasyona sahiptir. Bu sütunları birleştirerek hem çoklu kolineerliği ele alırız hem de model için toplam özellik sayısını azaltırız, böylece tahmin uygulamasını kullanıcılar için daha basit hale getiririz.
Ocak_min_sıcaklık, şubat_min_sıcaklık, mart_min_sıcaklık, nisan_min_sıcaklık, ekim_min_sıcaklık, kasım_min_sıcaklık, aralık_min_sıcaklık özelliklerini ortalama kullanarak birleştirerek yeni bir özellik olan Avg_min_temp_winter'ı oluşturuyoruz.

Benzer şekilde, ocak_max_sıcaklık, şubat_max_sıcaklık, mart_max_sıcaklık, nisan_max_sıcaklık, ekim_max_sıcaklık, kasım_max_sıcaklık, aralık_max_sıcaklık özelliklerini birleştirerek yeni bir özellik olan Avg_max_temp_winter'ı oluşturuyoruz;
ocak_ort_sıcaklık, şubat_ort_sıcaklık, mart_ort_sıcaklık, nisan_ort_sıcaklık, ekim_ort_sıcaklık, kasım_ort_sıcaklık, aralık_ort_sıcaklık özelliklerini birleştirerek yeni bir özellik olan Avg_temp_winter'ı oluşturuyoruz;
mayıs_min_sıcaklık, haziran_min_sıcaklık, temmuz_min_sıcaklık, ağustos_min_sıcaklık, eylül_min_sıcaklık özelliklerini birleştirerek yeni bir özellik olan Avg_min_temp_summer'ı oluşturuyoruz;
mayıs_max_sıcaklık, haziran_max_sıcaklık, temmuz_max_sıcaklık, ağustos_max_sıcaklık, eylül_max_sıcaklık özelliklerini birleştirerek yeni bir özellik olan Avg_max_temp_summer'ı oluşturuyoruz;
mayıs_ort_sıcaklık, haziran_ort_sıcaklık, temmuz_ort_sıcaklık, ağustos_ort_sıcaklık, eylül_ort_sıcaklık özelliklerini birleştirerek yeni bir özellik olan Avg_temp_summer'ı oluşturuyoruz;
days_below_30F, days_below_20F, days_below_10F, days_below_0F özelliklerini birleştirerek yeni bir özellik olan Avg_days_below30F'ı oluşturuyoruz;
""")
stl.write("Sonunda, aşağıdaki özelliklere sahibiz modeli oluşturmak için:")
stl.write("(buraya özellikleri ekleyin)")
