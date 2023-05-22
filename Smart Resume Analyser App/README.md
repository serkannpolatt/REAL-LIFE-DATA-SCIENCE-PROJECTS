## English
## Smart Resume Analyzer

### Introduction
The code provided implements a Smart Resume Analyzer application using Streamlit, a web application framework for Python. The purpose of this application is to analyze resumes in PDF format and provide recommendations based on the resume content. It utilizes various libraries and functionalities to extract information from resumes, generate recommendations for skills and courses, and store user data in a MySQL database.

### Features and Functionality
- Uploading and displaying resumes in PDF format
- Extracting basic information from resumes, such as name, email, and contact details
- Analyzing the resume to determine the level of the candidate (Fresher, Intermediate, or Experienced)
- Recommending skills based on the content of the resume
- Recommending courses and certificates related to specific fields (Data Science, Web Development, Android Development, iOS Development, UI/UX Development)
- Providing resume tips and ideas to improve the resume content
- Storing user data, including name, email, resume score, timestamp, number of pages, predicted field, user level, actual skills, recommended skills, and recommended courses, in a MySQL database

### Dependencies and Libraries
The code requires the following libraries to be installed:

- **streamlit:** Used for creating the web application interface
- **pandas:** Used for data manipulation and analysis
- **base64:** Used for encoding and decoding data in base64 format
- **time, datetime:** Used for working with dates and timestamps
- **pyresparser:** Used for parsing resume content
- **pdfminer3:** Used for extracting text from PDF files
- **io:** Used for handling file streams
- **streamlit_tags:** Used for creating tag inputs in Streamlit
- **PIL (Python Imaging Library):** Used for working with images
- **pymysql:** Used for connecting to MySQL database
- **pafy:** Used for fetching YouTube video information
- **plotly.express:** Used for data visualization

### Code Structure
The code is structured into different functions for each specific functionality:

- **fetch_yt_video(link):** Fetches the title of a YouTube video given its link.
- **get_table_download_link(df, filename, text):** Generates a link allowing the data in a Pandas DataFrame to be downloaded as a CSV file.
- **pdf_reader(file):** Reads the text content of a PDF file.
- **show_pdf(file_path):** Displays a PDF file in the Streamlit interface.
- **course_recommender(course_list):** Recommends courses and certificates based on a provided list of courses.
- **insert_data(name, email, res_score, timestamp, no_of_pages, reco_field, cand_level, skills, recommended_skills, courses):** Inserts user data into the MySQL database.
- **run():** The main function that runs the Streamlit application.

The code also includes the necessary configurations and setups for the Streamlit application, such as setting the page title and icon, creating the database and table if they don't exist, and defining the layout and functionality of the Streamlit app.

### Usage
To use the Smart Resume Analyzer application, you need to run the run() function. This will start the Streamlit web application and display the user interface in the browser. You can then choose between being a "Normal User" or an "Admin" and proceed accordingly. The application allows you to upload a resume in PDF format and provides various recommendations and analysis based on the resume content.

> *Note: This readme provides an overview of the code and its purpose. It does not include specific instructions on how to set up the application and its dependencies. Make sure you have all the necessary libraries installed and set up a MySQL database with the appropriate credentials before running the code.*

## Türkçe 
## Akıllı Özgeçmiş Analizörü

### Giriş
Sağlanan kod, Python için bir web uygulama çerçevesi olan Streamlit kullanılarak Akıllı Özgeçmiş Analizörü uygulamasını uygular. Bu uygulamanın amacı, PDF formatındaki özgeçmişleri analiz etmek ve özgeçmiş içeriğine dayalı öneriler sunmaktır. Özgeçmişlerden bilgi çıkarmak, beceri ve kurs önerileri oluşturmak ve kullanıcı verilerini bir MySQL veritabanında depolamak için çeşitli kütüphane ve işlevleri kullanır.

