import cv2
import numpy as np

# Access the camera using the app
cap = cv2.VideoCapture('http://192.168.1.3:8080/video')

while True:
    # Capture an image from the camera
    ret, frame = cap.read()

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur the image to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    # Detect straight lines
    lines = cv2.HoughLines(blurred, 1, np.pi/180, 50)

    # Draw the lines on the image
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Show the image with the lines
    cv2.imshow("Lines", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()
