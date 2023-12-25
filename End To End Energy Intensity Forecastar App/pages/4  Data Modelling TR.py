import streamlit as st
import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from PIL import Image

st.set_page_config(layout="wide")
st.text("YAPIM HALİNDE 🔧⚙️")

def model_explainability():
    # Veri setini yükle
    df = pd.read_csv("train.csv")

    # Bağımsız değişkenler ve bağımlı değişkeni belirle
    X = df.drop("site_eui", axis=1)
    y = df["site_eui"]

    # Kategorik özellikleri doldur
    imputer = SimpleImputer(strategy="most_frequent")
    X_filled = imputer.fit_transform(X)

    # Doldurulmuş veriyi DataFrame formatına dönüştür
    X_filled = pd.DataFrame(X_filled, columns=X.columns)

    # Kategorik özellikleri sayısal özelliklere dönüştür
    label_encoder = LabelEncoder()
    X_encoded = X_filled.apply(label_encoder.fit_transform)

    # Eğitim ve test veri setlerini oluştur
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # AutoGluon kullanarak regresyon modeli oluştur ve eğit
    train_data = TabularDataset('train.csv')
    predictor = TabularPredictor(label='site_eui').fit(train_data, time_limit=120)  # Fit models for 120s

    # Eğitim veri seti üzerinde tahmin yap
    autogluon_train_predictions = predictor.predict(X_train)

    # Test veri seti üzerinde tahmin yap
    autogluon_test_predictions = predictor.predict(X_test)

    # AutoGluon'un tahmin performansını değerlendir
    autogluon_train_mse = mean_squared_error(y_train, autogluon_train_predictions)
    autogluon_test_mse = mean_squared_error(y_test, autogluon_test_predictions)

    # Diğer modelleri oluştur ve eğit
    decision_tree = DecisionTreeRegressor()
    random_forest = RandomForestRegressor()
    linear_regression = LinearRegression()
    gradient_boosting = GradientBoostingRegressor()
    svr = SVR()
    elastic_net = ElasticNet()
    knn = KNeighborsRegressor()

    decision_tree.fit(X_train, y_train)
    random_forest.fit(X_train, y_train)
    linear_regression.fit(X_train, y_train)
    gradient_boosting.fit(X_train, y_train)
    svr.fit(X_train, y_train)
    elastic_net.fit(X_train, y_train)
    knn.fit(X_train, y_train)

    # Diğer modellerle tahmin yap
    dt_test_predictions = decision_tree.predict(X_test)
    rf_test_predictions = random_forest.predict(X_test)
    lr_test_predictions = linear_regression.predict(X_test)
    gb_test_predictions = gradient_boosting.predict(X_test)
    svr_test_predictions = svr.predict(X_test)
    en_test_predictions = elastic_net.predict(X_test)
    knn_test_predictions = knn.predict(X_test)

    # Diğer modellerin tahmin performansını değerlendir
    dt_mse = mean_squared_error(y_test, dt_test_predictions)
    rf_mse = mean_squared_error(y_test, rf_test_predictions)
    lr_mse = mean_squared_error(y_test, lr_test_predictions)
    gb_mse = mean_squared_error(y_test, gb_test_predictions)
    svr_mse = mean_squared_error(y_test, svr_test_predictions)
    en_mse = mean_squared_error(y_test, en_test_predictions)
    knn_mse = mean_squared_error(y_test, knn_test_predictions)

    # Grafik ve tablo oluşturma
    data = {
        'Model': ['AutoGluon', 'Decision Tree', 'Random Forest', 'Linear Regression', 'Gradient Boosting', 'SVR', 'ElasticNet', 'KNN'],
        'MSE': [autogluon_test_mse, dt_mse, rf_mse, lr_mse, gb_mse, svr_mse, en_mse, knn_mse]
    }
    df_results = pd.DataFrame(data)

    # Sütun grafiği
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Model', y='MSE', data=df_results, ax=ax)
    ax.set_xlabel('Model')
    ax.set_ylabel('Mean Squared Error')
    ax.set_title('Model Karşılaştırması')
    ax.set_ylim(bottom=0)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Tablo
    st.write(df_results)

    # Sonuçları yazdır
    st.write("AutoGluon - Eğitim veri seti MSE:", autogluon_train_mse)
    st.write("AutoGluon - Test veri seti MSE:", autogluon_test_mse)
    st.write("Decision Tree - Test veri seti MSE:", dt_mse)
    st.write("Random Forest - Test veri seti MSE:", rf_mse)
    st.write("Linear Regression - Test veri seti MSE:", lr_mse)
    st.write("Gradient Boosting - Test veri seti MSE:", gb_mse)
    st.write("SVR - Test veri seti MSE:", svr_mse)
    st.write("ElasticNet - Test veri seti MSE:", en_mse)
    st.write("KNN - Test veri seti MSE:", knn_mse)

def main():
    model_explainability()

if __name__ == "__main__":
    main()
