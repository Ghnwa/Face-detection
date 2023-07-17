import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
url_phone = 'http://192.168.43.13:8080/video'
cap = cv2.VideoCapture(0)#'http://192.168.43.1:8080/vedio'
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
#resized = cv2.resize(cap,(600,400))
#cv2.imshow("frame",resized)
#cap = resized
while True:
    # Read the frame
    _, frame = cap.read()
    img = cv2.resize(frame,(20,30))
    img = frame
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()
