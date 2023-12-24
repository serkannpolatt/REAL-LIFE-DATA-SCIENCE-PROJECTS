import streamlit as stl 
stl.set_page_config(layout="wide")

stl.header("Data Preproccessing & Feature Engineering")

stl.subheader("EDA Recap")
stl.write("""Some important conclusions from EDA
          6 Columns have missing values
          Elevation column correlates pretty well with Site EUI (*)
          Days with fog has missing values, it needs to be filled using knnimputer, the rest 3 columns missing values can be handled by mode values and as most of the vlaues are 1
          We remove facility type clumn, as this categorical column has high dimensionality and can intriduce noise in the model
          Days with above 110F can also be removed
        """)

stl.subheader("Handling Missing Values")

stl.write("Percentage of missing values in the dataset")
stl.image("EDA_Plots/Missing_values.jpg")

stl.write("""The first step is to remove features with significant missing values (with over 50% missing values), and then use data filling techniques to handle the rest.
          We can use KNNImputer to fill the missing values in features with type numerical values,KNNImputer fills the values by observing trends in reated features. But as more than 50 percent of values are missing, we would introduce lot of noissy patterns in the data. 
          Removing the features is the best solution in this case
          
          \n 
          """)

stl.subheader("Filling Missing Values")
stl.write("""
          We fill the NULL values of categorical values by prediciting them. A simple regression model is built on rest of the models to fill the missing vlaues. We fill the features year_built and energy_star_rating with this method.  """)

# stl.subheader("Removing some Features")

stl.write("Removing Noisy Features")
stl.write("""
        The First step is to remove features: Year Factor, Facility Type, Days Above 110 F. \n
          Facility type column is a categorical column with high dimensionality and can introduce noissy patterns in the model \n.
          All data samples in the training set have Year Factor feature as value '7', but we do not have any data sample in the training set with value '7' \n
          We remove Year Factor feature, as this is an anonymised feature. There is no way to map this feature to its original value. hence, the user input of year faactor is unuseable for us. So we drop this for our model 
         """)


stl.subheader("Feature Engineering")
stl.subheader("Handling Multi Collinearity")
stl.write("""
The first step is to identify highly correlated features. To handle multi-collinearity problem, we use Variance Inflation Factor(VIF). This way, we identify features with VIF values greater than 4.
\n
Seasonal columns are highly correlated with each other. Aggregating these columns will not only handle multi collinearity but wil also reduce the total number features for our model, making the prediction application simple to use for users
We create a new feature Avg_min_temp_winter by aggregating features january_min_temp,february_min_temp,march_min_temp ,  april_min_temp,october_min_temp,november_min_temp,december_min_temp. The aggregation is done using average. 

Simillarly we create a new feature Avg_max_temp_winter by aggregating features january_max_temp,february_max_temp,march_max_temp, april_max_temp,october_max_temp,november_max_temp,december_max_temp; 
Avg_temp_winter by aggregating features january_avg_temp,february_avg_temp,march_avg_temp ,april_avg_temp,october_avg_temp,november_avg_temp,december_avg_temp; 
Avg_min_temp_summer by aggregating features may_min_temp,june_min_temp,july_min_temp,august_min_temp,september_min_temp;  
Avg_max_temp_summer by aggregating features may_max_temp,june_max_temp,july_max_temp,august_max_temp,september_max_temp; 
Avg_temp_summer by aggregating features may_avg_temp,june_avg_temp,july_avg_temp,august_avg_temp,september_avg_temp; 
Avg_days_below30F by aggregating features days_below_30F,days_below_20F,days_below_10F,days_below_0F; 
""")
stl.write("At the end, we have the following features to build the model:")
stl.write("(add features here)")


