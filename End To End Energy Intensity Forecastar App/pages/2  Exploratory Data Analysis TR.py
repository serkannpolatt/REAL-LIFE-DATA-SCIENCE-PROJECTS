import streamlit as stl
stl.set_page_config(layout="wide")

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.impute import KNNImputer
from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBRegressor
import xgboost
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold, cross_val_score
import sklearn
import shap
import optuna
import joblib

import numpy as np
import pandas as pd
import streamlit as stl
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components

import codecs 

import sweetviz as sv

def count_plot(variable, num, data):
    fig = plt.figure(figsize=(12,7))
    count = sns.countplot(y=variable,data=data,color="salmon", facecolor=(0, 0, 0, 0),linewidth=5,edgecolor=sns.color_palette("BrBG", num))
    count.set_title('Train')
    return plt
    # plt.save(f"Plots/{variable}_count_plot.jpg")


def main():
    

    df = pd.read_csv("train.csv")
    df_test = pd.read_csv("test.csv")

    stl.header('**DataFrame**')
    stl.write(df)
    stl.write('---')

    stl.header('**Keşifsel Veri Analizi**')
    stl.write("""
    Bu analiz, eğitim veri setinin keşifsel analizini gerçekleştirmeyi ve her bir değişkenin hedef değişkenimiz olan 'site_eui' 
    (Bir binanın tüketmiş olduğu ısı ve elektrik miktarı olarak ifade edilen Site Enerji Kullanım Yoğunluğu) ile nasıl ilişkili olduğunu anlamayı amaçlamaktadır.
    Toplamda 64 öznitelik bulunmaktadır (hedef değişkeni dahil).
    """)

    stl.write("Veri kümesinin profil raporuna hızlı bir göz atalım, veri kümesini daha iyi anlamak için değişken adına tıklayabilirsiniz.")

    report_file = codecs.open('Pages/EDA.html', 'r')
    page = report_file.read()
    components.html(page, width=2000, height=1500, scrolling=True)

    stl.header('**Veri Setinden Elde Edilen İpuçları**')

    stl.write("Tekrarlanan veri örneği olmayan toplamda 75,757 veri örneği bulunmaktadır. 64 değişkenin 57'si sayısal ve geri kalan 7'si kategoriktir.")

    stl.subheader('**Kategorik Değişkenler**')

    stl.subheader('**Yıl Faktörü**')
    stl.write("""Bu özellik, veri örneklerinin kaydedildiği yılı temsil eder. Veri örneklerinin çoğunluğu (%50'den fazlası) yıl 5 ve yıl 6'ya aittir.
                 Yıllara göre median site enerji kullanımı yaklaşık olarak aynı değere sahiptir. 200 SUI'nin üzerindeki değerler aykırı değerlerdir. 
                Test veri kümesine baktığımızda, veri örneklerinin kaydedildiği yalnızca bir yıl bulunmaktadır.
              """)
    stl.image("./EDA_Plots/Year_Factor_count_plot.jpg", caption="Eğitim veri kümesinde Yıl Faktörü")
    stl.image("./EDA_Plots/Year_Factor_test_count_plot.jpg", caption="Test veri kümesinde Yıl Faktörü")
    stl.write("""Site EUI vs Yıl Faktörü
              """)
    stl.image("EDA_Plots/Year_Factor_vs_eui.jpg", caption="Yıl Faktörü vs Site EUI")
    stl.write("Yıl bazında Site EUI dağılımı")
    stl.image("EDA_Plots/year_distribution.jpg", caption="Yıl Faktörü vs Site EUI")
    stl.write("---")

    stl.subheader('**Bölge Faktörü**')
    stl.write("""Toplamda 7 farklı eyalet bulunmaktadır. Veri örneklerinin çoğunluğu 6. eyalete aittir. Test verilerine baktığımızda, 6. eyaletten örnek bulunmamaktadır. Test veri kümesindeki çoğunluk eyaleti ise 11. eyalettir. Median Site EUI değeri 6. eyalet için en yüksektir.
              """)
    stl.image("./EDA_Plots/State_Factor_count_plot.jpg", caption="Eğitim veri kümesinde Bölge Faktörü")
    stl.image("./EDA_Plots/State_Factor_test_count_plot.jpg", caption="Test veri kümesinde Bölge Faktörü")
    stl.write("""Site EUI vs Bölge Faktörü              """)
    stl.image("EDA_Plots/State_Factor_vs_eui.jpg", caption="Bölge Faktörü vs Site EUI")
    stl.write("Eyalet bazında Site EUI dağılımı")
    stl.image("EDA_Plots/state_distribution.jpg", caption="Bölge Faktörü vs Site EUI")

    stl.subheader('**Bina Sınıfı**')
    stl.write("""Veri örnekleri genel olarak iki bina tipine ayrılır: konut ve ticari. İlginç bir şekilde, hem konut binaları hem de ticari binalar için median Site EUI değeri oldukça benzer görünmektedir. Bu değişken, Tesis Türü ile birlikte incelenmesi gerekmektedir. Ayrıca, konut binalarına kıyasla ticari binalar için daha fazla veri örneği kaydedilmiştir.
    """)
    stl.image("./EDA_Plots/building_class_count_plot.jpg", caption="Eğitim veri kümesinde Bina Sınıfı")
    stl.image("./EDA_Plots/building_class__test_count_plot.jpg", caption="Test veri kümesinde Bina Sınıfı")
    stl.write("""Site EUI vs Bina Sınıfı              """)
    stl.image("EDA_Plots/building_class_vs_eui.jpg", caption="Bina sınıfı vs Site EUI")
    stl.write("Bina tipine göre Site EUI dağılımı")
    stl.image("EDA_Plots/building_distribution.jpg", caption="Bölge Faktörü vs Site EUI")

    stl.subheader('**Tesis Türü**')
    stl.write("""Median Site EUI değeri, ticari bina sınıfına dahil olan Veri Merkezleri için en yüksektir. Konut bina sınıfında ise Karışık kullanım türlerinin median Site EUI değeri en yüksektir.
    """)
    stl.image("./EDA_Plots/facility_count.jpg", caption="Eğitim veri kümesinde Tesis Türü")
    # stl.image("./EDA_Plots/building_class__test_count_plot.jpg", caption="Facility Type in Test dataset")
    stl.write("""En yüksek Site EUI'ye sahip konut tesisleri""")
    stl.image("EDA_Plots/top_res_eui.jpg", caption="En yüksek Site EUI'ye sahip konut tesisleri")
    stl.write("""En yüksek Site EUI'ye sahip ticari tesisler""")
    stl.image("EDA_Plots/top_com_eui.jpg", caption="En yüksek Site EUI'ye sahip ticari tesisler")


    stl.subheader('**Sayısal Değişkenler**')

    stl.subheader('**Kat Alanı**')
    stl.write("""Oldukça çeşitli bir bina setimiz var, kat alanı 900 metrekare ile 63.000 metrekare arasında değişiyor. Beklendiği gibi, daha yüksek kat alanına sahip binaların median Site EUI değeri de yüksek oluyor.
    """)
    stl.write("""Site EUI'nin Kat Alanı ile nasıl değiştiğine bakalım""")
    stl.image("EDA_Plots/floor_area.jpg", caption="Kat alanı vs Site EUI")
    stl.write("""Bina sınıfına göre Site EUI'nin Kat Alanı ile nasıl değiştiğine bakalım""")
    stl.image("EDA_Plots/floor_area_build.jpg", caption="Kat alanı vs Site EUI (Bina Sınıfına göre)")
    stl.write("""Bina sınıfına göre Site EUI'nin Kat Alanı ile nasıl değiştiğine bakalım""")
    

    stl.subheader('**Yapım Yılı**')
    stl.write("""Beklendiği gibi, daha yeni binaların median Site EUI değeri, daha eski binalara göre daha düşüktür. Bu oldukça sezgiseldir.""")
    stl.write("""Son 50 yılda inşa edilen binaların Median Site EUI değerlerine bakalım""")
    stl.image("EDA_Plots/year_built.jpg", caption="Yapım Yılına göre Median Site EUI")

    stl.subheader('**Energy Star Derecelendirmesi**')
    stl.write("""Beklendiği gibi, enerji star derecelendirmesi düşük olan binaların median Site EUI değeri yüksek olur ve tam tersi.""")
    stl.write("""Binaların enerji star derecelendirmesi ile Site EUI'nin nasıl değiştiğine bakalım""")
    stl.image("EDA_Plots/energy_rating_2.jpg", caption="Binaların Site EUI'si vs. enerji star derecelendirmesi")
    stl.write("""Binaların enerji star derecelendirmesi ile Median Site EUI'nin nasıl değiştiğine bakalım""")
    stl.image("EDA_Plots/Energy_rating.jpg", caption="Binaların Median Site EUI'si vs. enerji star derecelendirmesi")
    stl.write("""Binaların enerji star derecelendirmesi ile kat alanının nasıl değiştiğine bakalım""")
    stl.image("EDA_Plots/Energy_rating3.jpg", caption="Binaların enerji star derecelendirmesi vs. bina kat alanı")
    stl.write("""Enerji star derecelendirmesinin bina sınıfına göre nasıl değiştiğine bakalım""")
    stl.image("EDA_Plots/energy_rating_vs_building.jpg", caption="Binaların enerji star derecelendirmesi vs. bina sınıfı")

    stl.subheader('**Yükseklik**')
    stl.write("""""")
    stl.write("""Binaların yüksekliği ile Site EUI'nin nasıl değiştiğine bakalım""")
    stl.image("EDA_Plots/elevation.jpg", caption="Bina Yüksekliği vs Site EUI")

    stl.subheader('**Sıcaklık**')
    stl.write("""4. eyalet diğer eyaletlere göre en düşük minimum sıcaklığa sahip, önceden gözlemlediğimiz gibi, 4. eyaletin (ve 6. eyaletin) veri setinde en yüksek median Site EUI'ya sahip olduğunu gördük. Sıcaklık grafiği, 11. eyalette 40-80 arasında optimal sıcaklık olduğunu ve dolayısıyla en düşük median Site EUI'ya sahip olduğunu gösteriyor""")
    stl.write("""Eyaletlere göre minimum sıcaklıkların yıl boyunca nasıl değiştiğine bakalım""")
    stl.image("EDA_Plots/statewise_min_temp.jpg", caption="Yıl boyunca minimum sıcaklıklar")
    stl.write("""Eyaletlere göre maksimum sıcaklıkların yıl boyunca nasıl değiştiğine bakalım""")
    stl.image("EDA_Plots/statewise_max_temp.jpg", caption="Yıl boyunca maksimum sıcaklıklar")

    stl.subheader('**Isıtma Derecesi Günleri ve Soğutma Derecesi Günleri**')
    stl.image("EDA_Plots/hdd_cdd.jpg", caption="Yıl boyunca Isıtma Derecesi Günleri ve Soğutma Derecesi Günleri")

    stl.write("""Eyaletlere göre median soğutma derecesi günlerinin median Site EUI'ya etkisine bakalım""")
    stl.image("EDA_Plots/cdd_eui.jpg", caption="Median Soğutma Derecesi Günleri vs. median Site EUI")

    stl.write("""Eyaletlere göre median ısıtma derecesi günlerinin median Site EUI'ya etkisine bakalım""")
    stl.image("EDA_Plots/hdd_eui.jpg", caption="Median Isıtma Derecesi Günleri vs. median Site EUI")

    stl.subheader('**Yağış ve Kar**')
    stl.write("""Yağışın (inç cinsinden) Site EUI'ya etkisine bakalım""")
    stl.image("EDA_Plots/snow.jpg", caption="Yağış vs. median Site EUI")
    stl.write("""Kar yağışının (inç cinsinden) Site EUI'ya etkisine bakalım""")
    stl.image("EDA_Plots/preci.jpg", caption="Kar Yağışı vs. median Site EUI")

    stl.subheader('**Değişkenler Arasındaki Korelasyon**')
    stl.image("EDA_Plots/corr_heatmap.jpg", caption="Korelasyon ısı haritası")

    stl.write("""Yüksek Site EUI değerlerini (potansiyel aykırı değerler) çıkaralım, daha güçlü bir korelasyon görüyoruz""")
    stl.image("EDA_Plots/corr_heatmap2.jpg", caption="Korelasyon ısı haritası (Site EUI < 200)")

    stl.write("""Yüksek Site EUI değerleri için (potansiyel aykırı değerler) korelasyona bakalım""")
    stl.image("EDA_Plots/corr_heatmap3.jpg", caption="Korelasyon ısı haritası (Site EUI > 200)")

    stl.header('**Sonuçlar**')
    stl.write("""
            6 sütunda eksik değerler var (eksik değerlerin yüzdesini ekleyin)
            Veri setinde birden fazla sütunun korelasyonu var
            Kış ve yaz sıcaklıkları birbirleriyle ilişkilidir
            Sayısal özellikler için dağılım grafiği ekleyin
              
    """)


if __name__ == "__main__":
      main()
