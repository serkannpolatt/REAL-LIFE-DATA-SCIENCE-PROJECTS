import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz
from PIL import Image

st.set_page_config(layout="wide")
st.text("UNDER CONSTRUCTION 🔧⚙️")

def model_explainability():
    # Load the dataset
    df = pd.read_csv("train.csv")

    # Define the independent and dependent variables
    X = df.drop("site_eui", axis=1)
    y = df["site_eui"]

    # Fill categorical features
    imputer = SimpleImputer(strategy="most_frequent")
    X_filled = imputer.fit_transform(X)

    # Convert filled data to DataFrame format
    X_filled = pd.DataFrame(X_filled, columns=X.columns)

    # Convert categorical features to numerical features
    label_encoder = LabelEncoder()
    X_encoded = X_filled.apply(label_encoder.fit_transform)

    # Create training and test datasets
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # Create and train the Linear Regression model
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    # Create and train the Decision Tree Regression model
    tree_model = DecisionTreeRegressor()
    tree_model.fit(X_train, y_train)

    # Create and train the Random Forest Regression model
    forest_model = RandomForestRegressor()
    forest_model.fit(X_train, y_train)

    # Make predictions on the training dataset
    linear_train_predictions = linear_model.predict(X_train)
    tree_train_predictions = tree_model.predict(X_train)
    forest_train_predictions = forest_model.predict(X_train)

    # Make predictions on the test dataset
    linear_test_predictions = linear_model.predict(X_test)
    tree_test_predictions = tree_model.predict(X_test)
    forest_test_predictions = forest_model.predict(X_test)

    # Calculate mean squared error (MSE) for the training dataset
    linear_train_mse = mean_squared_error(y_train, linear_train_predictions)
    tree_train_mse = mean_squared_error(y_train, tree_train_predictions)
    forest_train_mse = mean_squared_error(y_train, forest_train_predictions)

    # Calculate mean squared error (MSE) for the test dataset
    linear_test_mse = mean_squared_error(y_test, linear_test_predictions)
    tree_test_mse = mean_squared_error(y_test, tree_test_predictions)
    forest_test_mse = mean_squared_error(y_test, forest_test_predictions)

    # Print the results
    st.write("Linear Regression - Training dataset MSE:", linear_train_mse)
    st.write("Decision Tree Regression - Training dataset MSE:", tree_train_mse)
    st.write("Random Forest Regression - Training dataset MSE:", forest_train_mse)
    st.write("Linear Regression - Test dataset MSE:", linear_test_mse)
    st.write("Decision Tree Regression - Test dataset MSE:", tree_test_mse)
    st.write("Random Forest Regression - Test dataset MSE:", forest_test_mse)

    # Print the coefficients of the Linear Regression model
    coefficients = linear_model.coef_
    st.write("Linear Regression - Coefficients:", coefficients)

    # Visualize the Decision Tree Regression model
    dot_data = export_graphviz(tree_model, out_file=None, feature_names=X_encoded.columns)
    st.graphviz_chart(dot_data)

    # Visualize feature importance of the Random Forest Regression model
    importances = forest_model.feature_importances_
    feature_names = X_encoded.columns

    plt.figure(figsize=(10, 6))
    plt.bar(feature_names, importances)
    plt.xticks(rotation=90)
    plt.xlabel("Features")
    plt.ylabel("Importance Level")
    plt.title("Random Forest Regression - Feature Importance Levels")
    st.pyplot(plt)

def main():
    model_explainability()

if __name__ == "__main__":
    main()
