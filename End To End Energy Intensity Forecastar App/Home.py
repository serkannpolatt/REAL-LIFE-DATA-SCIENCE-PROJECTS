import streamlit as st
st.set_page_config(layout="wide")

from PIL import Image
import pandas as pd
import numpy as np
import joblib
from xgboost import XGBRegressor


st.title("Energy Intensity Forecast Application 🏢⚡")
st.image(Image.open("Images/banner.jpg"))

model = joblib.load("model_v2.joblib")


# st.markdown(
#     """
# <style>
# .reportview-container .markdown-text-container {
#     font-family: serif;
# }
# .sidebar .sidebar-content {
#     background-image: linear-gradient(#cf872e,#2e7bcf);
#     color: white;
# }
# .Widget>label {
#     color: white;
#     font-family: serif;
# }
# [class^="st-b"]  {
#     color: white;
#     font-family: monospace;
# }
# .st-bb {
#     background-color: transparent;
# }
# .st-at {
#     background-color: #0c0080;
# }
# footer {
#     font-family: monospace;
# }
# .reportview-container .main footer, .reportview-container .main footer a {
#     color: #0c0080;
# }
# header .decoration {
#     background-image: none;
# }

# </style>
# """,
#     unsafe_allow_html=True,
# )


def get_forecast(data):
    model = joblib.load("model_v2.joblib")
    return model.predict(data)


def main():
    with st.form('prediction_form'):

        st.subheader("Enter building characteristics and site weather conditions:")
        col0,col1, col2,col3 = st.columns([0.1,0.4,0.4,0.1])

        floor_area = col1.number_input(label='Building\'s floor area', min_value=1, step = 1)
        building_type = col1.radio("Choose building type: ", ['Commercial', 'Residential'])
        ratings = col1.slider("Energy Star Ratings ",min_value=1, step=1, max_value=5)
        year_built = col1.number_input("Year built", min_value=1920, step=1, max_value=2030)
        elevation = col1.number_input(label='Elevation of the site (on which building is constructed)', min_value=1, step=1)
        day30 = col1.number_input(label='Days below 30F', min_value=1, step=1)

        hdd = col2.number_input(label='Heating Degree Days', min_value=1, step=1)
        cdd = col2.number_input(label='Colling Degree Days', min_value=1, step=1)
        precip = col2.number_input(label='Precipitation (in inches)')
        snow = col2.number_input(label='Snowfall (in inches)')
        day80 = col2.number_input(label='Days above 80F')
      
        avg_min_win = col1.slider(label='Average Minimum Temperature Winter')
        avg_max_win = col1.slider(label='Average Maximum Temperature Winter')
        avg_win =  col1.slider(label='Average Temperature Winter')

        avg_min_sum =  col2.slider(label='Average Minimum Temperature Summer')
        avg_max_sum =  col2.slider(label='Average Maximum Temperature Summer')
        avg_sum = col2.slider(label='Average  Temperature Summer')

        submit = st.form_submit_button("Forecast Site EUI")

    if submit:
        if building_type == 'Commercial':
           building_type = 0
        if building_type == 'Residential':
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
        avg_win =  np.float64(avg_win)

        avg_min_sum =  np.float64(avg_min_sum)
        avg_max_sum =  np.float64(avg_max_sum)
        avg_sum = np.float64(avg_sum)

        day30 = np.float64(avg_sum)

        data = np.array([building_type,floor_area,year_built,ratings,elevation,cdd ,hdd,precip,snow,day80,avg_min_win,avg_max_win,avg_win,avg_min_sum,avg_max_sum,avg_sum,avg_sum]).reshape(1,-1)

        pred = get_forecast(data)

       
        st.write('Forecasted Energy Use Intensity for the site is: **{:.2f}** units'.format(pred[0]))
       

if __name__ == '__main__':
    main()