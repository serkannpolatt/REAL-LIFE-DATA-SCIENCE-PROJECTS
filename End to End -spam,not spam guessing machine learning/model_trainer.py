from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB

# Model training function
# Model eğitim fonksiyonu
def run_model_training(X_train, X_test, y_train, y_test):
    # Initialize the MultinomialNB model
    # MultinomialNB modelini başlatın
    clf = MultinomialNB()
    
    # Fit the model with training data
    # Modeli eğitin
    clf.fit(X_train,y_train)
    
    # Evaluate model accuracy on the test set
    # Test setindeki model doğruluğunu değerlendirin
    clf.score(X_test,y_test)
    
    # Make predictions on the test set
    # Test setinde tahminler yapın
    y_pred = clf.predict(X_test)
    
    # Print classification report to evaluate precision, recall and F1-score
    # Hassasiyeti, hatırlamayı ve F1 puanını değerlendirmek için sınıflandırma raporunu yazdırın
    print(classification_report(y_test, y_pred))

    return clf
