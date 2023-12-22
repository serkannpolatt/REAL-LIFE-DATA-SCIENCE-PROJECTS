import streamlit as stl 
stl.set_page_config(layout="wide")

import pandas as pd

stl.header('**Data Collection**')

stl.write("""
            Dataset is sourced from [WiDS Datathon 2022](https://www.kaggle.com/competitions/widsdatathon2022) and contains over 100k data samples.

        """)

stl.subheader('Background') 
stl.write("""
According to a report issued by the International Energy Agency (IEA), the lifecycle of buildings from construction to demolition were responsible for 37% of global energy-related and process-related CO2 emissions in 2020. Yet it is possible to drastically reduce the energy consumption of buildings by a combination of easy-to-implement fixes and state-of-the-art strategies. For example, retrofitted buildings can reduce heating and cooling energy requirements by 50-90 percent. Many of these energy efficiency measures also result in overall cost savings and yield other benefits, such as cleaner air for occupants. This potential can be achieved while maintaining the services that buildings provide.[1](https://www.kaggle.com/competitions/widsdatathon2022) and contains over 100k data samples.

        """)
stl.subheader('Overview: Dataset and Challenge') 
stl.write("""
The WiDS Datathon dataset was created in collaboration with Climate Change AI (CCAI) and Lawrence Berkeley National Laboratory (Berkeley Lab). WiDS Datathon participants will analyze differences in building energy efficiency, creating models to predict building energy consumption. Participants will use a dataset consisting of variables that describe building characteristics and climate and weather variables for the regions in which the buildings are located. Accurate predictions of energy consumption can help policymakers target retrofitting efforts to maximize emissions reductions.[1](https://www.kaggle.com/competitions/widsdatathon2022) .

        """)
stl.subheader('Dependent Variable') 
stl.write("""
Site Energy Intensity (Site EUI) is the dependent variable we are are trying to predict.

Site energy intensity is an important metric to measure for any building to understand its energy utilization and identify opportunities for energy efficiency. It also gives us an indication of the building’s overall CO2 emissions and helps us control the emissions.

Site EUI is a measure that is a function of a building’s energy intensity as the size of the building. Site EUI depends upon various characteristics of the building and weather-related factors of location. In this article, we will develop a data science solution to predict site EUI using machine learning techniques and then deploy the model on a cloud platform for inference. So let’s get started with this exciting project.[1](https://www.kaggle.com/competitions/widsdatathon2022) .

        """)
stl.subheader('Independent Variables') 
stl.write("""
id: building id \n
Year_Factor: an anonymized year in which the weather and energy usage factors were observed\n
State_Factor: anonymized state in which the building is located\n
building_class: building classification\n
facility_type: building usage type\n
floor_area: floor area (in square feet) of the building\n
year_built: a year in which the building was constructed\n
energy_star_rating: the energy star rating of the building\n
ELEVATION: elevation of the building location\n
january_min_temp: minimum temperature in January (in Fahrenheit) at the location of the building\n
january_avg_temp: the average temperature in January (in Fahrenheit) at the location of the building\n
january_max_temp: maximum temperature in January (in Fahrenheit) at the location of the building\n
cooling_degree_days: cooling degree day for a given day is the number of degrees where the daily average temperature exceeds 65 degrees Fahrenheit. Each month is summed to produce an annual total at the location of the building.\n
heating_degree_days: heating degree day for a given day is the number of degrees where the daily average temperature falls under 65 degrees Fahrenheit. Each month is summed to produce an annual total at the location of the building.\n
precipitation_inches: annual precipitation in inches at the location of the building\n
snowfall_inches: annual snowfall in inches at the location of the building\n
snowdepth_inches: annual snow depth in inches at the location of the building\n
avg_temp: average temperature over a year at the location of the building\n
days_below_30F: total number of days below 30 degrees Fahrenheit at the location of the building\n
days_below_20F: total number of days below 20 degrees Fahrenheit at the location of the building\n
days_below_10F: total number of days below 10 degrees Fahrenheit at the location of the building\n
days_below_0F: total number of days below 0 degrees Fahrenheit at the location of the building\n
days_above_80F: total number of days above 80 degrees Fahrenheit at the location of the building\n
days_above_90F: total number of days above 90 degrees Fahrenheit at the location of the building\n
days_above_100F: total number of days above 100 degrees Fahrenheit at the location of the building\n
days_above_110F: total number of days above 110 degrees Fahrenheit at the location of the building\n
direction_max_wind_speed: wind direction for maximum wind speed at the location of the building. Given in 360-degree\n
compass point directions (e.g. 360 = north, 180 = south, etc.).\n
direction_peak_wind_speed: wind direction for peak wind gust speed at the location of the building. Given in 360-degree compass point directions (e.g. 360 = north, 180 = south, etc.).\n
max_wind_speed: maximum wind speed at the location of the building\n
days_with_fog: number of days with fog at the location of the building [1](https://www.kaggle.com/competitions/widsdatathon2022) \n
""")

stl.header('**Dataset**')
df = pd.read_csv("train.csv")
stl.write(df)
stl.write('---')