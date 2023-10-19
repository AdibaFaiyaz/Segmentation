import os
import cv2

currentframe = 0
try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

list_of_vids = os.listdir("Vids")
for vid in list_of_vids:
    cam = cv2.VideoCapture("./Vids/"+vid)
    if cam.isOpened:
        while True:

            # reading from frame
            ret, frame = cam.read()

            if ret:
                # if video is still left continue creating images
                name = './data/frame' + str(currentframe) + '.jpg'
                print('Creating...' + name)
                cv2.imwrite(name, frame)
                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
            else:
                break


#use face-recognition library to recheck whether the faces in the faces dir are actual faces (as dlib is installed in tf)
#if no face then delete the file, check using model=cnn