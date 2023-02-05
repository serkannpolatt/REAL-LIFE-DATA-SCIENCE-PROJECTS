import cv2
import numpy as np

# Read image
image = cv2.imread('s.png')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,150,apertureSize=3)


lines_list =[]
lines = cv2.HoughLinesP(
			edges, 
			1, 
			np.pi/180, 
			threshold=100, 
			minLineLength=5, 
			maxLineGap=10 
			)

for points in lines:

	x1,y1,x2,y2=points[0]

	cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)

	lines_list.append([(x1,y1),(x2,y2)])
	
cv2.imwrite('Algilanan.png',image)
