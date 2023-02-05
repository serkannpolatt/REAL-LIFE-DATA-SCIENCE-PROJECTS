import cv2

cap = cv2.VideoCapture('http://192.168.1.3:8080/video')
while(cap.isOpened()):
    ret, frame = cap.read()
    try:
        cv2.imshow('temp', cv2.resize(frame, (600,400)))
        key = cv2.waitKey(1)
        if key == ord ('q'):
            break
    except cv2.error:
        print("Sona Eriyor..")
        break

cap.release()
cv2.destroyAllWindows()