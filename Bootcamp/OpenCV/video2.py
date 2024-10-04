import cv2

# Creating a face detector based on Hass Cascade algorithm
face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Assigning the picture to the variable and coloring it to gray to make it easier to detect the face
img_original = cv2.imread("face.jpg")
img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)     # converts the image to gray color space

# Finding the coordinates of the face
faces = face_cascades.detectMultiScale(img_gray)
print(faces)    # returns the coordinates of the beginning of the fase and its size in pixels

# Overalying the face border on the original image
for (x, y, w, h) in faces:
    # rectangle (img, beginnning coordinates, end coordinates, color, thickness)
    cv2.rectangle(img_original, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Displaying the original picture with the face border
cv2.imshow('Result', img_original)
cv2.waitKey(0)