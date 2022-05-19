import cv2
import face_recognition

img = cv2.imread("images/rich.jpg")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
encode = face_recognition.face_encodings(rgb)[0]

img2 = cv2.imread("images/rich2.jpg")
rgb2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
encode2 = face_recognition.face_encodings(rgb2)[0]

result = face_recognition.compare_faces([encode], encode2)
print("Result: ", result)

cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.waitKey(0)