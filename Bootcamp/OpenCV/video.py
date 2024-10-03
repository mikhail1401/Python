import cv2

cap = cv2.VideoCapture(0)   # 0 is the first camera, webcamera in my case

while True:
    success, frame = cap.read()     # success is a boolean variable that tells if the next frame is gotten successfully
    cv2.imshow("Webcam", frame)     # both success and frame will get value from cap.read()

    if cv2.waitKey(1) & 0xff == ord('q'):     # the frame will update every 1 milisecond
        break   # Exit loop if 'q' is pressed