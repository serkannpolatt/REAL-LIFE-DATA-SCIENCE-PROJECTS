import streamlit as st
st.set_page_config(layout="wide")

from PIL import Image
import pandas as pd
import numpy as np
import joblib
from xgboost import XGBRegressor

st.title("Tesis Enerji Yoğunluğu Tahmini Uygulaması 🏢⚡")
st.image(Image.open("Images/banner.jpg"))

model = joblib.load("model_v2.joblib")

def get_forecast(data):
    model = joblib.load("model_v2.joblib")
    return model.predict(data)

def main():
    with st.form('prediction_form'):
        st.subheader("Binanın özelliklerini ve site hava koşullarını girin:")
        col0, col1, col2, col3 = st.columns([0.1, 0.4, 0.4, 0.1])

        floor_area = col1.number_input(label="Bina alanı", min_value=1, step=1)
        building_type = col1.radio("Bina türünü seçin: ", ['Ticari', 'Konut'])
        ratings = col1.slider("Energy Star Derecelendirmesi", min_value=1, step=1, max_value=5)
        year_built = col1.number_input("Yapım yılı", min_value=1920, step=1, max_value=2030)
        elevation = col1.number_input(label="Binanın bulunduğu alanın rakımı", min_value=1, step=1)
        day30 = col1.number_input(label="30°F altındaki gün sayısı", min_value=1, step=1)

        hdd = col2.number_input(label="Isıtma Derecesi Günü", min_value=1, step=1)
        cdd = col2.number_input(label="Soğutma Derecesi Günü", min_value=1, step=1)
        precip = col2.number_input(label="Yağış miktarı (inç cinsinden)")
        snow = col2.number_input(label="Kar miktarı (inç cinsinden)")
        day80 = col2.number_input(label="80°F üzerindeki gün sayısı")
      
        avg_min_win = col1.slider(label="Kışın Ortalama Minimum Sıcaklık")
        avg_max_win = col1.slider(label="Kışın Ortalama Maksimum Sıcaklık")
        avg_win = col1.slider(label="Kışın Ortalama Sıcaklık")

        avg_min_sum = col2.slider(label="Yazın Ortalama Minimum Sıcaklık")
        avg_max_sum = col2.slider(label="Yazın Ortalama Maksimum Sıcaklık")
        avg_sum = col2.slider(label="Yazın Ortalama Sıcaklık")

        submit = st.form_submit_button("Site EUI Tahmini")

    if submit:
        if building_type == 'Ticari':
            building_type = 0
        if building_type == 'Konut':
            building_type = 1
        
        floor_area = np.float64(floor_area)
        year_built = np.float64(year_built)
        ratings = np.float64(ratings)
        elevation = np.float64(elevation)
        cdd = np.int64(cdd)
        hdd = np.int64(hdd)
        precip = np.float64(precip)
        snow = np.float64(snow)
        day80 = np.int64(day80)
        avg_min_win = np.float64(avg_min_win)
        avg_max_win = np.float64(avg_max_win)
        avg_win = np.float64(avg_win)
        avg_min_sum = np.float64(avg_min_sum)
        avg_max_sum = np.float64(avg_max_sum)
        avg_sum = np.float64(avg_sum)
        day30 = np.float64(avg_sum)

        data = np.array([building_type, floor_area, year_built, ratings, elevation, cdd, hdd, precip, snow, day80, avg_min_win, avg_max_win, avg_win, avg_min_sum, avg_max_sum, avg_sum, avg_sum]).reshape(1, -1)

        pred = get_forecast(data)

        st.write("Tahmini Site EUI (Enerji Kullanım Yoğunluğu): **{:.2f}** birim".format(pred[0]))

if __name__ == '__main__':
    main()
