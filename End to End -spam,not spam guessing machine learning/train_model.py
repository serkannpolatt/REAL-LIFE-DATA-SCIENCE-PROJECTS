# Packages
# Gerekli kütüphaneler
import os  # Operating system module for changing the file path / Dosya yolu değiştirmek için işletim sistemi modülü
os.chdir("C://Users//Serkan POLAT//Desktop//SSD")  # Change the working directory / Çalışma dizinini değiştir

import joblib  # Joblib library for loading and saving models / Modelleri yükleme ve kaydetme için Joblib kütüphanesi

# Get customized functions from library
# Kütüphaneden özelleştirilmiş fonksiyonları al
import packages.data_processor as dp  # Custom module for data processing / Veri işleme için özelleştirilmiş modül
import packages.model_trainer as mt  # Custom module for model training / Model eğitimi için özelleştirilmiş modül

# 0.Path to data
# 0. Veri yolunu belirt
path_to_data = 'data/input_spam.csv'

# 1.Prepare the data
# 1. Veriyi hazırla
prepared_data = dp.prepare_data(path_to_data, encoding="latin-1")

# 2.Create train - test split
# 2. Eğitim ve test veri setlerini oluştur
train_test_data, vectorizer = dp.create_train_test_data(prepared_data['text'], prepared_data['label'], 0.33, 2021)

# 3.Run training
# 3. Eğitimi başlat
model = mt.run_model_training(train_test_data['x_train'], train_test_data['x_test'], train_test_data['y_train'], train_test_data['y_test'])

# 4.Save the trained model and vectorizer
# 4. Eğitilmiş modeli ve vektörleştiriciyi kaydet
joblib.dump(model, './models/my_spam_model.pkl')
joblib.dump(vectorizer, open("./vectors/my_vectorizer.pickle", "wb"))
