# Import required packages and modules
# Gerekli kütüphaneler ve modüller import ediliyor
import packages.data_processor as dp  # Module for data processing / Veri işleme için gereken modül
import streamlit as st  # Streamlit library / Streamlit kütüphanesi
import joblib  # Required library for loading the model / Modelin yüklenmesi için gerekli olan joblib kütüphanesi
import os  # os module for changing the file path / Dosya yolu değiştirmek için gerekli olan os modülü

# Change the working directory
# Çalışma dizini değiştiriliyor
os.chdir("C://Users//Serkan POLAT//Desktop//SSD")

# Load the model
# Modeli yükle
spam_clf = joblib.load(open('models/my_spam_model.pkl', 'rb'))

# Load the vectorizer
# Vektörleştirici yükleniyor
vectorizer = joblib.load(open('vectors/my_vectorizer.pickle', 'rb'))

### MAIN FUNCTION ###
def main(title="Text classification App for demo".upper()):
    # Create the application title and center-align it
    # Uygulama başlığı oluşturuluyor ve merkezde hizalanıyor
    st.markdown("<h1 style='text-align: center; font-size: 25px; color: blue;'>{}</h1>".format(title),
                unsafe_allow_html=True)
    st.image("images\myimage.png", width=100)
    info = ''

    with st.expander("1. Check if your text is a spam or not spam / Metninizin spam olup olmadığını kontrol edin 😀"):
        text_message = st.text_input("Please enter your message / Lütfen mesajınızı girin")
        if st.button("Predict / Tahmin"):
            # Perform prediction on the input text
            # Giriş metni üzerinde tahminleme yapılıyor
            prediction = spam_clf.predict(vectorizer.transform([text_message]))

            if prediction[0] == 0:
                info = 'NOT SPAM / SPAM DEĞİL'  # It's not spam
            else:
                info = 'SPAM'  # It's spam
            st.success('Prediction / Tahmin: {}'.format(info))

if __name__ == "__main__":
    main()
