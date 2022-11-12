import cv2


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_good.xml")

mycam = cv2.VideoCapture(0)

while True:
    # Capture mypicture
    image, mypicture = mycam.read()

    imGray = cv2.cvtColor(mypicture, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        imGray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(mypicture, (x, y), (x+w, y+h), (255, 16, 240), 3)

    # Display the resulting frame
    cv2.imshow('Video', mypicture)

    if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cv2.imwrite("mypicture.png", mypicture)
# When everything is done, release the capture
mycam.release()
cv2.destroyAllWindows()

