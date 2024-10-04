import cv2

# Creating a face detector based on Hass Cascade algorithm
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Creating an object that will access the WebCam
cap = cv2.VideoCapture(0)   # 0 is the first camera, webcamera in my case

# Continuously capturing video frames from the webcam and displaying them in real-time
while True:
    # success is a boolean variable that indicates whether the frame was captures successfully
    # frame holds the actual image data of the captured frame
    success, frame = cap.read()

    # creating a window titled "Webcam" and displaying the original frame
    cv2.imshow("Webcam", frame)

    # making the frame mage gray to detect the face easier
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # finding the coordinates of the face(s)
    faces = face_cascade.detectMultiScale(img_gray)

    # drawing the face border over the frame
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # creating a window titled "Result" and displaying the frame with the face border overlay
    cv2.imshow("Result", frame)

    # updating the display every 1 milisecond and exiting the loop once 'q' is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):     # the frame will update every 1 milisecond
        break   # Exit loop if 'q' is pressed

