## English
## Army PDF Data Extraction
This code snippet demonstrates the extraction of data from a PDF file using the PyPDF2 library and the subsequent data manipulation using pandas and numpy libraries. The code performs the following tasks:

### Extracting PDF Information
1. The PDF file path is specified using the variable file_path.
2. The code opens the PDF file using a PdfReader object from the PyPDF2 library.
3. The number of pages in the PDF file is determined using len(reader.pages).
4. The number of pages is printed to the console.

### Data Manipulation
1. The extracted text from the first page of the PDF is stored in the variable page_content.
2. The page_content is split into rows based on a specific pattern using the re.split() function.
3. The resulting rows are split into columns using the comma separator.
4. The resulting data is stored in a pandas DataFrame called df_text.

### Cleaning and Formatting Data
1. Two new DataFrames, df_mos and df_date, are created as copies of df_text.
2. The first row of both DataFrames is dropped as it contains headers.
3. Regular expressions are used to clean the data in the MOS column of df_mos and the Date column of df_date.
4. Unnecessary characters, numbers, and whitespace are removed from the columns using regular expressions.
5. The columns are renamed to "MOS" and "Date", respectively.
6. The indices of both DataFrames are reset to allow for proper column binding.
7. The cleaned DataFrames df_mos and df_date are merged with the original DataFrame df_all using the pd.concat() function.
8. The resulting DataFrame contains columns for Name, First Name, Middle Name, Last Name, Suffix, MOS, and Date.


Please note that this code assumes the presence of the necessary libraries and a PDF file named "army.pdf" in the specified path. You may need to modify the code to suit your specific requirements, such as changing the file path or handling different PDF structures.

> *Note: The interpretation and application of the extracted data may vary depending on the specific context and requirements of the project.*

## Türkçe
## Ordu PDF Veri Çıkarımı
Bu kod parçacığı, PyPDF2 kütüphanesi kullanarak bir PDF dosyasından veri çıkarımını ve ardından pandas ve numpy kütüphanelerini kullanarak veri manipülasyonunu göstermektedir. Kod aşağıdaki görevleri gerçekleştirir:

### PDF Bilgilerinin Çıkarılması
1. PDF dosya yolu file_path değişkeni kullanılarak belirtilir.
2. Kod, PyPDF2 kütüphanesinden bir PdfReader nesnesi kullanarak PDF dosyasını açar.
3. PDF dosyasındaki sayfa sayısı len(reader.pages) kullanılarak belirlenir.
4. Sayfa sayısı konsola yazdırılır.

### Veri Manipülasyonu
1. PDF'nin ilk sayfasından çıkarılan metin page_content değişkeninde saklanır.
2. re.split() fonksiyonu kullanarak page_content belirli bir desene göre satırlara bölünür.
3. Elde edilen satırlar virgül ayırıcısıyla sütunlara bölünür.
4. Elde edilen veriler, df_text adlı bir pandas DataFrame'inde saklanır.

### Verinin Temizlenmesi ve Biçimlendirilmesi
1. df_text kopyası olarak iki yeni DataFrame oluşturulur: df_mos ve df_date.
2. Her iki DataFrame'in ilk satırı başlık içerdiği için düşürülür.
3. df_mos'un MOS sütunu ve df_date'in Date sütunu içindeki verileri temizlemek için düzenli ifadeler kullanılır.
4. Gereksiz karakterler, sayılar ve boşluklar düzenli ifadeler kullanılarak sütunlardan kaldırılır.
5. Sütunlar sırasıyla "MOS" ve "Date" olarak yeniden adlandırılır.
6. Her iki DataFrame'in dizinleri, uygun sütun bağlamı için sıfırlanır.
7. Temizlenmiş df_mos ve df_date DataFrame'leri, pd.concat() fonksiyonu kullanılarak orijinal df_all DataFrame'ine birleştirilir.
8. Elde edilen DataFrame, Name, First Name, Middle Name, Last Name, Suffix, MOS ve Date sütunlarını içerir.

Lütfen bu kodun, gerekli kütüphanelerin ve belirtilen yol içinde "army.pdf" adında bir PDF dosyasının mevcut olduğunu varsaydığını unutmayın. Dosya yolu değiştirilmesi veya farklı PDF yapılarına uyum sağlanması gibi özel gereksinimlerinize göre kodu düzenlemeniz gerekebilir.

> *Not: Elde edilen verinin yorumlanması ve uygulanması, projenin belirli bağlamı ve gereksinimleri doğrultusunda değişebilir.*
