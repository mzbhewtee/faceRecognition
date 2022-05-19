import cv2
from simpleFaceRec import SimpleFacerec

sf = SimpleFacerec()
sf.load_encoding_images("images/")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    location, name = sf.detect_known_faces(frame)
    for loc, names in zip(location, name):
        top, right, bottom, left = (loc[0], loc[1], loc[2], loc[3])

        cv2.putText(frame, names,(left, top -10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,200),2)
        cv2.rectangle(frame, (left,top),(right,bottom),(0,0,200),2)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()