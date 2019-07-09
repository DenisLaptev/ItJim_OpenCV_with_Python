import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # capture 1-st videoCam in the system
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # codac for video recording to file
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()  # ret=True or False
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    # условие выхода из цикла(нажать 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