### Özellikler ve İşlevsellik
- PDF formatındaki özgeçmişleri yüklemek ve görüntülemek
- Özgeçmişlerden ad, e-posta ve iletişim bilgileri gibi temel bilgileri çıkarmak
- Adayın seviyesini (Yeni mezun, Orta düzey veya Deneyimli) belirlemek için özgeçmişi analiz etmek
- Özgeçmiş içeriğine dayalı beceri önerilerinde bulunmak
- Veri Bilimi, Web Geliştirme, Android Geliştirme, iOS Geliştirme, UI/UX Geliştirme gibi belirli alanlarla ilgili kurs ve sertifikalar önermek
- Özgeçmiş içeriğini geliştirmek için özgeçmiş ipuçları ve fikirleri sağlamak
- Kullanıcı verilerini bir MySQL veritabanında depolamak (ad, e-posta, özgeçmiş puanı, zaman damgası, sayfa sayısı, tahmin edilen alan, kullanıcı seviyesi, gerçek beceriler, önerilen beceriler ve önerilen kurslar)

### Bağımlılıklar ve Kütüphaneler
Kodun çalışması için aşağıdaki kütüphanelerin kurulu olması gerekmektedir:

- **streamlit:** Web uygulama arayüzü oluşturmak için kullanılır
- **pandas:** Veri manipülasyonu ve analizi için kullanılır
- **base64:** Verileri base64 formatında kodlama ve kod çözme işlemleri için kullanılır
- **time, datetime:** Tarih ve zaman damgalarıyla çalışmak için kullanılır
- **pyresparser:** Özgeçmiş içeriğini ayrıştırmak için kullanılır
- **pdfminer3:** PDF dosyalarından metin çıkarmak için kullanılır
- **io:** Dosya akışlarını işlemek için kullanılır
- **streamlit_tags:** Streamlit'te etiket girişleri oluşturmak için kullanılır
- **PIL (Python Imaging Library):** Görsellerle çalışmak için kullanılır
- **pymysql:** MySQL veritabanına bağlanmak için kullanılır
- **pafy:** YouTube video bilgisi almak için kullanılır
- **plotly.express:** Veri görselleştirme için kullanılır

### Kod Yapısı
Kod, her bir özel işlev için farklı işlevlere bölünmüştür:

- **fetch_yt_video(link):** Verilen bir bağlantıya sahip bir YouTube videosunun başlığını alır.
- **get_table_download_link(df, filename, text):** Pandas DataFrame içindeki verilerin CSV dosyası olarak indirilmesine izin veren bir bağlantı oluşturur.
- **pdf_reader(file):** Bir PDF dosyasının metin içeriğini okur.
- **show_pdf(file_path):** Bir PDF dosyasını Streamlit arayüzünde görüntüler.
- **course_recommender(course_list):** Belirtilen bir kurs listesine dayalı olarak kurs ve sertifikalar önerir.
- **insert_data(name, email, res_score, timestamp, no_of_pages, reco_field, cand_level, skills, recommended_skills, courses):** Kullanıcı verilerini MySQL veritabanına ekler.
- **run():** Streamlit uygulamasını çalıştıran ana işlev.

Kod ayrıca Streamlit uygulamasının gereken yapılandırmalarını ve ayarlamalarını da içerir. Sayfa başlığını ve simgesini ayarlama, veritabanını ve tabloyu oluşturma (varsa), Streamlit uygulamasının düzenini ve işlevselliğini tanımlama gibi.

### Kullanım
Akıllı Özgeçmiş Analizörü uygulamasını kullanmak için run() işlevini çalıştırmanız gerekmektedir. Bu, Streamlit web uygulamasını başlatacak ve kullanıcı arayüzünü tarayıcıda görüntüleyecektir. Ardından "Normal Kullanıcı" veya "Yönetici" olarak seçim yapabilir ve buna göre devam edebilirsiniz. Uygulama, PDF formatında bir özgeçmiş yüklemenize ve özgeçmiş içeriğine dayalı çeşitli öneriler ve analizler sunmanıza olanak tanır.

> *Not: Bu readme, kodun genel bir özetini ve amacını içermektedir. Uygulamanın ve bağımlılıklarının nasıl kurulacağına dair belirli talimatlar içermemektedir. Kodu çalıştırmadan önce gerekli tüm kütüphanelerin kurulu olduğundan ve uygun kimlik bilgilerine sahip bir MySQL veritabanı oluşturulduğundan emin olun.*
