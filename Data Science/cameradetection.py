import cv2





def detectPlanes(gray):
    # Görüntüyü bulanıklaştır
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Düz alanları algıla
    ret, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Sadece düz alanları döndür
    planes = []
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            planes.append(contour)

    return planes

# Kamera objesini oluştur
cap = cv2.VideoCapture(0)

while True:
    # Kameradan görüntü al
    ret, frame = cap.read()

    # Görüntüyü gri seviyesine dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Düz alanları algıla (detectPlanes)
    planes = detectPlanes(gray)

    # Bulunan düz alanları resme çiz
    for plane in planes:
        cv2.drawContours(frame, [plane], -1, (0, 255, 0), 2)

    # Görüntüyü ekranda göster
    cv2.imshow("Planes", frame)

    # 'q' tuşuna basılınca döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı kapat
cap.release()
cv2.destroyAllWindows()




