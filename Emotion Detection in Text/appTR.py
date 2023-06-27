# Core Paketler
import streamlit as st
import altair as alt
import plotly.express as px

# EDA Paketleri
import pandas as pd
import numpy as np
from datetime import datetime

# Modeli Yükleme
import joblib
pipe_lr = joblib.load(open("./models/emotion_classifier_pipe_lr.pkl", "rb"))

# İzleme Yardımcıları
from track_utils import (
    create_page_visited_table,
    add_page_visited_details,
    view_all_page_visited_details,
    add_prediction_details,
    view_all_prediction_details,
    create_emotionclf_table,
)

# Duygu Tahmini Fonksiyonu
def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    return results[0]

# Tahmin Olasılıklarını Alma Fonksiyonu
def get_prediction_proba(docx):
    results = pipe_lr.predict_proba([docx])
    return results

# Duygu ve Emoji Eşleme Sözlüğü
emotions_emoji_dict = {
    "anger": "😠",
    "disgust": "🤮",
    "fear": "😨😱",
    "happy": "🤗",
    "joy": "😂",
    "neutral": "😐",
    "sad": "😔",
    "sadness": "😔",
    "shame": "😳",
    "surprise": "😮",
}

# Ana Uygulama
def main():
    st.title("Duygu Sınıflandırma Uygulaması")
    menu = ["Anasayfa", "İzleme", "Hakkında"]
    choice = st.sidebar.selectbox("Menü", menu)
    create_page_visited_table()
    create_emotionclf_table()

    if choice == "Anasayfa":
        add_page_visited_details("Anasayfa", datetime.now())
        st.subheader("Metinde Duygu Tespiti")

        with st.form(key="emotion_clf_form"):
            raw_text = st.text_area("Buraya Yazın")
            submit_text = st.form_submit_button(label="Gönder")

        if submit_text:
            col1, col2 = st.columns(2)

            # Fonksiyonu Burada Uygula
            prediction = predict_emotions(raw_text)
            probability = get_prediction_proba(raw_text)

            add_prediction_details(raw_text, prediction, np.max(probability), datetime.now())

            with col1:
                st.success("Orijinal Metin")
                st.write(raw_text)

                st.success("Tahmin")
                emoji_icon = emotions_emoji_dict[prediction]
                st.write("{}:{}".format(prediction, emoji_icon))
                st.write("Güvenlik:{}".format(np.max(probability)))

            with col2:
                st.success("Tahmin Olasılığı")
                proba_df = pd.DataFrame(probability, columns=pipe_lr.classes_)
                proba_df_clean = proba_df.T.reset_index()
                proba_df_clean.columns = ["duygular", "olasılık"]

                fig = alt.Chart(proba_df_clean).mark_bar().encode(
                    x="duygular", y="olasılık", color="duygular"
                )
                st.altair_chart(fig, use_container_width=True)

    elif choice == "İzleme":
        add_page_visited_details("İzleme", datetime.now())
        st.subheader("İzleme Uygulaması")

        with st.expander("Sayfa Metrikleri"):
            page_visited_details = pd.DataFrame(
                view_all_page_visited_details(), columns=["Sayfa Adı", "Ziyaret Zamanı"]
            )
            st.dataframe(page_visited_details)

            pg_count = page_visited_details["Sayfa Adı"].value_counts().rename_axis(
                "Sayfa Adı"
            ).reset_index(name="Sayılar")
            c = alt.Chart(pg_count).mark_bar().encode(
                x="Sayfa Adı", y="Sayılar", color="Sayfa Adı"
            )
            st.altair_chart(c, use_container_width=True)

            p = px.pie(pg_count, values="Sayılar", names="Sayfa Adı")
            st.plotly_chart(p, use_container_width=True)

        with st.expander("Duygu Sınıflandırma Metrikleri"):
            df_emotions = pd.DataFrame(
                view_all_prediction_details(),
                columns=["Orijinal Metin", "Tahmin", "Olasılık", "Ziyaret Zamanı"],
            )
            st.dataframe(df_emotions)

            prediction_count = df_emotions["Tahmin"].value_counts().rename_axis(
                "Tahmin"
            ).reset_index(name="Sayılar")
            pc = alt.Chart(prediction_count).mark_bar().encode(
                x="Tahmin", y="Sayılar", color="Tahmin"
            )
            st.altair_chart(pc, use_container_width=True)

    else:
        st.subheader("Hakkında")
        st.write("Bu bir duygu sınıflandırma uygulamasıdır. Metin girişi yaparak duygularınızın tahminini gerçekleştirebilirsiniz.")
        st.write("Uygulama, bir duygu sınıflandırma modelini kullanarak metinlerdeki duyguları tahmin etmek için geliştirilmiştir.")
        st.write("Model, eğitilmiş bir makine öğrenimi modelini yükleyerek duygu tahmini yapar. Bu model, metindeki duyguları sınıflandırmak için birçok dil işleme ve makine öğrenimi tekniği kullanır.")
        st.write("Duygu tahmin sonuçları, tahmin edilen duygunun yanı sıra bir güvenlik değeriyle birlikte sunulur. Ayrıca, tahmin olasılıkları da görselleştirilir.")
        st.write("Uygulama ayrıca kullanıcı etkileşimlerini ve duygu sınıflandırma metriklerini izlemek için bir izleme bölümü içerir.")
        st.write("Daha fazla bilgi için [GitHub](https://github.com/serkannpolatt) sayfasını ziyaret edebilirsiniz.")

add_page_visited_details("Hakkında", datetime.now())

if __name__ == "__main__":
    main()
