import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Veri yükleme

data = pd.read_csv('superstore_dataset2011-2015.csv', encoding="ISO-8859-1")

# Yan Menü (Sidebar)
st.sidebar.title("Hipotezler")
hipotez = st.sidebar.radio("Bir hipotez seçin:", [
    "Teknoloji ürünleri diğer ürün kategorilerine göre en yüksek kar marjına sahiptir.",
    "Doğu bölgesi diğer bölgelere göre en yüksek satışa sahiptir.",
    "Satışlar yılın belirli aylarında daha yüksektir.",
    "Aynı gün kargolanan siparişlerin iade oranı en düşüktür.",
    "Şirketin karı hafta içi günlerde hafta sonlarından daha fazladır."
])

# Ana Sayfa
st.title("Süpermarket Satışları Kontrol Paneli")

# Hipotez 1
if hipotez == "Teknoloji ürünleri diğer ürün kategorilerine göre en yüksek kar marjına sahiptir.":
    # Ürün kategorilerine göre gruplayarak toplam kârı hesaplayın
    plt.figure(figsize=(8, 5))
    kat_kar = data.groupby('Category')['Profit'].sum()

    # Kategorilere göre çubuk grafiği oluşturun
    fig, ax = plt.subplots()
    ax.bar(kat_kar.index, kat_kar.values)
    ax.set_title('Kategoriye Göre Toplam Kar')
    ax.set_xlabel('Kategori')
    ax.set_ylabel('Toplam Kar')
    st.pyplot(fig)

    # Sonuç
    st.write(
        "Sonuç: Hipotez destekleniyor, çünkü teknoloji ürünleri üç kategori arasında en yüksek kâr marjına sahiptir.")

# Hipotez 2
elif hipotez == "Doğu bölgesi diğer bölgelere göre en yüksek satışa sahiptir.":
    # Bölgelere göre gruplayarak satışların toplamını hesaplayın
    bolge_satis = data.groupby('Region')['Sales'].sum()

    # Bölgelere göre çubuk grafiği oluşturun
    fig, ax = plt.subplots()
    ax.bar(bolge_satis.index, bolge_satis.values)
    ax.set_title('Bölgeye Göre Toplam Satışlar')
    ax.set_xlabel('Bölge')
    ax.set_ylabel('Toplam Satışlar')
    ax.tick_params(axis='x', rotation=45)  # x ekseni etiketini döndür
    st.pyplot(fig)

    # Sonuç
    st.write("Sonuç: Hipotez desteklenmiyor, çünkü merkezi bölge en yüksek satışa sahiptir.")

# Hipotez 3
elif hipotez == "Satışlar yılın belirli aylarında daha yüksektir.":
    # Sipariş Tarihinden ayı çıkarın
    data['Sipariş Ayı'] = pd.DatetimeIndex(data['Sipariş Tarihi']).month

    # Aya göre gruplayarak satışların toplamını hesaplayın
    ay_satis = data.groupby('Sipariş Ayı')['Satışlar'].sum()

    # Aya göre satışların çizgi grafiğini oluşturun
    fig, ax = plt.subplots()
    ax.plot(ay_satis.index, ay_satis.values)
    ax.set_title('Aya Göre Toplam Satışlar')
    ax.set_xlabel('Ay')
    ax.set_ylabel('Toplam Satışlar')
    ax.tick_params(axis='x', rotation=45)  # x ekseni etiketini döndür
    st.pyplot(fig)

    # Sonuç
    st.write(
        "Sonuç: Çizgi grafiğinden de görülebileceği gibi, satışlar Kasım ve Aralık aylarında daha yüksektir. Bu, hipotezimizi desteklemektedir.")

# Hipotez 4
elif hipotez == "Aynı gün kargolanan siparişlerin iade oranı en düşüktür.":
    # Her kargo modu için toplam sipariş sayısını hesaplayın
    toplam_siparis_sayisi_kargo_moduna_gore = data.groupby('Kargo Modu').size()

    # Her kargo modu için iade edilen siparişlerin toplam sayısını hesaplayın
    kargo_moduna_gore_iade_edilen_siparis_sayisi = data[data['Kar'] < 0].groupby('Kargo Modu').size()

    # Her kargo modu için siparişlerin iade oranını hesaplayın
    kargo_moduna_gore_iade_orani = (kargo_moduna_gore_iade_edilen_siparis_sayisi / toplam_siparis_sayisi_kargo_moduna_gore) * 100

    # İade oranına göre çubuk grafiği oluşturun
    fig, ax = plt.subplots()
    ax.bar(kargo_moduna_gore_iade_orani.index, kargo_moduna_gore_iade_orani.values)
    ax.set_title('Kargo Moduna Göre İade Oranı')
    ax.set_xlabel('Kargo Modu')
    ax.set_ylabel('İade Oranı')
    ax.tick_params(axis='x', rotation=45)  # x ekseni etiketini döndür
    st.pyplot(fig)

    # Sonuç
    st.write("Sonuç: Hipotez destekleniyor, çünkü aynı gün kargolanan siparişlerin iade oranı en düşüktür.")
elif hipotez == "Şirketin karı hafta içi günlerde hafta sonlarından daha fazladır.":
    # Sipariş Tarihinden gün adını çıkarın
    data['Sipariş Günü'] = pd.DatetimeIndex(data['Sipariş Tarihi']).day_name()
    # Hafta içi günleri (Pazartesi-Cuma) için ortalama karı hesaplayın
    haftaici_kar = data.groupby('Sipariş Günü')['Kar'].sum()

    # Hafta içi günleri için çubuk grafiği oluşturun
    fig, ax = plt.subplots()
    ax.bar(haftaici_kar.index, haftaici_kar.values)
    ax.set_title('Hafta İçi Günlerine Göre Ortalama Kar')
    ax.set_xlabel('Hafta İçi Günü')
    ax.set_ylabel('Toplam Kar')
    st.pyplot(fig)

    # Sonuç
    st.write("Sonuç: Hipotez destekleniyor, çünkü hafta içi günlerde ortalama kar hafta sonlarından daha yüksektir.")
