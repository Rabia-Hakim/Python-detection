import cv2

face_Cascade = cv2.CascadeClassifier("haarcascade_frontalface_good.xml")

#Connect to the camera
mycam = cv2.VideoCapture(0)

#take photo and save in image variable
image, mypicture = mycam.read()
imgGray = cv2.cvtColor(mypicture, cv2.COLOR_BGR2GRAY)

#detect the face
faces = face_Cascade.detectMultiScale(imgGray, 1.1, 4)

#draw the rectangle
for (x, y, w, h) in faces:
  cv2.rectangle(mypicture, (x, y), (x + w, y + h), (255, 16, 240), 3)
cv2.imwrite('mypicture.png', mypicture)
cv2.imshow("myphoto", mypicture)
cv2.waitKey(0)
tst
