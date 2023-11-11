# Gerekli kütüphaneleri içe aktarın
from sklearn import preprocessing 
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Önceden eğitilmiş modeli yükle
filename = 'final_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Müşteri verilerini oku
df = pd.read_csv("Clustered_Customer_Data.csv")

# Streamlit ayarlarını yapılandır
st.set_option('deprecation.showPyplotGlobalUse', False)

# Arka plan rengini ayarla
st.markdown('<style>body{background-color: Mavi;}</style>', unsafe_allow_html=True)

# Uygulama başlığını ayarla
st.title("Tahmin")

# Form oluştur ve kullanıcı girişlerini al
with st.form("my_form"):
    balance = st.number_input(label='Bakiye', step=0.001, format="%.6f")
    balance_frequency = st.number_input(label='Bakiye Frekansı', step=0.001, format="%.6f")
    purchases = st.number_input(label='Alışverişler', step=0.01, format="%.2f")
    oneoff_purchases = st.number_input(label='Tek Seferlik Alışverişler', step=0.01, format="%.2f")
    installments_purchases = st.number_input(label='Taksitli Alışverişler', step=0.01, format="%.2f")
    cash_advance = st.number_input(label='Nakit Avans', step=0.01, format="%.6f")
    purchases_frequency = st.number_input(label='Alışveriş Frekansı', step=0.01, format="%.6f")
    oneoff_purchases_frequency = st.number_input(label='Tek Seferlik Alışveriş Frekansı', step=0.1, format="%.6f")
    purchases_installment_frequency = st.number_input(label='Taksitli Alışveriş Frekansı', step=0.1, format="%.6f")
    cash_advance_frequency = st.number_input(label='Nakit Avans Frekansı', step=0.1, format="%.6f")
    cash_advance_trx = st.number_input(label='Nakit Avans İşlem Sayısı', step=1)
    purchases_trx = st.number_input(label='Alışveriş İşlem Sayısı', step=1)
    credit_limit = st.number_input(label='Kredi Limiti', step=0.1, format="%.1f")
    payments = st.number_input(label='Ödemeler', step=0.01, format="%.6f")
    minimum_payments = st.number_input(label='Minimum Ödemeler', step=0.01, format="%.6f")
    prc_full_payment = st.number_input(label='Tam Ödeme Oranı', step=0.01, format="%.6f")
    tenure = st.number_input(label='Görev süresi', step=1)

    # Kullanıcıdan alınan veriyi bir liste içinde sakla
    data = [[balance, balance_frequency, purchases, oneoff_purchases, installments_purchases, cash_advance,
             purchases_frequency, oneoff_purchases_frequency, purchases_installment_frequency, cash_advance_frequency,
             cash_advance_trx, purchases_trx, credit_limit, payments, minimum_payments, prc_full_payment, tenure]]

    # Formu gönder düğmesi
    submitted = st.form_submit_button("Gönder")

# Form gönderildiyse
if submitted:
    # Tahmin yap ve sonucu görüntüle
    clust = loaded_model.predict(data)[0]
    print('Veri, Küme', clust, 'a aittir')

    # Veri çerçevesinde tahmin edilen kümenin verilerini al
    cluster_df1 = df[df['Cluster'] == clust]

    # Grafik boyutlarını ayarla
    plt.rcParams["figure.figsize"] = (20, 3)

    # Her sütun için bir histogram çiz ve göster
    for c in cluster_df1.drop(['Cluster'], axis=1):
        fig, ax = plt.subplots(figsize=(5, 5))
        sns.histplot(cluster_df1[c], ax=ax)  # Yalnızca bir küme için grafik çizin
        plt.show()
        st.pyplot(fig)