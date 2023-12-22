import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('**Veri Toplama**')

st.write("""
    Veri seti [WiDS Datathon 2022](https://www.kaggle.com/competitions/widsdatathon2022) tarafından sağlanmış olup 100 binden fazla veri örneği içermektedir.
""")

st.subheader('Arka Plan')
st.write("""
    Uluslararası Enerji Ajansı (IEA) tarafından yayınlanan bir rapora göre, 2020 yılında binaların inşasından yıkımına kadar olan yaşam döngüleri, küresel enerjiye dayalı ve süreçe dayalı CO2 emisyonlarının %37'sinden sorumludur. Ancak binaların enerji tüketimini kolay uygulanabilir düzeltmeler ve son teknoloji stratejilerin bir kombinasyonuyla önemli ölçüde azaltmak mümkündür. Örneğin, retrofitleme yapılan binaların ısıtma ve soğutma enerji ihtiyaçları %50-90 oranında azaltılabilir. Bu enerji verimliliği önlemlerinin birçoğu aynı zamanda genel maliyet tasarrufları sağlar ve kullanıcılar için daha temiz hava gibi diğer faydalar elde edilmesini sağlar. Enerji tüketimini doğru bir şekilde tahmin etmek, politika yapıcıların emisyon azaltma çabalarını en üst düzeye çıkarmak için retrofit çalışmalarını hedeflemesine yardımcı olabilir.
""")

st.subheader('Genel Bakış: Veri Seti ve İş')
st.write("""
    WiDS Datathon veri seti, Climate Change AI (CCAI) ve Lawrence Berkeley National Laboratory (Berkeley Lab) ile işbirliği içinde oluşturulmuştur. WiDS Datathon katılımcıları, bina enerji verimliliğindeki farklılıkları analiz ederek, bina enerji tüketimini tahmin etmek için modeller oluşturacaklardır. Katılımcılar, binaların bulunduğu bölgeler için bina özelliklerini ve iklim ve hava durumu değişkenlerini tanımlayan bir veri seti kullanacaklardır. Enerji tüketiminin doğru bir şekilde tahmin edilmesi, politika yapıcıların emisyon azaltma çabalarını maksimize etmek için retrofit çalışmalarını hedeflemelerine yardımcı olabilir.
""")

st.subheader('Bağımlı Değişken')
st.write("""
    Site Enerji Yoğunluğu (Site EUI), tahmin etmeye çalıştığımız bağımlı değişkendir.
    
    Site enerji yoğunluğu, herhangi bir binanın enerji kullanımını anlamak ve enerji verimliliği için fırsatları belirlemek için önemli bir ölçüttür. Aynı zamanda binanın genel CO2 emisyonları hakkında bir gösterge sunar ve emisyonları kontrol etmemize yardımcı olur.

    Site EUI, bir binanın enerji yoğunluğunun binanın büyüklüğüne bağlı olduğu bir ölçüttür. Site EUI, binanın çeşitli özelliklerine ve binanın bulunduğu yerin hava koşullarına bağlıdır. Bu makalede, makine öğrenimi tekniklerini kullanarak site EUI'yi tahmin etmek için bir veri bilimi çözümü geliştireceğiz ve ardından modeli çıkarım için bir bulut platformuna dağıtacağız.
""")

st.subheader('Bağımsız Değişkenler')
st.write("""
    id: bina kimliği\n
    Year_Factor: hava ve enerji kullanım faktörlerinin gözlendiği anonimleştirilmiş bir yıl\n
    State_Factor: bina konumunun anonimleştirilmiş bir eyaleti\n
    building_class: bina sınıflandırması\n
    facility_type: bina kullanım türü\n
    floor_area: binanın kat alanı (kare fit cinsinden)\n
    year_built: bina inşa edildiği yıl\n
    energy_star_rating: binanın enerji yıldız derecesi\n
    ELEVATION: bina konumunun yüksekliği\n
    january_min_temp: binanın bulunduğu yerde Ocak ayındaki minimum sıcaklık (Fahrenheit cinsinden)\n
    january_avg_temp: binanın bulunduğu yerde Ocak ayındaki ortalama sıcaklık (Fahrenheit cinsinden)\n
    january_max_temp: binanın bulunduğu yerde Ocak ayındaki maksimum sıcaklık (Fahrenheit cinsinden)\n
    cooling_degree_days: verilen bir günde ortalama sıcaklık 65 Fahrenheit derecenin üzerindeyse soğutma derece günü. Her ay, binanın bulunduğu yerdeki toplam yılı oluşturmak için toplanır.\n
    heating_degree_days: verilen bir günde ortalama sıcaklık 65 Fahrenheit derecenin altındaysa ısıtma derece günü. Her ay, binanın bulunduğu yerdeki toplam yılı oluşturmak için toplanır.\n
    precipitation_inches: binanın bulunduğu yerde yıllık yağış miktarı (inç cinsinden)\n
    snowfall_inches: binanın bulunduğu yerde yıllık kar yağışı miktarı (inç cinsinden)\n
    snowdepth_inches: binanın bulunduğu yerde yıllık kar kalınlığı (inç cinsinden)\n
    avg_temp: binanın bulunduğu yerde bir yıl boyunca ortalama sıcaklık\n
    days_below_30F: binanın bulunduğu yerde 30 Fahrenheit derecenin altındaki toplam gün sayısı\n
    days_below_20F: binanın bulunduğu yerde 20 Fahrenheit derecenin altındaki toplam gün sayısı\n
    days_below_10F: binanın bulunduğu yerde 10 Fahrenheit derecenin altındaki toplam gün sayısı\n
    days_below_0F: binanın bulunduğu yerde 0 Fahrenheit derecenin altındaki toplam gün sayısı\n
    days_above_80F: binanın bulunduğu yerde 80 Fahrenheit derecenin üzerindeki toplam gün sayısı\n
    days_above_90F: binanın bulunduğu yerde 90 Fahrenheit derecenin üzerindeki toplam gün sayısı\n
    days_above_100F: binanın bulunduğu yerde 100 Fahrenheit derecenin üzerindeki toplam gün sayısı\n
    days_above_110F: binanın bulunduğu yerde 110 Fahrenheit derecenin üzerindeki toplam gün sayısı\n
    direction_max_wind_speed: binanın bulunduğu yerde maksimum rüzgar hızı için rüzgar yönü. 360 derece pusula noktası yönünde verilir (örneğin 360 = kuzey, 180 = güney, vb.).\n
    direction_peak_wind_speed: binanın bulunduğu yerde pik rüzgar hızı için rüzgar yönü. 360 derece pusula noktası yönünde verilir (örneğin 360 = kuzey, 180 = güney, vb.).\n
    max_wind_speed: binanın bulunduğu yerdeki maksimum rüzgar hızı\n
    days_with_fog: binanın bulunduğu yerde sisli gün sayısı\n
""")

st.header('**Veri Seti**')
df = pd.read_csv("train.csv")
st.write(df)
st.write('---')
