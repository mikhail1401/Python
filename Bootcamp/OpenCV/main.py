import cv2

img = cv2.imread('test.jpg')    # read the image
print(img.shape)

img2 = cv2.resize(img, (500, 500))
print(img2.shape)

cv2.imshow('Original', img)     # display the image
cv2.imshow('Result', img2)

cv2.waitKey(0)      # wait for any key to close. 0 will never close

