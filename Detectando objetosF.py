import cv2
import serial
import time
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
 
ser= serial.Serial("COM4",9600,timeout=1)
time.sleep(2)

pinguinoClassif = cv2.CascadeClassifier('cascade.xml')

while True:
	
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	toy = pinguinoClassif.detectMultiScale(gray,scaleFactor = 7, minNeighbors = 400,minSize=(70,88))

	for (x,y,w,h) in toy:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		cv2.putText(frame,'Pinguino',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
		ser.write(b"N")
	cv2.imshow('frame',frame)
	
	if cv2.waitKey(0) == 27:
		break
	else:
		print("No hay nada")
		ser.write(b"P")
	
	
	


cap.release()
cv2.destroyAllWindows()
ser.close()