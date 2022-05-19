import cv2
import face_recognition


# read an image
img = cv2.imread("images/rich.jpg")

# convert the colior format from brg to rgb
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# encode the image
encode = face_recognition.face_encodings(rgb)[0]


# Do the same thing for the second image that is to be compared
img2 = cv2.imread("images/rich2.jpg")
rgb2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
encode2 = face_recognition.face_encodings(rgb2)[0]

# compare the images
result = face_recognition.compare_faces([encode], encode2)

# print the result
print("Result: ", result)

cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.waitKey(0)