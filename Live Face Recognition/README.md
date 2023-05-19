## English
## Live Face Recognition

### Project Description
This project aims to detect a person's face in real-time using image processing and face recognition techniques, and determine the match by comparing it with a reference image.

### Objective
The objective of this project is to perform face recognition in real-time using a camera feed, comparing it with a specific reference image to determine the match. If the detected face matches the reference image, it will display the text "MATCH!", otherwise, it will display "NO MATCH!".

### Steps

1. Camera Settings and Loading the Reference Image:
	- Configure camera settings and determine the display size.
	- Load the reference image to be used for comparison.

2. Definition of Face Matching Function:
	- Define a function called "check_face".
	-  This function performs face matching by using a given frame image and the reference image.
	-  Update the "face_match" variable based on the match result.

3. Main Loop:
	- Start an infinite loop.
	- Read frames from the camera feed.
	- Every 30 frames, start a new thread to perform face matching using the frame image.
	- Add an appropriate text to the image based on the match result for each frame.
	- Display the image on the screen with the name "video".

4. Program Termination:
	- Terminate the program when the 'q' key is pressed on the keyboard.
	- Close all windows.


> *Please note that the provided code example is a Python program and it is not provided in a directly executable format. It uses a specific reference image and a face recognition library. To run this example, you will need to install the required libraries and use your own reference image.*

## Türkçe
## Canlı Yüz Tanıma

### Proje Açıklaması
Bu proje, görüntü işleme ve yüz tanıma tekniklerini kullanarak bir kişinin yüzünü gerçek zamanlı olarak algılayıp bir referans görüntüyle karşılaştırarak eşleşme durumunu belirlemeyi amaçlamaktadır.

### Amaç
Projenin amacı, bir kamera ile gerçek zamanlı olarak alınan video akışında yüz tanıma işlemi yaparak, belirli bir referans görüntüyle karşılaştırarak eşleşme durumunu tespit etmektir. Eğer algılanan yüz, referans görüntüyle eşleşiyorsa "MATCH!" yazısı gösterilecek, eşleşme sağlanamazsa "NO MATCH!" yazısı gösterilecektir.

### Adımlar
1. Kamera Ayarları ve Referans Görüntünün Yüklenmesi:
	- Kamera ayarları yapılır ve görüntüleme boyutu belirlenir.
	- Karşılaştırma için kullanılacak referans görüntü yüklenir.

2. Yüz Eşleştirme Fonksiyonunun Tanımlanması:
	- check_face adında bir fonksiyon tanımlanır.
	- Bu fonksiyon, verilen bir kare görüntüyü ve referans görüntüyü kullanarak yüz eşleştirmesi yapar.
	- Eşleşme durumuna göre face_match değişkeni güncellenir.

3. Ana Döngü:
	- Sonsuz bir döngü başlatılır.
	- Kameradan kareler okunur.
	- Her 30 karede bir check_face fonksiyonu, kare görüntüyü kullanarak yüz eşleştirmesi yapmak üzere yeni bir iş parçacığı başlatır.
	- Her kare için eşleşme durumuna göre uygun bir yazıyı görüntüye ekler.
	- Görüntü, "video" adıyla ekranda gösterilir.

4. Programın Sonlandırılması:
	- Klavyeden 'q' tuşuna basıldığında program sonlandırılır.
	- Tüm pencereler kapatılır.


> *Lütfen unutmayın, yukarıda verilen kod örneği bir Python programıdır ve doğrudan çalıştırılabilecek bir formatta verilmemiştir. Kodda belirli bir referans görüntüsü ve yüz tanıma kütüphanesi kullanılmıştır. Bu örneği çalıştırmak için ilgili kütüphaneleri kurmanız ve kendi referans görüntünüzü kullanmanız gerekecektir.*
