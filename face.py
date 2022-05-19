import cv2
from simpleFaceRec import SimpleFacerec


# Instantiate simplefacerec
sf = SimpleFacerec()

# load and encode the images 
sf.load_encoding_images("images/")

# Open the camera and give it a variable
cap = cv2.VideoCapture(0) # The zero is used when you have one camera, incase of front and back camera use 1 for front camera andd 0 for back camera 2 for webcam

# While the camera is open
while True:

    # read the content of the camera
    ret, frame = cap.read()

    # get the location and name of the face recognized
    location, name = sf.detect_known_faces(frame) #detect known faces is use to detect the face in the camera

    # location and names in the captured image
    for loc, names in zip(location, name):

        # set the position 
        top, right, bottom, left = (loc[0], loc[1], loc[2], loc[3])

        # retrive the name of the images, this is gotten from the names stored in the images file
        # set the location where the name will be store, the font, colour, and thickness
        cv2.putText(frame, names,(left, top -10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,200),2)

        # draw a rectangle across the face recognised, the colour, and thickness
        cv2.rectangle(frame, (left,top),(right,bottom),(0,0,200),2)

    # display the camera in the frame
    cv2.imshow("Frame", frame)

    # keep the frame running except the programme is stopped
    key = cv2.waitKey(1)
    if key == 27:
        break

# stop the camera and destroy the window
cap.release()
cv2.destroyAllWindows()