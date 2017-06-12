import numpy as np
import cv2

def sketch(image):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gblur = cv2.GaussianBlur(gray, (5,5), 0)
    cedges = cv2.Canny(gblur, 10, 70)
    ret, mask = cv2.threshold(cedges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture('data/video/DJI_0001.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame',sketch(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
