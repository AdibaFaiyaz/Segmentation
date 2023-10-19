from roboflow import Roboflow
import cv2

rf = Roboflow(api_key="6n4JBtINCrh1xThmVtlc")
project = rf.workspace().project("custom-road-detection")
model = project.version(1).model

cap = cv2.VideoCapture("test.mp4")
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame', frame)
        model.predict(frame)


        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()