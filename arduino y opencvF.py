import cv2
import serial
import time
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
 
ser= serial.Serial("COM5",9600,timeout=1)
time.sleep(2)

pythonClassifi = cv2.CascadeClassifier('cascade.xml')



while True:
	
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	python = pythonClassifi.detectMultiScale(gray,scaleFactor = 1.1 ,minNeighbors = 400,minSize=(500,80))
	

	for (x,y,w,h) in python:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		cv2.putText(frame,'Python',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
		ser.write(b"P")
	cv2.imshow('Python',frame)

    #Para agregar otro objeto solo debes añadir el codigo anterior
	
	if cv2.waitKey(0) == 27:
		break


cap.release()
cv2.destroyAllWindows()
ser.close()