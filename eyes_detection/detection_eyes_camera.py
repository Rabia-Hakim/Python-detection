# import required libraries
import cv2

eye_cascade = cv2.CascadeClassifier("classifier_eyes_good.xml")

# connects to camera
mycam = cv2.VideoCapture(0)

# take photo and save in image variable
result, mypicture = mycam.read()
imGray = cv2.cvtColor(mypicture, cv2.COLOR_BGR2GRAY)

#detect the face
eyes = eye_cascade.detectMultiScale(imGray, 1.1, 4)

#draw the rectangle
for (x, y, w, h) in eyes:
  cv2.rectangle(mypicture, (x, y), (x + w, y + h), (255, 16, 240), 3)

cv2.imwrite('mypicture.png', mypicture)
cv2.imshow("myphoto", mypicture)
cv2.waitKey(0)