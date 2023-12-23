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

    stl.header('**Exploratory Data Analysis**')
    stl.write("""
    The aim of this analysis is to perform the exploratory analysis of train dataset and 
    get some insights on how each of the variables relate to our target variable which is 'site_eui'
      (Site Energy Usage Intensity-the amount of heat and electricity consumed by a building). 
      We have about 64 attributes in total(including the target variable). 
    """)

    stl.write("Lets take a quick look at profile report of the dataframe, to better understand the dataset. Click on the variable name to enlarge the associated chart")

    report_file = codecs.open('Pages/EDA.html','r')
    page = report_file.read()
    components.html(page,width=2000,height=1500,scrolling=True)

    

    stl.header('**Insights from the Dataset**')

    stl.write("There are 75757 data samples with zero duplicates. Out of 64 variables, 57 are numerical and the rest 7 are categorical ")

    stl.subheader('**Categorical Variables**')

    stl.subheader('**Year Factor**')
    stl.write("""This feature corresponds to the year in which the data samples were recorded, majority of the data samples (almost half) belong to just year 5 and year 6. 
                 Median site energy usage across the years appears to be around the same value. Values above 200 SUI are outliers. 
                Looking at the test dataset, there is only one year in wihch the samples were recorded.
              """)
    # s1,s2 = stl.columns(2)
    stl.image("./EDA_Plots/Year_Factor_count_plot.jpg", caption="Year Factor in Train dataset")
    stl.image("./EDA_Plots/Year_Factor_test_count_plot.jpg", caption="Year Factor in Test dataset")
    # s2.image()
    stl.write("""Site EUI vs Year Factor
              """)
    stl.image("EDA_Plots/Year_Factor_vs_eui.jpg", caption="Year Factor vs Site EUI")
    stl.write("Year wise distribution of site EUI")
    stl.image("EDA_Plots/year_distribution.jpg", caption="Year Factor vs Site EUI")
    stl.write("---")




    stl.subheader('**State Factor**')
    stl.write("""There are in total 7 unique states. Majority of the data samples belog to satte 6. Looking at test data, there are no samples from state 6. Majority of sata samples in test dataset belong to state 11. Median Site EUI is highest for state 6
              """)
    stl.image("./EDA_Plots/State_Factor_count_plot.jpg", caption="State Factor in Train dataset")
    stl.image("./EDA_Plots/State_Factor_test_count_plot.jpg", caption="State Factor in Test dataset")
    stl.write("""Site EUI vs State Factor              """)
    stl.image("EDA_Plots/State_Factor_vs_eui.jpg", caption="Year Factor vs Site EUI")
    stl.write("State wise distribution of site EUI")
    stl.image("EDA_Plots/state_distribution.jpg", caption="State Factor vs Site EUI")




    stl.subheader('**Building Class**')
    stl.write("""Data samples are broadly categorised into two building types: residential and Commercial. Interestingly, median Site EUI for both residential building and commercial buldings appears to be quite simillar. This variable needs to be looked in conjunction with Facility Type. Also, there are more data samples recorded for residential buildings compared to commercial buildings.
    """)
    stl.image("./EDA_Plots/building_class_count_plot.jpg", caption="Building Class in Train dataset")
    stl.image("./EDA_Plots/building_class__test_count_plot.jpg", caption="Building Class in Test dataset")
    stl.write("""Site EUI vs Building Class              """)
    stl.image("EDA_Plots/building_class_vs_eui.jpg", caption="Building class vs Site EUI")
    stl.write("Building type wise distribution of site EUI")
    stl.image("EDA_Plots/building_distribution.jpg", caption="State Factor vs Site EUI")

    stl.subheader('**Facility Type**')
    stl.write("""Median Site EUI is the highest for Data Centers which fall under commercial building class. In residential building class, Mixed use facility types have highest media Site EUI.
    """)
    stl.image("./EDA_Plots/facility_count.jpg", caption="Facility Type in Train dataset")
    # stl.image("./EDA_Plots/building_class__test_count_plot.jpg", caption="Facility Type in Test dataset")
    stl.write("""Top residential facilitie having highest Site EUI""")
    stl.image("EDA_Plots/top_res_eui.jpg", caption="residential facilities with highest Site EUI")
    stl.write("""Top commercial facilities having highest Site EUI""")
    stl.image("EDA_Plots/top_com_eui.jpg", caption="commercial facilities with highest Site EUI")

    stl.subheader('**Numerical Variables**')

    stl.subheader('**Floor Area**')
    stl.write("""We have quite a diverse set of buildings, the flooe area varies starting from 900 square feet to 63,00- square feet. As expected, buildings with highers floor area have a high median Site EUI
    """)
    stl.write("""Lets look at how Site EUI varies with Floor Area""")
    stl.image("EDA_Plots/floor_area.jpg", caption="floor area vs Site EUI")
    stl.write("""Lets look at how Site EUI varies with Floor Area, based on building class""")
    stl.image("EDA_Plots/floor_area_build.jpg", caption="residential facilities with highest Site EUI")
    stl.write("""Lets look at how Site EUI varies with Floor Area, based on building class""")
    

    stl.subheader('**Year Built**')
    stl.write("""Like we would expect, newer buildings have less median Site_EUI when compared to older buildings. This is very intuitive""")
    stl.write("""Lets take a look at Median site EUI of buildings built in last 50 years""")
    stl.image("EDA_Plots/year_built.jpg", caption="Median site EUI vs Year built")


    stl.subheader('**Energy Star Rating**')
    stl.write("""Like we would expect, building with lower energy star rating have high median Site EUI and vice versa""")
    stl.write("""Lets take a look at how  site EUI varies with building's energy star rating """)
    stl.image("EDA_Plots/energy_rating_2.jpg", caption="Site EUI of buildings vs building rating")
    stl.write("""Lets take a look at how median site EUI varies with building's energy star rating """)
    stl.image("EDA_Plots/Energy_rating.jpg", caption="Median site EUI of buildings vs building rating")
    stl.write("""Lets take a look at how energy star rating varies building's floor area """)
    stl.image("EDA_Plots/Energy_rating3.jpg", caption="Energy Star Rating of buildings vs floor area of building")
    stl.write("""Lets take a look at how energy star rating varies building type """)
    stl.image("EDA_Plots/energy_rating_vs_building.jpg", caption="Energy Star Rating of buildings vs building class")

    stl.subheader('**Elevation**')
    stl.write("""""")
    stl.write("""Lets take a look at how  site EUI varies with building's elevation """)
    stl.image("EDA_Plots/elevation.jpg", caption="Elevation of building vs Site EUI")

    stl.subheader('**Temperature**')
    stl.write("""State 4 has lowest minimum temperature compared to other states, previosuly we have observed that state 4 (along with state 6) has the highest median Site EUI in the datsaet. Temperature plot shows that, state 11 has optimal temperature between 40s to 80s, thus has the lowest median Site EUI""")
    stl.write("""Lets take a look at how  minimum temperatures across states vary over the course of an year """)
    stl.image("EDA_Plots/statewise_min_temp.jpg", caption="Minimum temperatures over the course of an year")
    stl.write("""Lets take a look at how  maximum temperatures across states vary over the course of an year """)
    stl.image("EDA_Plots/statewise_max_temp.jpg", caption="Maximum temperatures over the course of an year")

    stl.subheader('**Heating Degree Days and Coolng Degree Days**')
    stl.image("EDA_Plots/hdd_cdd.jpg", caption="Maximum temperatures over the course of an year")

    stl.write("""Lets take a look at how across states,  median coling degree days effects median site eui """)
    stl.image("EDA_Plots/cdd_eui.jpg", caption="Median Cooling Degree Days vs median Site EUI")

    stl.write("""Lets take a look at how across states,  median heating degree days effects median site eui """)
    stl.image("EDA_Plots/hdd_eui.jpg", caption="Median Heating Degree Days vs median Site EUI")

    stl.subheader('**Precipitation and Snow**')
    stl.write("""Lets take a look at how precipitation (in inches) effects  site eui """)
    stl.image("EDA_Plots/snow.jpg", caption="Precipitation vs median Site EUI")
    stl.write("""Lets take a look at how snowfall (in inches) effects  site eui """)
    stl.image("EDA_Plots/preci.jpg", caption="Snowfall vs median Site EUI")

    stl.subheader('**Correlation between variables**')
    stl.image("EDA_Plots/corr_heatmap.jpg", caption="Correlation heatmap")

    stl.write("""Lets remove Site EUI high values (possible outliers), we see a stronger correlation """)
    stl.image("EDA_Plots/corr_heatmap2.jpg", caption="Correlation heatmap (Site EUI < 200)")

    stl.write("""Lets check correlation for high Site EUI  values (possible outliers)""")
    stl.image("EDA_Plots/corr_heatmap3.jpg", caption="Correlation heatmap (Site EUI > 200)")

    stl.header('**Conclusions**')
    stl.write("""
            6 columns are having missing values (add percentage of missing values)
            Dataset has multiple columns of correlation
            Temperatures during winter and summer correlate with each other
            Add distribution graph for numercial features
              
    """)


if __name__ == "__main__":
      main()


