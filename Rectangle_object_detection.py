import numpy as nm
import cv2

print("Object dectection by Rectangle")
color = (0,0,0)
line_width = 4
#radius = 50
#h = (10,15)
#w = (10,30)
point = (50,50)
point2 = (150,150)
cap = cv2.VideoCapture(0)

def click(event, x, y, flags, param):
	global pressed, point, point2

	if event == cv2.EVENT_RBUTTONDOWN:
		print("Pressed", x, y)
		point = (x,y)
		point2 = (x+100,y+100)


cv2.namedWindow("PointOut")
cv2.setMouseCallback("PointOut",click)

while(True):
	retina,frame = cap.read()
	frame = cv2.resize(frame,(0,0), fx = 0.75, fy = 0.75)
	cv2.rectangle(frame,point,point2,color,line_width)
	cv2.imshow("PointOut", frame)
	ch = cv2.waitKey(1)
	if ch == ord('b'):
		break
cap.release()
cv2.destroyAllWindows()
